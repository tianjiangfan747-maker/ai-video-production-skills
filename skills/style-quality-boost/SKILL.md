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

### 3. 风险词（仅诊断命中时使用）
以下是需要观察的风险，不是每条 Prompt 都要复制的反面词尾巴：

`flat lighting / washed out colors / plastic skin / stock photo look / cluttered background / jittery camera / low resolution texture / overexposed highlights`

优先用正向设计解决，例如用“左侧柔光照亮面部，右侧保留柔和阴影”代替“不要平光、不要塑料感”。用户明确排除或该问题反复出现时，才保留一条针对性限制；已由参考图或正面描述覆盖的内容不再重复。输出前按 `shot-execution` 的语义审查压缩。

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
1. 把选定的风格方向表达清楚，风格词的位置按模型实测调整，不假定“前 1/3 永远权重更高”。
2. 跨镜头复用同一份风格合同与身份资产。强参考图已锁定角色时，不在每条视频 Prompt 逐字重复角色描述；身份漂移时回到 `image-control-pass` 补 Identity 控制。
3. 花字/字幕样式也要服从风格（多巴胺=粗体圆体字+撞色描边；极简=细体无衬线+大量留白）；用户不需要花字/字幕时不额外设计。
4. 出片后对照风格合同检查关键差异，不机械堆叠词板。

### 3. 按需光影方法

画面平、主体不突出或需要光影叙事时，按 `光源位置 → 方向 → 软硬/色温 → 亮暗比 → 遮挡/投影 → 材质响应` 补齐缺失项。窗光、门缝光、灯光、反射光等必须有可理解的空间来源；动态扫光、影子移动要由主体或光源运动触发。

跨镜头记录主光方向和允许的变化，不为“电影感”给每镜强加逆光、体积光或高反差。具体资产交接见 `image-control-pass/references/midjourney-style-assets.md`。

### 4. MJ 风格资产协作（可选）

需要探索更鲜明的风格或建立风格化资产时，先经 `image-control-pass` 使用 Midjourney 产出 Style Master 与风格合同，再进入角色、场景、关键帧控制。MJ 负责风格探索，不替代身份或空间锁定；参数按当前官方支持配置，不写死版本。

## 三、QC 检查表（成片验收用）
- [ ] 光影方向与来源符合场景，亮暗层次服务主体；不是每镜都必须高反差
- [ ] 本镜需要呈现的主体材质细节可见（皮肤/食物/面料/金属）
- [ ] 景深与空间关系符合镜头目的；需要环境叙事时不强制背景虚化
- [ ] 配色符合风格锚点，不出现破坏风格的偏色
- [ ] 角色跨镜头不漂移（发型/服装/妆容一致）
- [ ] 有至少一个"记忆点画面"（可截图当封面的帧）
- [ ] 视频 Prompt 未重复资产描述、通用质量后缀和无效否定

## 四、与其他 skill 的协作
- 角色一致性 → 配合 `character-asset`
- 风格母版 / MJ 探索 → 配合 `image-control-pass`
- 单镜头执行 prompt → 配合 `shot-execution`（只注入本镜需要且未被参考图覆盖的风格/光影信息）
- 成片验收 → 配合 `video-production-qc`（本清单并入其质感维度）
