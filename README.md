# 🎬 AI 视频微短剧分镜编剧 Skill (v1.2.1)

> 将故事创意、大纲或剧本转化为符合影视视听语言的工业级标准化分镜表，输出深度兼容 Midjourney / Flux / Runway / Kling / MiniMax 等主流 AI 视频生成工具链的多模态参考参数（`--cref` / `--sref` / `--oref`）与官方运镜控制指令。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.2.1-blue.svg)]()
[![Architecture](https://img.shields.io/badge/Architecture-Dual--Mode%20Production%20Core-purple.svg)]()
[![Stack](https://img.shields.io/badge/AI%20Stack-Midjourney%20%7C%20Flux%20%7C%20Runway%20%7C%20Kling%20%7C%20MiniMax-green.svg)]()

---

## 📌 核心定位与设计哲学

专为 **1~3 分钟** 微短剧、电影级叙事短片及 AI 视频前期卡前设计（Pre-visualization）打造。

> [!IMPORTANT]
> **最高原则：绝不允许为了死板满足规则而牺牲影视叙事逻辑与视听张力！**  
> 规则是保障 AI 视频生成可行性与空间几何严谨性的工业底线，而镜头的灵魂在于叙事推进、人物情绪起伏与观众心理节奏。

---

## 🌟 官方实战案例直观展示（Featured Showcase）

为让用户能最直观地感受本 Skill 的实际输出效果，本项目内置了一份完整的**9:16 竖屏科幻悬疑微短剧**示范全案：

### 📺 案例：《我死后的第七天，AI给我打来了电话》
- **剧本原点**：程序员在妹妹去世第七天接到她的来电，电话警告“别碰电脑”，电脑屏幕却打出“她在骗你”……
- **输出成果**：[👉 查看完整 26 镜工业级分镜全案 (examples/ai_call_showcase.md)](examples/ai_call_showcase.md)

#### 🚀 Skill 核心转化亮点展示：
| 转化维度 | 用户原始初稿 | Skill 工业级视听重构 |
|---|---|---|
| **画幅与构图** | 抽象描述 | **9:16 竖屏电影级构图**，生图词带 `--ar 9:16 --style raw`，增强纵向窒息感 |
| **音画台词匹配** | 台词塞爆（如 2 秒塞 32 字） | **人类发音物理受控**：严格限制字数 `≤ 秒数 × 4.5 字`，杜绝配音穿帮 |
| **动作安全度** | 复合动作（“踉跄后退撞翻椅子”） | **严格单一微动态拆解**：镜 18（失力后退）+ 镜 19（办公椅倒地特写），消除 AI 穿模 |
| **剪辑节奏** | 机械定长 | **蒙太奇快慢相间**：悬念建立（2.0s~2.5s）→ 危机高潮（1.0s 快切）→ 终极反转（2.0s~2.5s 缓释），精确 45.0 秒累加 |
| **角色连续性** | 仅纯文字 Prompt（必然漂移） | **绑定多模态参考图资产**：`--cref [URL] --cw 100`（锁定林川病容面容与灰卫衣）+ I2V 首帧管线 |
| **声音设计** | 粗略音效 | **全流程四轨工程**：Ambience（雨夜底噪）、Foley（按键拟音）、SFX（警报电磁）、BGM（大提琴史诗悲鸣） |

#### 🎬 分镜表精彩片段预览（节选自 PART 4）：
| 镜号（时间戳） | 画面与动作描述 (单一微动态) | 英文生图与运镜控制提示词 | 旁白 / 对白 (字数受控) | 景别与机位 | 音效与声音设计 |
|---|---|---|---|---|---|
| **01** (00:00.0-00:02.5)<br>时长: 2.5s | 竖屏全景建立：昏暗狭窄的出租屋内暴雨抽打窗户。林川穿着宽大灰卫衣孤身弓背坐在电脑前，桌上一张发黄的兄妹合照泛着微光。 | 🖼️ **IMG**:<br>`Vertical 9:16 establishing shot, dark apartment at midnight, rain on window, pale East Asian man in oversized hoodie at glowing desk, framed photo, deep cyan shadows --ar 9:16 --style raw --sref https://asset.film/styles/cyber_noir_bedroom.png`<br>🎬 **MOT**:<br>`Camera: Slow Zoom In (Speed 1). Subject: minimal breathing movement.` | `[无台词]` | **WS**<br>垂直俯角慢推 | **Amb**: 窗外密集雨声雷鸣<br>**Fol**: 主机风扇低频嗡鸣<br>**BGM**: 孤寂电钢琴单音（A minor） |
| **02** (00:02.5-00:04.0)<br>时长: 1.5s | 桌面手部微距：放在桌角右侧的手机屏幕骤然亮起刺眼白光并持续剧烈震动。屏幕显示来电人：“妹妹——林小雨”。 | 🖼️ **IMG**:<br>`Macro close-up vertical shot of smartphone vibrating intensely, screen displaying incoming call "Sister - Lin Xiaoyu", shallow depth of field --ar 9:16 --style raw`<br>🎬 **MOT**:<br>`Camera: Static macro. Subject: phone vibrating slightly on desk surface.` | `[无台词]` | **ECU**<br>微距俯拍固定 | **Fol**: 手机高频震动摩擦声<br>**SFX**: 电子来电急促蜂鸣<br>**BGM**: 钢琴骤停，低频嗡鸣升起 |
| **03** (00:04.0-00:05.5)<br>时长: 1.5s | 林川面部特写：手机冷白光照亮他惨白的面孔。他瞳孔猛烈收缩，喉结上下剧烈滑动，眼神陷入极度恐惧。 | 🖼️ **IMG**:<br>`Vertical close-up of East Asian man 25yo, pale skin with dark circles, messy black hair, cold screen light, pupils dilated in terror --ar 9:16 --style raw --cref https://asset.film/chars/lin_chuan_ref.png --cw 100`<br>🎬 **MOT**:<br>`Camera: Static. Subject: sudden pupil constriction, rapid throat swallow.` | 林川（极度颤抖，6字）：<br>“小雨……已经死了。” | **CU**<br>正面平视固定 | **Amb**: 空间死寂<br>**Fol**: 极沉重的倒抽凉气声<br>**BGM**: 大提琴不协和长音升至 7.0 |

> 完整 26 镜请参阅：[👉 examples/ai_call_showcase.md](examples/ai_call_showcase.md)

---

## 📂 项目结构

```
AI_grenerate_content_skill/
├── README.md                           # 项目说明与工业指南
├── examples/
│   └── ai_call_showcase.md             # 官方示范全案（《我死后的第七天，AI给我打来了电话》26镜竖屏工业全案）
└── skills/
    └── ai-video-storyboard/
        ├── SKILL.md                    # 核心 System Prompt（自包含工业闭环内核 v1.2.1）
        └── references/
            ├── production_example.md   # 生产级示范案例备份
            ├── storyboard_schema.json  # 工业级 17 字段 JSON Schema（支持自动化流水线对接）
            ├── prompt_engineering_guide.md # 现代 AI 工具官方参数与 I2V 管线手册
            ├── validation_checklist.md # 自动化七项自检与 13 项验收标准手册
            └── cinematic_language_guide.md # 影视视听语言与景别运镜语法速查
```

---

## 🚀 六大模块输出排版契约 (PART 1 ~ PART 6)

```
用户输入（故事/剧本/创意）
        │
        ▼
[PART 1] 剧作七维架构解构卡           ── 事件、动机、关系、攻防态势、空间、张力曲线、影调
        │
        ▼
[PART 2] 视觉资产与多模态锚点锁定卡   ── 绑定 --cref / --oref 角色参考、--sref 风格参考与服装道具
        │
        ▼
[PART 3] 场景空间几何与 180° 轴线规划 ── 确立三维坐标、左右视线、摄影机安全半圆
        │
        ▼
[PART 4] 工业级标准化分镜表 (6 列表格)── 镜号时码、单一微动态、双通道提示词、字数受控台词、景别运镜、四轨音频
        │
        ▼
[PART 5] 自动化七项深度规则自检报告   ── 严格按 Item 1 至 Item 7 客观真实审查判定
        │
        ▼
[PART 6] 反馈与局部重构指引           ── 锁定未变镜头，维护剪辑点，时码自动重排
```

---

## 📋 13 项工业级验收标准清单 (Acceptance Criteria)

| 编号 | 验收维度 | 核心检验逻辑与合格判定条件 |
|:---:|---|---|
| **AC-01** | **镜头时长安全窗口** | 全片 100% 镜头处于安全窗口内（默认 ≤ 3.0s，或符合指定模型窗口）。 |
| **AC-02** | **剪辑节拍呼吸感** | 全片时长打破死板统一定长，高潮动作戏配置 1.0s~1.5s 快切，快慢张弛有度。 |
| **AC-03** | **台词音画物理匹配** | 单镜台词字数严格 ≤ `时长 × 4.5 字`，长台词必须拆短或标注跨镜延展。 |
| **AC-04** | **轴线空间合理性** | 双人及多人交互全流程无违规跳轴，视线对撞完全符合空间几何。 |
| **AC-05** | **越轴过渡合规性** | 艺术越轴必须具备轨道移动镜头、中性正面镜头或走位过渡。 |
| **AC-06** | **核心情绪特写覆盖** | 冲突爆发点与心理转折点均配置正面面部 CU/ECU 或手部特写。 |
| **AC-07** | **非机械化叙事设计** | 脱离逐字直译，建立镜头、倾听反应镜头与隐喻插入镜头占比 ≥ 25%。 |
| **AC-08** | **微动态物理可行性** | 每个分镜严格恪守单一微动作，严禁复合运动，彻底消除 AI 畸变。 |
| **AC-09** | **角色多模态连续性** | 角色显式绑定 `--cref` / `--oref` 或 I2V 首帧参考资产，全片外观严格一致。 |
| **AC-10** | **服装与道具守恒性** | 同序列内服装款式、面料颜色及道具持有状态严格闭环。 |
| **AC-11** | **画幅与生图参数规范** | 明确指定画幅（横屏 `--ar 16:9`，竖屏 `--ar 9:16`），并包含 `--style raw`。 |
| **AC-12** | **运镜官方参数规范** | MOT 提示词采用各平台官方运镜参数（Runway 运镜 / Kling 轴向滑块参数）。 |
| **AC-13** | **自检报告对齐完整** | 输出报告严格包含第 1 项至第 7 项完整真实审查结果，且所有红线项全部为 PASS。 |

---

## 🛠️ 兼容现代 AI 工具链

| 环节 | 主流支持工具 | 工业控制标准 |
|---|---|---|
| **角色与风格参考** | Midjourney v6/v7, Flux 1.0 (PuLID/LoRA) | `--cref [URL] --cw 100` / `--oref [URL]` / `--sref [URL] --sw 800` |
| **视频运镜与动力学** | Runway Gen-3/4, Kling 1.6/2.0, MiniMax Hailuo | 官方 Camera Control 参数 / 6 轴运镜滑块 / 首尾帧控制 |
| **全流程声音设计** | Suno, Udio, ElevenLabs, 剪映专业版 | 详尽标注 Ambience、Foley、SFX 与 BGM 四轨工程 |

---

## 📖 使用方法

1. **直接作为 System Prompt**：复制 [SKILL.md](skills/ai-video-storyboard/SKILL.md) 纯文本至你的 AI 平台（Claude、ChatGPT、Dify、Antigravity IDE）。
2. 输入你的故事或剧本。
3. 系统将全自动完成七维解构、多模态资产绑定、轴线推演、分镜生成与自检报告交付！

---

## 📄 开源许可

本项目基于 [MIT License](LICENSE) 许可开源。
