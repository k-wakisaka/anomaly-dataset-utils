# anomaly-dataset-utils

## Task flow
1. manipulate for function
2. clean floor
3. shoot & (if detail) annotate by shutter remote control & QuickTimePlayer
4. [upload](https://drive.google.com/drive/folders/1S6LWKWM84hgxveAl0s9vu40XjiaGp-Vv?usp=drive_link)
5. heic2png.py
6. annotate center point by /usr/local/bin/[labelme-Linux](https://github.com/wkentaro/labelme/releases/download/v5.2.1/labelme-Linux)
7. crop.py
8. (if anomaly)annotate anomaly polygons  by /usr/local/bin/[labelme-Linux](https://github.com/wkentaro/labelme/releases/download/v5.2.1/labelme-Linux)
9. (if anomaly)mask.py
10. [upload](https://drive.google.com/drive/folders/1WbkNND1urgiNAYOvQKoMQKCPigoG8w_L?usp=drive_link\)

## Task sheet

|component |function           |sample| angle | length | light |crop_height| crop_width | complete |
|----------|-------------------|------|-------|--------|-------|--------|-----------|--------|
|bottle    |good               |30    |       |        |       |        |           |        |
|bottle    |broken_large       |10    |       |        |       |        |           |        |
|bottle    |broken_small       |10    |       |        |       |        |           |        |
|bottle    |contamination      |10    |       |        |       |        |           |        |
|carpet    |good               |30    |       |        |       |        |           |        |
|carpet    |color              |10    |       |        |       |        |           |        |
|carpet    |cut                |10    |       |        |       |        |           |        |
|carpet    |hole               |10    |       |        |       |        |           |        |
|carpet    |metal_contamination|10    |       |        |       |        |           |        |
|carpet    |thread             |10    |       |        |       |        |           |        |
|grid      |good               |30    |       |        |       |        |           |        |
|grid      |bent               |10    |       |        |       |        |           |        |
|grid      |broken             |10    |       |        |       |        |           |        |
|grid      |glue               |10    |       |        |       |        |           |        |
|grid      |metal_contamination|10    |       |        |       |        |           |        |
|grid      |thread             |10    |       |        |       |        |           |        |
|leather   |good               |30    |       |        |       |        |           |        |
|leather   |color              |10    |       |        |       |        |           |        |
|leather   |cut                |10    |       |        |       |        |           |        |
|leather   |fold               |10    |       |        |       |        |           |        |
|leather   |glue               |10    |       |        |       |        |           |        |
|leather   |poke               |10    |       |        |       |        |           |        |
|metal_nat |good               |30    |       |        |       |        |           |        |
|metal_nat |bent               |10    |       |        |       |        |           |        |
|metal_nat |color              |10    |       |        |       |        |           |        |
|metal_nat |flip               |10    |       |        |       |        |           |        |
|metal_nat |scratch            |10    |       |        |       |        |           |        |
|screw     |good               |30    | 50    | min    | max   |        |           |        |
|screw     |manipulated_front  |10    | 50    | min    | max   |        |           |        |
|screw     |scratch_head       |10    | 50    | min    | max   |        |           |        |
|screw     |scratch_neck       |10    | 50    | min    | max   |        |           |        |
|screw     |thread_side        |10    | 50    | min    | max   |        |           |        |
|screw     |thread_top         |10    | 50    | min    | max   |        |           |        |
|tile      |crack              |10    |       |        |       |        |           |        |
|tile      |glue_strip         |10    |       |        |       |        |           |        |
|tile      |good               |30    |       |        |       |        |           |        |
|tile      |gray_stroke        |10    |       |        |       |        |           |        |
|tile      |oil                |10    |       |        |       |        |           |        |
|tile      |rough              |10    |       |        |       |        |           |        |
|toothbrush|good               |30    |       |        |       |        |           |        |
|toothbrush|defective          |10    |       |        |       |        |           |        |
|transistor|good               |30    |       |        |       |        |           |        |
|transistor|bent_lead          |10    |       |        |       |        |           |        |
|transistor|cut_lead           |10    |       |        |       |        |           |        |
|transistor|damaged_case       |10    |       |        |       |        |           |        |
|transistor|misplaced          |10    |       |        |       |        |           |        |
|wood      |good               |30    |       |        |       |        |           |        |
|wood      |color              |10    |       |        |       |        |           |        |
|wood      |combined           |10    |       |        |       |        |           |        |
|wood      |hole               |10    |       |        |       |        |           |        |
|wood      |liquid             |10    |       |        |       |        |           |        |
|wood      |scratch            |10    |       |        |       |        |           |        |
|zipper    |good               |30    |       |        |       |        |           |        |
|zipper    |broken_teeth       |10    |       |        |       |        |           |        |
|zipper    |combined           |10    |       |        |       |        |           |        |
|zipper    |fabric_border      |10    |       |        |       |        |           |        |
|zipper    |fabric_interior    |10    |       |        |       |        |           |        |
|zipper    |rough              |10    |       |        |       |        |           |        |
|zipper    |split_teeth        |10    |       |        |       |        |           |        |
|zipper    |squeezed_teeth     |10    |       |        |       |        |           |        |
|hazelnut  |good               |30    |       |        |       |        |           |        |
|hazelnut  |crack              |10    |       |        |       |        |           |        |
|hazelnut  |cut                |10    |       |        |       |        |           |        |
|hazelnut  |hole               |10    |       |        |       |        |           |        |
|hazelnut  |print              |10    |       |        |       |        |           |        |

