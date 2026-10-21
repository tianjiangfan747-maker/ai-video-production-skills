---
name: style-quality-boost
description: 广告/短视频视觉的"质感提升"与"风格化"增强技能。当用户要求提升画面质感、让视频更有独特风格/更吸引人/更特别、需要多巴胺配色、网红风角色设计或任何风格化创意设计，或觉得生成画面"平、廉价、没记忆点、不像大片"时使用。风格不局限于某一种，按项目选方向。适用于即梦、可灵、Seedance、Vivago/HiDream、Catnip 等文生/图生视频与图像流程的 prompt 强化与成片 QC。
---

# style-quality-boost：质感与风格化增强

两条独立能力，可单独用也可叠加：**质感（Texture/Quality）** 解决"看起来像随手拍/像AI塑料感"；**风格化（Stylization）** 解决"没有记忆点、不网红、不多巴胺"。

## 一、质感提升（Quality Boost）

### 1. 诊断清单（先看缺哪层）
按顺序检查画面缺什么，缺什么补什么，不要全堆：
- **光线层**：是否平光/大平光？→ 需要方向性光（侧逆光、黄金时刻、轮廓光 rim light）
- **材质层**：皮肤/布料/食物/金属是否有微观细节？→ 需要质地词（sweat beads, fabric weave, condensation, brushed metal）
- **镜头层**：是否像监控摄像头？→ 需要镜头语言（35mm/85mm 焦段、浅景深 f/1.8、手持微晃、推拉摇移）
- **色彩层**：是否灰/脏/饱和度过低？→ 需要调色锚点（teal-orange、film grain、 Kodak Portra 400）
- **运动层**：是否静止或匀速？→ 需要速度变化（slow motion 120fps、whip pan、speed ramp）

### 2. 质感 prompt 词库（按层取用，每层 1-2 个即可）
| 层 | 英文关键词（直接进 prompt） | 中文说明 |
|---|---|---|
| 光线 | golden hour backlight, soft diffused window light, neon rim light, volumetric light rays | 黄金时刻逆光 / 柔光窗光 / 霓虹轮廓光 / 体积光 |
| 材质 | glossy skin with subtle sweat, crispy golden crust with steam, liquid slow-motion swirl, fabric texture close-up | 皮肤微汗 / 酥脆蒸汽 / 液体慢动作 / 织物特写 |
| 镜头 | shot on ARRI Alexa, 85mm f/1.4 shallow depth of field, cinematic dolly-in, handheld documentary feel | 电影机质感 / 浅景深 / 推轨 / 手持纪实 |
| 调色 | teal and orange grade, Kodak Portra 400 film look, high contrast cinematic LUT, subtle film grain | 青橙调 / 胶片感 / 高对比电影 LUT / 颗粒 |
| 运动 | 120fps slow motion, speed ramping, whip pan transition, macro probe lens shot | 升格 / 变速 / 甩镜 / 探针微距 |

### 3. 反面词（必须避免的画面特征）
flat lighting, washed out colors, plastic skin, stock photo look, cluttered background, jittery camera, low resolution texture, overexposed highlights

## 二、风格化（Stylization）

核心目标：**让广告有辨识度、抓眼球、让人停下来**。风格不是固定某一种——先按产品和受众选方向，再把风格执行到底。风格化 = 一套统一的"配色 + 光线 + 造型 + 字体/花字 + 剪辑节奏"组合，最怕半途混风格。

### 0. 风格选型流程（先做这个）
1. 看产品调性和受众（如 Catnip = 北美 18–34 年轻女性 → 适合多巴胺/ins 网红风；奢侈品 → 极简高级）
2. 从下方风格库选 1 个主方向，写出**风格词板**（3-5 个关键词 + 1 张参考图）
3. 全片所有镜头只用这一套词板，不混搭

### 1. 风格库（按项目选用，每条广告只选一个）

**A. 多巴胺风（Dopamine）** — 快消、美妆、零食、社交 App
- 配色锚点：① 亮黄+宝蓝+玫红 ② 薄荷绿+珊瑚橙+紫 ③ 荧光粉+柠檬黄+青
- prompt 模板：`vibrant dopamine color palette, [亮黄+宝蓝] color blocking background, playful geometric props, hard studio flash lighting, pop art composition, gen-z aesthetic, bold saturated colors, clean seamless backdrop`
- 人物造型：oversized 彩色西装、撞色眼妆、果冻感配饰
- 禁忌：莫兰迪色、留白过多、写实自然光

**B. 网红风角色设计（Influencer/Ins Style）** — 社交 App、生活方式产品
- 角色锚点公式：`[年龄段+人种] [发型发色] [标志性单品] [妆容特征] [拍摄场景]`
  - 例：`22岁亚裔女生，黑长直+齐刘海，crop top + 低腰牛仔裤 + 腋下包，水光肌+玻璃唇，奶油色卧室对镜自拍`
- 氛围词：`clean girl aesthetic, soft pink bedroom, mirror selfie angle, golden hour selfie light, that girl morning routine vibe`
- 细分：Clean Girl（奶油极简）、Y2K（千禧辣妹）、Mob Wife（复古浓颜）、Office Siren（职场御姐）、Cottagecore（田园）

**C. 复古胶片风（Retro Film）** — 音乐、咖啡、服饰、情怀类产品
- 关键词：`shot on 16mm film, heavy film grain, faded warm tones, halation on highlights, vintage 90s camcorder aesthetic, nostalgic haze`
- 光线：夕阳、钨丝灯、过曝窗户光

**D. 怪诞超现实风（Surreal/Weird-core）** — 需要强记忆点的病毒式广告
- 关键词：`surreal absurd scene, oversized everyday objects, dreamlike logic, unexpected scale shift, deadpan humor, viral ad aesthetic`
- 玩法：把产品放进不合常理的场景（沙发上长出朋友、客厅里下起爆米花雨）

**E. 极简高级风（Minimal Premium）** — 数码、汽车、高端护肤
- 关键词：`minimalist studio, single directional light, lots of negative space, matte texture, monochrome with one accent color, architectural composition`

**F. 手绘/插画混合风（Mixed Media）** — 年轻品牌、App 功能演示
- 关键词：`mixed media animation, doodle overlays on live action, hand-drawn scribble effects, paper collage texture, stop-motion feel`

### 2. 风格化执行规则
1. 写 prompt 时**风格词前置**（模型对前 1/3 权重更高）
2. 同一个角色跨镜头时，把角色锚点公式**逐字复制**到每个镜头 prompt，只改动作和机位
3. 花字/字幕样式也要服从风格（多巴胺=粗体圆体字+撞色描边；极简=细体无衬线+大量留白）
4. 出片后对照风格词板逐条 QC

## 三、QC 检查表（成片验收用）
- [ ] 光线有方向、有层次，不是大平光
- [ ] 主体材质细节可见（皮肤/食物/面料/金属）
- [ ] 景深关系正确：主体实、背景虚化
- [ ] 配色符合风格锚点，无脏色、无偏色
- [ ] 角色跨镜头不漂移（发型/服装/妆容一致）
- [ ] 有至少一个"记忆点画面"（可截图当封面的帧）

## 四、与其他 skill 的协作
- 角色一致性 → 配合 `character-asset`
- 单镜头执行 prompt → 配合 `shot-execution`（把本技能的词库注入其模板）
- 成片验收 → 配合 `video-production-qc`（本清单并入其质感维度）
