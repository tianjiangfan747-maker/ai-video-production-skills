# Continuity Bible

这是项目的状态存储，不是普通说明文档。只保留会在后续镜头中被读取、被复制到 Prompt、或被 QC 检查的问题。

## Character

`character_id / identity_anchors / wardrobe_state / hair_state / body_state / prop_state / injury_state`

## Location

`location_id / geography / anchor_objects / entry_exit / camera_zones / axis / light_direction / time / weather`

## Prop

`prop_id / design_anchor / screen_position / owner / state / damage / interaction_state`

## Shot

`shot_id / start_state / action_start / action_end / end_state / screen_position / motion_vector / eyeline / camera_position / camera_end / handoff_in / handoff_out / chosen_take`

## State change ledger

任何会跨镜头留下痕迹的变化都要记录：湿、脏、破损、血迹、道具损耗、光线变化、时间变化、人物距离变化。

## 规则

Canonical identity 与 variable state 分离；不要为了状态变化重新定义角色或场景主资产。
