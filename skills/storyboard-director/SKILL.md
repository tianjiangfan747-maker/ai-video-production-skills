---
name: storyboard-director
description: 把剧本/场景转成节拍、blocking、coverage、镜头卡、关键帧与极简动作构图控制图，并管理连续性；需要把高光帧抽象成动作、机位、构图或景深参考图时使用
type: prompt
whenToUse: 当用户问这场戏怎么拍、做分镜/镜头表/预演、人物如何走位、镜头如何覆盖或保持方向，或要把关键帧/高光图转成控制图、动作参考图、构图参考图时
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

用户需要控制图时，把关键帧或高光图抽象成动作、机位、构图与空间参考，不重画身份和材质。默认使用纯白底、极少量统一线宽的灰色简线，不使用色块或精细线稿。

室内必须检查汇聚透视、前中后景、近大远小和前后遮挡；室外与高空用原有地平线、主体间距和相对大小控制深度，不发明建筑或地面。每镜输出一条可独立复制的提示词，具体合同与模板见 `references/motion-composition-control.md`。

## 8. 输出边界

这里输出“怎么拍”、镜头卡、关键帧与控制图提示词；不在这里写超长平台视频 Prompt。进入 `shot-execution` 后再做视频 Prompt 编译，控制图负责空间与动作，文字只补充变化和结束态。

## 参考资料

按需读取：

- `${KIMI_SKILL_DIR}/references/cinematic-language.md`：轴线、30°、镜头可读性。
- `${KIMI_SKILL_DIR}/references/handoff-matrix.md`：相邻镜头接力矩阵模板。
- `${KIMI_SKILL_DIR}/references/motion-composition-control.md`：极简控制图的线条合同、室内透视、室外景深、提示词模板与验收。
