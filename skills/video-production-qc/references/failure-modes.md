# Failure Modes

## F1 Identity drift

症状：脸、发际线、体型、服装核心结构漂移。
首选：回到 character-asset / reference-first。

## F2 Spatial error

症状：左右反转、越轴、人物互看方向错误、飞行/奔跑方向错。
首选：回到 storyboard + axis + blocking。

## F3 Action failure

症状：主动作没完成、动作跳跃、多人动作纠缠。
首选：降低 motion budget、拆镜、重做 keyframe。

## F4 Camera failure

症状：镜头乱晃、摄影机完成了错误路径、焦点漂移。
首选：减少主摄影机行为数量，明确终点。

## F5 Reference conflict

症状：多张参考图互相争抢（身份、空间、风格打架），输出谁也不像。
首选：显式指定主参考，明确每张参考图的职责，减少同时生效的参考数量。

## F6 Handoff failure

症状：单镜头都好，但切在一起像 PPT。
首选：动作/视线/屏幕方向/遮挡/声音桥重新设计。

## F7 Style/lighting drift

症状：色调、光向、材质语言跨镜头漂移，同一场戏不像同一个世界。
首选：回到风格母板与场景光线合同；查 state ledger 是否有未记录的光线/时间变化。

## F8 Platform capability mismatch

症状：平台当前版本不支持所要求的控制（时长、参考数量、首尾帧、音频、分辨率）。
首选：核对当前平台能力，调整控制策略或更换平台；不把平台参数当作永久事实。

## F9 Edit/sound bridge failure

症状：剪辑点跳戏、音画桥断裂、节奏塌。
首选：交给 edit-assembly 重新设计剪辑边界与声音桥，而不是重抽镜头。
