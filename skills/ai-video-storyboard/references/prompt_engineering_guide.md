# 现代 AI 视频提示词工程与多模态资产控制手册
*(Modern AI Video Prompt Engineering & Asset Control Manual V1.2)*

本文档详细说明当前主流 AI 图像与视频生成平台在工业分镜制作中的**真实官方语法、多模态一致性控制参数与 I2V（Image-to-Video）管线规范**。

---

## 一、工业级核心工作流：I2V（首帧生视频）标准管线

在现代工业化 AI 视频生产中，**Text-to-Video (T2V) 直接纯文本生视频已不是首选**，因为纯文字描述无法保证角色五官细节、特定服装和复杂空间在多镜头间的跨镜头守恒。

当前行业的主流解法为 **I2V (Image-to-Video) 工业流水线**：
```
[剧作分镜] ──► [Midjourney / Flux 渲染起始帧关键帧]
                     │ (绑定 --cref 角色参考与 --sref 风格参考)
                     ▼
             [获得高一致性 Keyframe 起始帧图片]
                     │
                     ▼
             [输入 Runway / Kling / MiniMax 进行 I2V 运镜与微动态驱动]
                     │ (应用官方 Camera Control 与首尾帧技术)
                     ▼
             [最大化抑制面容漂移与背景畸变，获得稳定分镜视频]
```

---

## 二、图像端：多模态角色与风格一致性规范

### 1. Midjourney v6 / v7 官方一致性参数

| 参数 | 官方定义 | 工业推荐用法 |
|---|---|---|
| `--cref [URL]` | **Character Reference (角色参考)** | 传入角色的白底标准立绘或三视图 URL，锁定面部五官与骨骼轮廓。 |
| `--cw [0-100]` | **Character Weight (角色权重)** | `--cw 100`（默认值，同时参考面容、发型与服装）；`--cw 0`（仅锁定五官，允许更换新场景服装）。 |
| `--sref [URL]` | **Style Reference (风格参考)** | 传入目标影片的调色/光影参考图 URL，全剧镜头保持统一影调。 |
| `--sw [0-1000]` | **Style Weight (风格权重)** | 推荐设为 `--sw 800`，确保电影色调强力附着。 |
| `--oref [URL]` | **Object Reference (道具参考)** | 用于关键道具（特定公文包、U盘、钥匙串）的外观锁定。 |
| `--ar 16:9` | **Aspect Ratio (画幅比例)** | 微短剧横屏统一 `--ar 16:9`；竖屏短剧统一 `--ar 9:16`。 |
| `--style raw` | **Raw Mode (原始摄影质感)** | 消除 Midjourney 默认的过度平滑插画感，增强真实皮肤毛孔与胶片颗粒。 |

#### 标准生图 Prompt 结构示例：
```
Close-up portrait of East Asian woman late 20s, raven-black ponytail, sharp intelligent almond eyes, faint bead of sweat on temple, dark matte windbreaker, cinematic chiaroscuro lighting, photorealistic film still, 35mm lens --ar 16:9 --style raw --cref https://asset.film/anlan.png --cw 100 --sref https://asset.film/fincher.png --sw 800
```

### 2. Flux 1.0 / Stable Diffusion 生态
- **PuLID / IP-Adapter FaceID**：通过人脸特征向量提取保持五官一致性（权重推荐 0.75~0.85）。
- **LoRA**：为定制主角训练专属 Character LoRA，在提示词中显式调用 `<lora:character_anlan:0.8>`。
- **ControlNet OpenPose / Depth**：用于精确控制特定分镜中角色的复杂构图与机位透视。

---

## 三、视频端：主流平台官方运动控制与运镜参数

### 1. Runway Gen-3 / Gen-4 Alpha

Runway 依靠**官方 Camera Control 控制面板 + 自然语言动作物理指令**：

#### 官方 Camera Control 参数映射：
- **Pan (平移摇镜)**：`Pan Left / Right` (数值 1~10)
- **Tilt (俯仰摇镜)**：`Tilt Up / Down` (数值 1~10)
- **Zoom (变焦推拉)**：`Zoom In / Out` (数值 1~10)
- **Roll (轴向旋转)**：`Roll Clockwise / Counter-clockwise` (用于失衡/坠落)
- **Camera Speed (运镜速度)**：`Speed 1 (极缓) ~ 10 (极速)`

#### 真实工程提示词规范：
```
Camera: Slow Zoom In (Speed 2), locked on subject. The woman’s eyes dart sharply to frame-right, rapid subtle chest breathing, rain pouring on glass in blurred background.
```

### 2. 可灵 Kling 1.6+ (工业级标准)

可灵拥有最强大的三维运镜控制与首尾帧技术：

#### 官方控制参数体系：
- **运镜模式**：
  - `水平平移 (X)`：[-10 到 +10]
  - `垂直平移 (Y)`：[-10 到 +10]
  - `前后变焦 (Z)`：[-10 到 +10]（推进取正，拉远取负）
  - `水平旋转 (Yaw)`：[-10 到 +10]
  - `垂直俯仰 (Pitch)`：[-10 到 +10]
  - `滚动旋转 (Roll)`：[-10 到 +10]
- **首尾帧过渡 (First & Last Frame)**：
  - 提供第一帧（起始姿态）与最后一帧（终止姿态），AI 在两帧之间生成严格受约束的物理运动插值（适合精准开门、拔卡、倒地等关键动作）。
- **元素控制 (Elements)**：在官方库中上传角色模型，保证生视频时最大程度抑制换脸。

#### 真实工程提示词规范：
```
景别：特写。机位平视固定。单一动作：戴黑色手套的手以极快速度将金属U盘笔直拔出机箱插槽，手指带有轻微运动模糊。画面色调冷蓝，高对比度。
```

### 3. 海螺 MiniMax (Hailuo)

海螺模型对**自然语言的动作动词**理解极深，忌讳机械堆砌参数词，必须采用精炼的**电影指令级动词**：
- **原则**：只描述可见物理动作与摄影机真实轨迹。
- **示例**：
  ```
  Static camera. The woman's eyes whip to the right in sudden panic, her breath catching in her throat. Deep moody shadows, cold blue lighting.
  ```

---

## 四、镜头时长与剪辑节奏工程准则

| 场景类型 | 默认安全窗口时长 (≤3.0s 模式) | 扩展模型时长 (5s/10s 模式) | 典型景别与运镜 | 视听目的 |
|---|---|---|---|---|
| **悬念建立 / 环境交代** | 2.0s ~ 3.0s | 3.0s ~ 4.5s | WS / ELS，缓慢推进 (Slow Dolly In) | 交代地理坐标、世界观氛围、沉浸感建立 |
| **人物心理与微反应** | 1.5s ~ 2.0s | 2.0s ~ 3.0s | MCU / CU，固定 (Locked Static) | 捕捉微表情、呼吸与眼神焦距变化 |
| **突发危机与动作戏** | **1.0s ~ 1.5s (快切)** | **1.0s ~ 1.5s (快切)** | ECU / CU，极快动作或快速推镜头 | 极速提升心率、制造窒息感与动作压迫 |
| **结局余味 / 悬念留白** | 2.0s ~ 3.0s | 3.5s ~ 5.0s | MS / WS，缓慢拉远 (Dolly Out) 或定格 | 情绪释放、意象升华、留白回味 |

> [!TIP]
> **剪辑节拍铁律**：严禁整部短片采用单一相同秒数（如清一色 3.0s）。必须像交响乐般有长有短，动作戏务必使用 1.0s~1.5s 快切，环境与情绪戏给予 2.0s~3.0s 呼吸空间。
