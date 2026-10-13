# 🎬 AI 视频微短剧分镜编剧 Skill (v1.2.0)

> 将故事创意、大纲或剧本转化为符合影视视听语言的工业级标准化分镜表，输出深度兼容 Midjourney / Flux / Runway / Kling / MiniMax 等主流 AI 视频生成工具链的多模态参考参数（`--cref` / `--sref`）与官方运镜控制指令。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-1.2.0-blue.svg)]()
[![Architecture](https://img.shields.io/badge/Architecture-Dual--Mode%20Production%20Core-purple.svg)]()
[![Stack](https://img.shields.io/badge/AI%20Stack-Midjourney%20%7C%20Flux%20%7C%20Runway%20%7C%20Kling%20%7C%20MiniMax-green.svg)]()

---

## 📌 核心定位与设计哲学

专为 **1~3 分钟** 微短剧、电影级叙事短片及 AI 视频前期卡前设计（Pre-visualization）打造。

> [!IMPORTANT]
> **最高原则：绝不允许为了死板满足规则而牺牲影视叙事逻辑与视听张力！**  
> 规则是保障 AI 视频生成可行性与空间几何严谨性的工业底线，而镜头的灵魂在于叙事推进、人物情绪起伏与观众心理节奏。

---

## 🌟 v1.2.0 工业级双模架构 (Dual-Mode Production)

针对传统 Skill 容易出现“外部引用失效”或“主文件与配套文档版本漂移”的痛点，v1.2.0 采用**双模闭环设计**：

1. **单文件独立自包含（Standalone Mode）**：
   - 即使脱离配套目录，直接将 [SKILL.md](skills/ai-video-storyboard/SKILL.md) 复制到任意 AI 平台（ChatGPT、Claude、Dify 等）作为单一 System Prompt，它自身已完整内置 **13 项验收标准 (AC-01~13)**、**自动化七项自检 (Item 1~7)**、**多模态一致性规范** 与 **生产级示范案例**，完全自闭环运行。
2. **知识库深度联动（Agent Workspace Mode）**：
   - 在支持目录读取的智能体环境中，`SKILL.md` 正文显式链接到 `references/` 目录中的专门手册（包含 17 字段 JSON Schema、官方运镜参数速查、视听语言决策树等），实现深度扩展。

---

## 📂 项目结构

```
AI_grenerate_content_skill/
├── README.md                           # 项目说明与工业指南
└── skills/
    └── ai-video-storyboard/
        ├── SKILL.md                    # 核心 System Prompt（自包含完整闭环内核 v1.2.0）
        └── references/
            ├── production_example.md   # 生产级示范案例（快慢切节奏 / --cref 多模态资产 / 真实七项自检）
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
[PART 2] 视觉资产与多模态锚点锁定卡   ── 绑定 --cref 角色参考、--sref 风格参考与服装道具
        │
        ▼
[PART 3] 场景空间几何与 180° 轴线规划 ── 确立三维坐标、左右视线、摄影机安全半圆
        │
        ▼
[PART 4] 工业级标准化分镜表 (6 列表格)── 镜号时码、单一微动态、双通道提示词、台词、景别运镜、四轨音频
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
| **AC-03** | **轴线空间合理性** | 双人及多人交互全流程无违规跳轴，视线对撞吻合空间几何。 |
| **AC-04** | **越轴过渡合规性** | 艺术越轴必须具备轨道移动镜头、中性正面镜头或走位过渡。 |
| **AC-05** | **核心情绪特写覆盖** | 冲突爆发点与心理转折点均配置正面面部 CU/ECU 或手部特写。 |
| **AC-06** | **非机械化叙事设计** | 脱离逐字直译，建立镜头、倾听反应镜头与隐喻插入镜头占比 ≥ 25%。 |
| **AC-07** | **微动态物理可行性** | 每个分镜严格恪守单一微动作，严禁复合运动，彻底消除 AI 畸变。 |
| **AC-08** | **角色多模态连续性** | 角色显式绑定 `--cref` 或 I2V 首帧参考资产，全片英文外观描述严格一致。 |
| **AC-09** | **服装与道具守恒性** | 同序列内服装款式、面料颜色及道具持有状态严格闭环。 |
| **AC-10** | **光影氛围统一性** | 场景提示词中的主光源方向、色温与胶片调色词统一锁定。 |
| **AC-11** | **生图 Prompt 规范** | IMG 提示词完全符合 Midjourney / Flux 语法并带 `--ar 16:9` 与 `--style raw`。 |
| **AC-12** | **运镜官方参数规范** | MOT 提示词采用各平台官方运镜参数（Runway 运镜 / Kling 1.6+ 轴向滑块参数）。 |
| **AC-13** | **自检报告对齐完整** | 输出报告严格包含第 1 项至第 7 项完整真实审查结果，且所有红线项全部为 PASS。 |

---

## 🛠️ 兼容现代 AI 工具链

| 环节 | 主流支持工具 | 工业控制标准 |
|---|---|---|
| **角色与风格参考** | Midjourney v6/v7, Flux 1.0 (PuLID/LoRA) | `--cref [URL] --cw 100` / `--sref [URL] --sw 800` |
| **视频运镜与动力学** | Runway Gen-3/4, Kling 1.6+, MiniMax Hailuo | 官方 Camera Control 滑块参数 / 6 轴运镜滑块 / 首尾帧控制 |
| **全流程声音设计** | Suno, Udio, ElevenLabs, 剪映专业版 | 详尽标注 Ambience、Foley、SFX 与 BGM 四轨工程 |

---

## 📖 使用方法

1. **直接作为 System Prompt**：复制 [SKILL.md](skills/ai-video-storyboard/SKILL.md) 纯文本至你的 AI 平台（Claude、ChatGPT、Dify、Antigravity IDE）。
2. 输入你的故事或剧本。
3. 系统将全自动完成七维解构、多模态资产绑定、轴线推演、分镜生成与自检报告交付！

---

## 📄 开源许可

本项目基于 [MIT License](LICENSE) 许可开源。
