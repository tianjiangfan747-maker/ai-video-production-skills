# Prompt Lexicon

## Preferred

“朝画面右侧移动”“向摄影机靠近”“从后景进入前景”“沿画面左边缘离开”优于“向左/向前”。

## Camera

locked-off / dolly in / dolly out / tracking / lateral move / handheld / OTS / POV 等，只使用真正需要的一个主要行为。

## Avoid

无参照系的 left/right/forward；纯抽象情绪；重复角色资产；一长串否定词。

## 限制词：必要、具体、未覆盖才保留

保留以下限制：

- 用户明确点名，例如“不要字幕”“不要 BGM”“不要乱码或杂乱线条”。
- 已在当前生成中反复出现、且一条短约束能针对解决的问题。
- 法律、品牌、内容安全或交付规格要求的排除项。

删除或改写以下冗余：

- `no watermark, no logo` 等未被要求、也无失败证据的通用尾巴。
- 已由正面描述覆盖的内容，例如“干净、只有一杯咖啡的木桌”之后不再追加“不要杂物、不要多余物体”。
- 强参考图已经锁定的身份、服装、材质、构图和背景，不在视频 Prompt 中反复描述，再补一串“不要改变”。
- 同义堆叠，例如 `no text / no subtitles / no captions` 只需按实际需求保留一种准确说法。

不要由脚本自动删否定词。脚本发现密度高时，由人检查它是否明确、必要、未覆盖；必要约束可以保留，精简不能牺牲用户要求。

## 镜头包裹动作

把镜头与动作写成一个可读事件，而不是 `dolly + pan + orbit + handheld` 的名词集合：

`起始构图 → 主动作/触发 → 摄影机路径 → 遮挡或层次变化 → 结束构图`

需要光影时补 `来源 + 方向 + 材质响应`；动态光影要有主体或光源运动作为原因。无信息增量的前景、遮挡、体积光不添加。

## 精简示例

冗长版：

> Cinematic 4K ultra-detailed shot. The camera pushes in, pans and orbits at the same time. Keep the exact same face, hair, clothing and background as the reference. No watermark, no logo, no distortion, no clutter, no bad anatomy, no subtitles.

精简版（强参考图、用户明确要求无字幕）：

> 人物沿画面右侧走向窗边，镜头贴近右肩跟随；门框短暂遮住人物，经过后露出远处高塔；人物在窗前停步，镜头停在越肩中景。无字幕。

保留了主动作、方向、镜头路径、遮挡/揭示和结束态；删除了已被参考图覆盖的资产描述、互相竞争的运镜、同义质量词与无依据的通用否定。
