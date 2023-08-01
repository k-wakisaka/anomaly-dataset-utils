# anomaly-dataset-utils

## Task flow

- manipulate for function
- tighten the screw
- clean floorcenter shoot & QuickTimePlayer
- [upload](https://drive.google.com/drive/folders/1S6LWKWM84hgxveAl0s9vu40XjiaGp-Vv?usp=drive_link)
- heic2png.py
- annotate center point by
  /usr/local/bin/[labelme-Linux](https://github.com/wkentaro/labelme/releases/download/v5.2.1/labelme-Linux)
- crop.py
- (if anomaly)annotate anomaly polygons by
  /usr/local/bin/[labelme-Linux](https://github.com/wkentaro/labelme/releases/download/v5.2.1/labelme-Linux)
- (if anomaly)mask.py
- [upload](https://drive.google.com/drive/folders/1WbkNND1urgiNAYOvQKoMQKCPigoG8w_L?usp=drive_link\)

## Task sheet

| component  | function            | sample | light | crop_height | crop_width | complete |
|------------|---------------------|--------|-------|------------|------------|----------|
| bottle     | good                | 30     |       |            |            |          |
| bottle     | broken_large        | 10     |       |            |            |          |
| bottle     | broken_small        | 10     |       |            |            |          |
| bottle     | contamination       | 10     |       |            |            |          |
| carpet     | good                | 30     |       | 2048       | 2048　      |          |
| carpet     | color               | 10     |       | 2048       | 2048       |          |
| carpet     | cut                 | 10     |       | 2048       | 2048       |          |
| carpet     | hole                | 10     |       | 2048    　  | 2048       |          |
| carpet     | metal_contamination | 10     |       | 2048       | 2048　      |          |
| carpet     | thread              | 10     |       | 2048       | 2048       |          |
| grid       | good                | 30     |       |            |            |          |
| grid       | bent                | 10     |       |            |            |          |
| grid       | broken              | 10     |       |            |            |          |
| grid       | glue                | 10     |       |            |            |          |
| grid       | metal_contamination | 10     |       |            |            |          |
| grid       | thread              | 10     |       |            |            |          |
| leather    | good                | 30     |       |            |            |          |
| leather    | color               | 10     |       |            |            |          |
| leather    | cut                 | 10     |       |            |            |          |
| leather    | fold                | 10     |       |            |            |          |
| leather    | glue                | 10     |       |            |            |          |
| leather    | poke                | 10     |       |            |            |          |
| metal_nat  | good                | 40     | max   | 1024       | 1024       | x        |
| metal_nat  | bent                | 10     | max   | 1024       | 1024       | x        |
| metal_nat  | color               | 10     | max   | 1024       | 1024       | x        |
| metal_nat  | flip                | 10     | max   | 1024       | 1024       | x        |
| metal_nat  | scratch             | 10     | max   | 1024       | 1024       | x        |
| screw      | good                | 36     | max   | 1408       | 1408       | x        |
| screw      | manipulated_front   | 10     | max   | 1408       | 1408       | x        |
| screw      | scratch_head        | 10     | max   | 1408       | 1408       | x        |
| screw      | scratch_neck        | 10     | max   | 1408       | 1408       | x        |
| screw      | thread_side         | 10     | max   | 1408       | 1408       | x        |
| screw      | thread_top          | 10     | max   | 1408       | 1408       | ~        |
| tile       | crack               | 10     |       |            |            |          |
| tile       | glue_strip          | 10     |       |            |            |          |
| tile       | good                | 30     |       |            |            |          |
| tile       | gray_stroke         | 10     |       |            |            |          |
| tile       | oil                 | 10     |       |            |            |          |
| tile       | rough               | 10     |       |            |            |          |
| toothbrush | good                | 40     | max   | 832        | 576        | x        |
| toothbrush | defective           | 40     | max   | 832        | 576        | x        |
| transistor | good                | 34     | max   | 1280       | 1280       | x        |
| transistor | bent_lead           | 10     | max   | 1280       | 1280       | x        |
| transistor | cut_lead            | 10     | max   | 1280       | 1280       | x        |
| transistor | damaged_case        | 10     | max   | 1280       | 1280       | x        |
| transistor | misplaced           | 10     | max   | 1280       | 1280       | ~        |
| wood       | good                | 30     |       |            |            |          |
| wood       | color               | 10     |       |            |            |          |
| wood       | combined            | 10     |       |            |            |          |
| wood       | hole                | 10     |       |            |            |          |
| wood       | liquid              | 10     |       |            |            |          |
| wood       | scratch             | 10     |       |            |            |          |
| zipper     | good                | 30     | max   | 2048       | 1536       | x        |
| zipper     | broken_teeth        | 10     | max   | 2048       | 1536       | x        |
| zipper     | combined            | 10     | max   | 2048       | 1536       | ~　       |
| zipper     | fabric_border       | 10     | max   | 2048       | 1536       | ~　       |
| zipper     | fabric_interior     | 10     | max   | 2048       | 1536       | x        |
| zipper     | rough               | 10     | max   | 2048       | 1536       | ~　       |
| zipper     | split_teeth         | 10     | max   | 2048       | 1536       | x        |
| zipper     | squeezed_teeth      | 10     | max   | 2048       | 1536       | ~        |
| hazelnut   | good                | 50     | max   | 1536       | 1536       | x        |
| hazelnut   | crack               | 10     | max   | 1536       | 1536       | x        |
| hazelnut   | cut                 | 10     | max   | 1536       | 1536       | x        |
| hazelnut   | hole                | 10     | max   | 1536       | 1536       | x        |
| hazelnut   | color               | 10     | max   | 1536       | 1536       | x        |
