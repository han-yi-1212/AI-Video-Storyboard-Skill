"""
工业级分镜自动化契约测试套件 (Storyboard Contract & Timing Test Suite V2.0)
验证分镜方案的时间戳连续性、单镜时长区间、台词字数物理限制、以及文档间的一致性。
"""

import re
import os
import unittest

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOWCASE_FILE = os.path.join(WORKSPACE_ROOT, "examples", "ai_call_showcase.md")
PROD_EXAMPLE_FILE = os.path.join(WORKSPACE_ROOT, "skills", "ai-video-storyboard", "references", "production_example.md")
SKILL_FILE = os.path.join(WORKSPACE_ROOT, "skills", "ai-video-storyboard", "SKILL.md")
CHECKLIST_FILE = os.path.join(WORKSPACE_ROOT, "skills", "ai-video-storyboard", "references", "validation_checklist.md")
README_FILE = os.path.join(WORKSPACE_ROOT, "README.md")


class TestStoryboardContract(unittest.TestCase):

    def parse_storyboard_table(self, file_path):
        """解析 Markdown 表格中的镜号与时间戳"""
        self.assertTrue(os.path.exists(file_path), f"文件不存在: {file_path}")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        pattern = r"\*\*([0-9]{2})\*\*.*?\((\d{2}):(\d{2}\.\d)-(\d{2}):(\d{2}\.\d)\).*?时长:\s*(\d+\.?\d*)s"
        matches = re.findall(pattern, content, re.DOTALL)
        
        shots = []
        for m in matches:
            shot_id = m[0]
            st_min, st_sec = int(m[1]), float(m[2])
            ed_min, ed_sec = int(m[3]), float(m[4])
            duration = float(m[5])
            
            start_time = round(st_min * 60 + st_sec, 2)
            end_time = round(ed_min * 60 + ed_sec, 2)
            
            shots.append({
                "shot_id": shot_id,
                "start": start_time,
                "end": end_time,
                "duration": duration
            })
        return shots, content

    def test_showcase_26_shots_timing_continuity(self):
        """测试 26 镜实战全案的时间戳严格连续性与时长数学计算"""
        shots, content = self.parse_storyboard_table(SHOWCASE_FILE)
        self.assertEqual(len(shots), 26, f"应包含 26 个分镜，实际解析到 {len(shots)}")

        # 验证首镜从 0.0s 开始
        self.assertEqual(shots[0]["start"], 0.0, "首镜必须从 00:00.0 开始")

        prev_end = 0.0
        total_duration = 0.0
        for s in shots:
            # 1. 验证时间戳连续性：后镜 start == 前镜 end
            self.assertAlmostEqual(s["start"], prev_end, delta=0.05,
                                   msg=f"镜头 {s['shot_id']} 出现时间戳跳跃: start={s['start']} != prev_end={prev_end}")
            
            # 2. 验证单镜计算一致性：end - start == duration
            calc_dur = round(s["end"] - s["start"], 2)
            self.assertAlmostEqual(calc_dur, s["duration"], delta=0.05,
                                   msg=f"镜头 {s['shot_id']} 时长计算错误: end-start={calc_dur} != duration={s['duration']}")
            
            # 3. 验证安全窗口：单镜不超过 3.0s
            self.assertLessEqual(s["duration"], 3.0, f"镜头 {s['shot_id']} 超出安全上限 3.0s")
            self.assertGreaterEqual(s["duration"], 0.8, f"镜头 {s['shot_id']} 低于极限下限 0.8s")

            prev_end = s["end"]
            total_duration += s["duration"]

        # 验证精确总时长为 45.0s
        self.assertAlmostEqual(total_duration, 45.0, delta=0.1, msg=f"总时长应为 45.0s，实际为 {total_duration}")
        self.assertAlmostEqual(shots[-1]["end"], 45.0, delta=0.1, msg=f"末镜结束时间应为 45.0s，实际为 {shots[-1]['end']}")

    def test_speech_rate_limits_in_showcase(self):
        """测试台词字数与镜头秒数必须符合人类物理发音上限 (<= 时长 * 4.5 字)"""
        with open(SHOWCASE_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        table_rows = [l for l in lines if l.startswith("| **")]
        for row in table_rows:
            cols = [c.strip() for c in row.split("|")]
            if len(cols) < 7:
                continue
            
            shot_col = cols[1]
            dialogue_col = cols[4]

            # 提取时长
            dur_m = re.search(r"时长:\s*(\d+\.?\d*)s", shot_col)
            if not dur_m:
                continue
            duration = float(dur_m.group(1))

            # 忽略无台词
            if "[无台词]" in dialogue_col or not dialogue_col:
                continue

            # 过滤全角/半角括号及说明，如：林川（极度颤抖，6字）：<br>“小雨……已经死了。”
            dialogue_text = re.sub(r"[（\(].*?[）\)]", "", dialogue_col)
            dialogue_text = re.sub(r"^.*?：", "", dialogue_text)
            dialogue_text = re.sub(r"<br\s*/?>", "", dialogue_text)
            dialogue_text = re.sub(r"[^\u4e00-\u9fa5]", "", dialogue_text)
            char_count = len(dialogue_text)

            max_allowed = int(duration * 4.5) + 1  # 允许 1 个字浮动容差
            self.assertLessEqual(char_count, max_allowed,
                                 msg=f"镜头台词超长超速! 时长 {duration}s，字数 {char_count}，允许上限 {max_allowed}，台词: {dialogue_text}")

    def test_production_example_timing(self):
        """测试 production_example.md 9 镜时长累加严格为 14.0s"""
        shots, _ = self.parse_storyboard_table(PROD_EXAMPLE_FILE)
        self.assertEqual(len(shots), 9, f"production_example 应为 9 镜，实际为 {len(shots)}")
        
        prev_end = 0.0
        for s in shots:
            self.assertAlmostEqual(s["start"], prev_end, delta=0.05)
            prev_end = s["end"]

        self.assertAlmostEqual(shots[-1]["end"], 14.0, delta=0.1)

    def test_acceptance_criteria_cross_file_consistency(self):
        """测试 13 项验收标准编号在所有文档中完全一致 (AC-01 ~ AC-13)"""
        files_to_check = [SKILL_FILE, CHECKLIST_FILE, README_FILE]
        for fpath in files_to_check:
            self.assertTrue(os.path.exists(fpath))
            with open(fpath, "r", encoding="utf-8") as f:
                c = f.read()
            for i in range(1, 14):
                ac_code = f"AC-{i:02d}"
                self.assertIn(ac_code, c, f"文档 {os.path.basename(fpath)} 缺少验收标准 {ac_code}")


if __name__ == "__main__":
    unittest.main()
