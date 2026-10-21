---
name: shot-execution
description: 把已设计好的单镜头压缩成平台中性的 AI 视频执行 Prompt，重点控制自然表演、空间方向、摄影机、时间变化和明确结束状态
type: prompt
whenToUse: 当用户要把一个已确定的镜头变成 I2V/T2V/R2V 视频生成 Prompt，或要修复单镜头的动作/摄影机/方向问题时
---

# Shot Execution

## 1. Image says what; Prompt says what happens

强参考图已经提供身份、构图、空间与视觉语言时，不重复描述。当前镜头的文字只负责变化。

Runway 当前 I2V 指南也建议主要描述 motion，并从简单 Prompt 开始、一次增加一个变量。

## 2. 内部六层

1. 起始状态 / 因果
2. 一个主行动
3. 空间方向 / motion vector
4. 一个主摄影机行为
5. 必要环境运动 / 声音
6. 结束状态

## 3. 自然表演

心理因果用于内部驱动；最终描述优先落到可观察动作。

允许停顿、犹豫、自然重心变化、反应先后。除非微动作本身传递剧情信息，不要列眉毛、鼻翼、瞳孔、喉结、手指等肌肉清单。

## 4. 空间先于修辞

双人/多人、打斗、追逐、飞行、投掷或画外目标出现时必须有参照系：screen-left/right、foreground/background、axis、camera side、eyeline、motion vector、entry/exit、action start/end。

## 5. Motion Budget

默认：**一个主动作 + 一个主摄影机行为 + 最多一个重要环境运动**。

超预算不是绝对错误，但要有原因；复杂链条优先拆镜。

## 6. 摄影机

回答：从哪里看、为什么从这里看、最后停在哪里。必要时写 `start → trigger → path → endpoint`。

## 7. 结束态

每镜必须说明人物、物体、视线和摄影机最终停在哪里，以及下一镜从什么东西接上。

## 8. 平台中性输出

先输出 neutral shot prompt，再交给平台适配层。这样同一导演决定可以映射到多个模型。

## 9. 最终压缩

Prompt 不是字段大拼盘。优先保留：动作、方向、摄影机、时序、结束态。只有参考图没有提供或本镜需要改变的视觉信息才补写。

## 参考资料

用词规范与禁忌：`${KIMI_SKILL_DIR}/references/prompt-lexicon.md`。
