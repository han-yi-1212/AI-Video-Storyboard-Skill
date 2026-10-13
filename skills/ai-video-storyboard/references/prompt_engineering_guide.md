# AI 视频工具提示词工程参考手册

本文档为分镜表第三列（英文生图/运镜提示词）的编写提供详细参考。

---

## 一、Midjourney v6/v7 提示词结构

### 基础框架

```
[主体] + [动作/姿态] + [外貌/服装锚点] + [环境] + [光影] + [景别] + [风格]
+ 技术参数
```

### 关键参数

| 参数 | 说明 | 推荐值 |
|---|---|---|
| `--ar` | 宽高比 | `16:9`（横屏）/ `9:16`（竖屏短视频） |
| `--s` | 风格化强度 | `250–750`（越低越写实） |
| `--style raw` | 减少 MJ 默认美化 | 搭配写实风格使用 |
| `--c` | 混乱度 | `0–20`（越低越可控） |
| `--no` | 负面提示 | `--no text, watermark, logo, blurry` |
| `--seed` | 固定种子 | 用于同一角色跨镜头一致性测试 |

### 写实电影风格锁定词库

```
cinematic still, photorealistic, 8K, film grain, anamorphic lens,
shallow depth of field, volumetric lighting, color graded,
shot on Arri Alexa Mini, 35mm film aesthetic
```

### 光影描述词库

| 情绪 | 光影词 |
|---|---|
| 温暖亲密 | warm golden hour light, soft diffused window light, amber glow |
| 冷酷疏离 | cold blue moonlight, harsh fluorescent overhead, sterile white light |
| 悬疑紧张 | single harsh side light, dramatic chiaroscuro, deep shadows |
| 恐怖压迫 | sickly green tint, flickering light, underlit from below |
| 浪漫梦幻 | soft pastel light leak, gentle backlit haze, pink-gold tones |
| 史诗宏大 | dramatic god rays, volumetric mist, epic golden light |

---

## 二、Flux 提示词特性

### 与 MJ 的差异

- Flux 更偏向自然语言描述，不使用 `--ar` 等参数标记
- 更擅长理解完整句子描述
- 对细节描述的响应更精确

### Flux 模板

```
A cinematic still photograph of [subject description].
[Action/pose]. [Wardrobe details]. [Environment description].
[Lighting setup]. Shot in [shot type].
Photorealistic, 8K resolution, film grain texture.
Aspect ratio 16:9.
```

---

## 三、Runway Gen-3/4 Alpha 运动提示词

### 结构

```
Camera: [camera movement description]
Subject: [subject motion description]
Background: [environmental motion description]
```

### 运动强度控制词

| 强度 | 英文描述 |
|---|---|
| 极微 | imperceptible, barely noticeable, ultra-subtle |
| 轻微 | subtle, gentle, slight, soft |
| 中等 | moderate, steady, smooth |
| 强烈 | dramatic, intense, rapid, sharp |
| 极端 | explosive, violent, extreme |

### 常用摄影机运动组合

```
Camera: slow dolly in, gentle steady speed.
Camera: static, locked-off shot.
Camera: lateral tracking right, moderate pace.
Camera: slow crane up revealing landscape.
Camera: handheld with subtle shake, documentary feel.
Camera: slow orbit clockwise around subject.
Camera: whip pan left to right, fast.
Camera: very slow zoom in, almost imperceptible.
```

### 常用主体运动描述

```
Subject: subtle breathing motion, slight chest rise and fall.
Subject: slow head turn from left to right.
Subject: single tear rolling down cheek.
Subject: fingers slowly clenching into fist.
Subject: hair gently blowing in breeze.
Subject: walking forward at slow pace.
Subject: eyes darting nervously left and right.
Subject: mouth opening slightly as if about to speak.
```

---

## 四、Kling 1.6+ 运动提示词

### 结构特点

- Kling 偏好简洁直接的运动描述
- 支持中英文混合（但英文效果更稳定）
- 建议每个维度（摄影机/角色/环境）各一句

### 模板

```
Camera motion: [movement type and direction].
Character action: [single specific action].
Environment: [ambient motion details].
Style: cinematic, photorealistic.
```

### 注意事项

- 避免描述超过 2 个并发动作
- 角色动作必须是单一微动态
- 明确标注动作的起止状态

---

## 五、MiniMax Hailuo 运动提示词

### 结构特点

- 更接近自然语言叙述
- 将场景描述和运动融合在一段话中
- 对氛围和情绪词响应较好

### 模板

```
A cinematic scene where [subject] [action] in [environment].
The camera [movement description].
[Atmospheric and mood details].
Cinematic quality, smooth natural motion, photorealistic.
```

---

## 六、跨镜头一致性维护策略

### 角色一致性

1. **锚点词复用**：每个镜头的 IMG prompt 必须包含角色的完整锚点词
2. **种子锁定**（MJ）：使用 `--seed` 参数在关键镜头间保持一致性
3. **参考图引导**：使用前序镜头生成的图像作为后续镜头的参考（`--cref`）
4. **负面提示统一**：所有镜头使用相同的 `--no` 列表

### 场景一致性

1. **环境锚点词复用**：同一场景的所有镜头共享环境描述
2. **光影一致**：同一场景同一时间段的光影描述保持统一
3. **色温锁定**：明确标注色温（warm 3200K / neutral 5600K / cool 7000K+）

### 情绪一致性

1. **渐进变化**：情绪关键词应在相邻镜头间呈现渐进变化
2. **避免跳变**：不要在相邻镜头中突然切换完全相反的情绪描述
3. **动作衔接**：上一镜的结束动作 = 下一镜的起始状态

---

## 七、常见错误与修正

| ❌ 错误 | ✅ 修正 | 原因 |
|---|---|---|
| `a man running and jumping over a table` | 拆分为两个镜头 | 复合动作导致穿模 |
| `beautiful cinematic scene` | 具体描述光影和构图 | 模糊词无法生成精确画面 |
| `the character looks sad` | `brows furrowed, eyes downcast, lips slightly parted, hollow gaze` | 情绪需要具象化 |
| 不同镜头中角色描述不一致 | 统一使用锚点词 | 会导致角色外观漂移 |
| `Camera moves around while character runs and talks` | 拆分运动维度 | 并发运动超出模型能力 |
| 使用中文在英文prompt中 | 全部翻译为英文 | 影响模型理解 |
