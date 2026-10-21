# Veo / Runway 适配层

## 共同原则

保留：subject action / camera motion / environmental motion / timing / direction。

当输入图已经定义主体、构图、光线和风格时，视频文字重点写运动；从简单版本开始逐项增加控制变量。Runway 当前 I2V 指南明确建议主要描述 motion，并逐项迭代；Veo 官方提示指南强调 framing/camera motion、style、lighting 等维度。（来源：Runway Gen-4 Prompting Guide，help.runwayml.com；Google Veo Prompt Guide，deepmind.google/models/veo/prompt-guide）

## 差异

不要把某一平台的 Prompt 习惯直接当成所有平台的通用语法。适配层只负责翻译。
