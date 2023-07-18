# anomaly-dataset-utils

## Task flow
1. manipulate for function
2. clean floor
3. shoot
4. [upload](https://drive.google.com/drive/folders/1S6LWKWM84hgxveAl0s9vu40XjiaGp-Vv?usp=drive_link)
5. heic2png.py
6. annotate center point by /usr/local/bin/[labelme-Linux](https://github.com/wkentaro/labelme/releases/download/v5.2.1/labelme-Linux)
7. crop.py
8. [upload](https://drive.google.com/drive/folders/1WbkNND1urgiNAYOvQKoMQKCPigoG8w_L?usp=drive_link\)

## Task sheet

|component |function           |sample|zoom|ratio|light|crop_height|crop_width|complete|
|----------|-------------------|------|----|-----|-----|-----------|----------|--------|
|bottle    |good               |30    |3   |1x1  |max  |768        |768       |        |
|bottle    |broken_large       |20    |3   |1x1  |max  |768        |768       |        |
|bottle    |broken_small       |20    |3   |1x1  |max  |768        |768       |        |
|bottle    |contamination      |20    |3   |1x1  |max  |768        |768       |        |
|carpet    |good               |30    |    |     |     |           |          |        |
|carpet    |color              |20    |    |     |     |           |          |        |
|carpet    |cut                |20    |    |     |     |           |          |        |
|carpet    |hole               |20    |    |     |     |           |          |        |
|carpet    |metal_contamination|20    |    |     |     |           |          |        |
|carpet    |thread             |20    |    |     |     |           |          |        |
|grid      |good               |30    |    |     |     |           |          |        |
|grid      |bent               |20    |    |     |     |           |          |        |
|grid      |broken             |20    |    |     |     |           |          |        |
|grid      |glue               |20    |    |     |     |           |          |        |
|grid      |metal_contamination|20    |    |     |     |           |          |        |
|grid      |thread             |20    |    |     |     |           |          |        |
|leather   |good               |30    |    |     |     |           |          |        |
|leather   |color              |20    |    |     |     |           |          |        |
|leather   |cut                |20    |    |     |     |           |          |        |
|leather   |fold               |20    |    |     |     |           |          |        |
|leather   |glue               |20    |    |     |     |           |          |        |
|leather   |poke               |20    |    |     |     |           |          |        |
|metal_nat |good               |30    |    |     |     |           |          |        |
|metal_nat |bent               |20    |    |     |     |           |          |        |
|metal_nat |color              |20    |    |     |     |           |          |        |
|metal_nat |flip               |20    |    |     |     |           |          |        |
|metal_nat |scratch            |20    |    |     |     |           |          |        |
|screw     |good               |30    |    |     |     |           |          |        |
|screw     |manipulated_front  |20    |    |     |     |           |          |        |
|screw     |scratch_head       |20    |    |     |     |           |          |        |
|screw     |scratch_neck       |20    |    |     |     |           |          |        |
|screw     |thread_side        |20    |    |     |     |           |          |        |
|screw     |thread_top         |20    |    |     |     |           |          |        |
|tile      |crack              |20    |    |     |     |           |          |        |
|tile      |glue_strip         |20    |    |     |     |           |          |        |
|tile      |good               |30    |    |     |     |           |          |        |
|tile      |gray_stroke        |20    |    |     |     |           |          |        |
|tile      |oil                |20    |    |     |     |           |          |        |
|tile      |rough              |20    |    |     |     |           |          |        |
|toothbrush|good               |30    |    |     |     |           |          |        |
|toothbrush|defective          |20    |    |     |     |           |          |        |
|transistor|good               |30    |    |     |     |           |          |        |
|transistor|bent_lead          |20    |    |     |     |           |          |        |
|transistor|cut_lead           |20    |    |     |     |           |          |        |
|transistor|damaged_case       |20    |    |     |     |           |          |        |
|transistor|misplaced          |20    |    |     |     |           |          |        |
|wood      |good               |30    |    |     |     |           |          |        |
|wood      |color              |20    |    |     |     |           |          |        |
|wood      |combined           |20    |    |     |     |           |          |        |
|wood      |hole               |20    |    |     |     |           |          |        |
|wood      |liquid             |20    |    |     |     |           |          |        |
|wood      |scratch            |20    |    |     |     |           |          |        |
|zipper    |good               |30    |    |     |     |           |          |        |
|zipper    |broken_teeth       |20    |    |     |     |           |          |        |
|zipper    |combined           |20    |    |     |     |           |          |        |
|zipper    |fabric_border      |20    |    |     |     |           |          |        |
|zipper    |fabric_interior    |20    |    |     |     |           |          |        |
|zipper    |rough              |20    |    |     |     |           |          |        |
|zipper    |split_teeth        |20    |    |     |     |           |          |        |
|zipper    |squeezed_teeth     |20    |    |     |     |           |          |        |
|hazelnut  |good               |30    |    |     |     |           |          |        |
|hazelnut  |crack              |20    |    |     |     |           |          |        |
|hazelnut  |cut                |20    |    |     |     |           |          |        |
|hazelnut  |hole               |20    |    |     |     |           |          |        |
|hazelnut  |print              |20    |    |     |     |           |          |        |

