---
name: storyboard-director
description: 把剧本/场景转成节拍、blocking、coverage、镜头卡、关键帧与极简动作构图控制图，并管理连续性；支持动作机位提取、按需景深、补镜垫图和外部图片构图抽象
type: prompt
whenToUse: 当用户问这场戏怎么拍、做分镜/镜头表/预演、人物如何走位或保持方向，或要把关键帧/高光图/外部图片转成控制图、动作参考图、构图参考图，或用干净控制图补镜、补视频时
---

# Storyboard Director

## 核心顺序

**故事功能 → Beat → Blocking → 摄影机 → Coverage → Continuity → Keyframe/Control/Handoff**

## 1. Beat Map

每拍回答：发生什么、角色状态、压力如何变化、观众需要知道什么、这一拍的叙事目的。

## 2. Blocking before framing

先确定：`start → movement → interaction → end`，再决定机位和镜头尺寸。

## 3. 空间连续性

涉及多人或方向性运动时锁：`axis / camera_side / screen_position / eyeline / motion_vector / entry / exit / action_start / action_end`。

30° 是避免 stutter 的可选工具，不是死规定；如果镜头有明确叙事理由，可以违背，但必须知道为什么。

## 4. Coverage

选择 master / two-shot / single / OTS / POV / reaction / insert / cutaway 等真正提供信息的镜头。没有新增信息的镜头删除。

## 5. Shot Card 最低字段

`shot_id / purpose / duration / size / lens_feel / camera / blocking / action_start / action_end / character_state / eyeline / continuity_in / continuity_out / keyframe / control_reference / risk / fallback`

## 6. Handoff Matrix

相邻镜头至少交接一种：动作、视线、屏幕方向、进出画、前景遮挡、构图形状、道具状态、空间入口、光线或声音。

默认追求**可剪辑连续性**，而非强求 AI 生成器做像素级无缝。

## 7. 关键帧与极简控制图

关键帧负责“把下一阶段要看到的起点/关键动作/结束态画出来”。生产板的文字元数据应由确定性排版生成，而不是依赖图像模型画字。

控制图是按需减少信息干扰的视觉参考，不是固定的景深模板。默认只保留本次所需的动作、姿势、机位、主体位置和关键道具，使用纯白底与极少量统一灰色简线，不使用色块或精细线稿。

只有前中后景、透视、出入口、遮挡或尺度关系影响镜头时才加入环境：室内可用汇聚线、近大远小和必要出口；室外背景无用或干扰时可全部省略。控制图也可用于补镜、补视频的干净垫图，或从用户提供的其他图片中提取站位、机位、构图与冲击方向；最终视频不得继承白底、灰线和抽象人形。

每镜按用途输出一条可独立复制的提示词，具体选择规则与模板见 `references/motion-composition-control.md`。

## 8. 输出边界

这里输出“怎么拍”、镜头卡、关键帧与控制图提示词；不在这里写超长平台视频 Prompt。进入 `shot-execution` 后再做视频 Prompt 编译，控制图只负责用户指定的信息，文字补充变化、视觉资产和结束态。

## 参考资料

按需读取：

- `${KIMI_SKILL_DIR}/references/cinematic-language.md`：轴线、30°、镜头可读性。
- `${KIMI_SKILL_DIR}/references/handoff-matrix.md`：相邻镜头接力矩阵模板。
- `${KIMI_SKILL_DIR}/references/motion-composition-control.md`：控制图用途选择、可选景深、补镜垫图、外部构图提取、提示词模板与验收。
