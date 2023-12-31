# anomaly-dataset-utils

--------

## Prepare datste

### Task flow

#### Prepare sub dataset
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

#### Split
- split.py

#### Task sheet

| component | function  | sample | light | crop_height | crop_width | complete |
|-----------|-----------|-------|-------|-------------|-----------|----------|
| kabayaki1 | good      | 50    | max   | 3072        | 1536      | x        |
| kabayaki1 | cut       | 10    | max   | 3072        | 1536      | x        |
| kabayaki1 | hole      | 10    | max   | 3072        | 1536      | x        |
| kabayaki1 | glue      | 10    | max   | 3072        | 1536      | x        |
| kabayaki1 | color     | 10    | max   | 3072        | 1536      | x        |
| kabayaki2 | good      | 50    | max   | 3072        | 1536      | x        |
| kabayaki2 | cut       | 10    | max   | 3072        | 1536      | x        |
| kabayaki2 | hole      | 10    | max   | 3072        | 1536      | x        |
| kabayaki2 | glue      | 10    | max   | 3072        | 1536      | x        |
| kabayaki2 | color     | 10    | max   | 3072        | 1536      | x        |
| karpas1   | good      | 50    | max   | 1024        | 2816      | x        | 
| karpas1   | cut       | 10    | max   | 1024        | 2816      | x        |
| karpas1   | hole      | 10    | max   | 1024        | 2816      | x        |
| karpas1   | protrude  | 10    | max   | 1024        | 2816      | x        |
| karpas1   | color     | 10    | max   | 1024        | 2816      | x        |
| karpas2   | good      | 50    | max   | 1024        | 2816      | x        | 
| karpas2   | cut       | 10    | max   | 1024        | 2816      | x        |
| karpas2   | hole      | 10    | max   | 1024        | 2816      | x        |
| karpas2   | protrude  | 10    | max   | 1024        | 2816      | x        |
| karpas2   | color     | 10    | max   | 1024        | 2816      | x        |
| felix1    | good      | 50    | max   | 1536        | 2304      | x        |4
| felix1    | cut       | 10    | max   | 1536        | 2304      |          |
| felix1    | hole      | 10    | max   | 1536        | 2304      |          |
| felix1    | protrude  | 10    | max   | 1536        | 2304      |          |
| felix1    | oil       | 10    | max   | 1536        | 2304      |          |
| felix1    | color     | 10    | max   | 1536        | 2304      |          |
| felix2    | good      | 50    | max   | 1536        | 2304      | x        |4
| felix2    | cut       | 10    | max   | 1536        | 2304      |          |
| felix2    | hole      | 10    | max   | 1536        | 2304      |          |
| felix2    | protrude  | 10    | max   | 1536        | 2304      |          |
| felix2    | oil       | 10    | max   | 1536        | 2304      |          |
| felix2    | color     | 10    | max   | 1536        | 2304      |          |
| umai1     | good      | 50    | max   | 2560        | 2560      |          |
| umai1     | cut       | 10    | max   | 2560        | 2560      |          |
| umai1     | hole      | 10    | max   | 2560        | 2560      |          |
| umai1     | glue      | 10    | max   | 2560        | 2560      |          |
| umai1     | different | 10    | max   | 2560        | 2560      |          |
| umai1     | color     | 10    | max   | 2560        | 2560      |          |
| umai2     | good      | 50    | max   | 2560        | 2560      |          |
| umai2     | cut       | 10    | max   | 2560        | 2560      |          |
| umai2     | hole      | 10    | max   | 2560        | 2560      |          |
| umai2     | glue      | 10    | max   | 2560        | 2560      |          |
| umai2     | different | 10    | max   | 2560        | 2560      |          |
| umai2     | color     | 10    | max   | 2560        | 2560      |          |
| gum       | good      | 50    | max   | 2560        | 2560      |          |
| gum       | cut       | 10    | max   | 2560        | 2560      |          |
| gum       | hole      | 10    | max   | 2560        | 2560      |          |
| gum       | clack     | 10    | max   | 2560        | 2560      |          |
| gum       | thread    | 10    | max   | 2560        | 2560      |          |
| gum       | liquid    | 10    | max   | 2560        | 2560      |          |
| caramel   | good      | 50    | max   | 2560        | 2560      |          |
| caramel   | cut       | 10    | max   | 2560        | 2560      |          |
| caramel   | hole      | 10    | max   | 2560        | 2560      |          |
| caramel   | bent      | 10    | max   | 2560        | 2560      |          |
| caramel   | thread    | 10    | max   | 2560        | 2560      |          |
| caramel   | liquid    | 10    | max   | 2560        | 2560      |          |


| component    | function            | sample | light   | crop_height | crop_width | complete |
| ------------ |---------------------|--------|---------|--------|------------|----------|
| bottle       | good                | 30     |         | 2560   | 2560       | x        |
| bottle       | broken_large        | 10     |         | 2560   | 2560       | x        |
| bottle       | broken_small        | 10     |         | 2560    | 2560       | x        |
| bottle       | contamination       | 10     |         | 2560       | 2560       | x        |
| carpet       | good                | 36     |         | 2048   | 2048　      | x        |
| carpet       | color               | 10     |         | 2048   | 2048       | x        |
| carpet       | cut                 | 10     |         | 2048   | 2048       | x        |
| carpet       | hole                | 10     |         | 2048    　 | 2048       | x        |
| carpet       | metal_contamination | 10     |         | 2048   | 2048　      | ~        |
| carpet       | thread              | 10     |         | 2048   | 2048       | x        |
| grid         | good                | 30     |         | 1408  　 | 1408　      | x        |
| grid         | bent                | 10     |         | 1408   | 1408       | x        |
| grid         | broken              | 10     |         | 1408   | 1408       | x        |
| grid         | glue                | 10     |         | 1408   | 1408       | x        |
| grid         | metal_contamination | 10     |         | 1408   | 1408       | ~        |
| grid         | thread              | 10     |         | 1408   | 1408       | x        |
| leather      | good                | 30     | max     | 1408   | 1408       | x        |
| leather      | color               | 10     | max     | 1408   | 1408       | x        |
| leather      | cut                 | 10     | max     | 1408　  | 1408       | x　       |
| leather      | fold                | 10     | max     | 1408   | 1408       | x        |
| leather      | glue                | 10     | max　    | 1408   | 1408       | x        |
| leather      | poke                | 10     | max     | 1408   | 1408　      | x        |
| metal_nat    | good                | 40     | max     | 1024   | 1024       | x        |
| metal_nat    | bent                | 10     | max     | 1024   | 1024       | x        |
| metal_nat    | color               | 10     | max     | 1024   | 1024       | x        |
| metal_nat    | flip                | 10     | max     | 1024   | 1024       | x        |
| metal_nat    | scratch             | 10     | max     | 1024   | 1024       | x        |
| screw        | good                | 36     | max     | 2240   | 2240       | x        |
| screw        | manipulated_front   | 10     | max     | 2240   | 2240       | x        |
| screw        | scratch_head        | 10     | max     | 2240   | 2240       | x        |
| screw        | scratch_neck        | 10     | max     | 2240   | 2240       | x        |
| screw        | thread_side         | 10     | max     | 2240   | 2240       | x        |
| screw        | thread_top          | 10     | max     | 2240   | 2240       | ~        |
| tile         | crack               | 10     | max     | 1408   | 1408       | x        |
| tile         | glue_strip          | 10     | max     | 1408   | 1408       | x        |
| tile         | good                | 30     | max     | 1408   | 1408       | x        |
| tile         | gray_stroke         | 10     | max     | 1408   | 1408       | x        |
| tile         | oil                 | 10     | max     | 1408   | 1408       | x        |
| tile         | rough               | 10     | max     | 1408   | 1408       | x        |
| toothbrush   | good                | 40     | max     | 832    | 576        | x        |
| toothbrush   | defective           | 40     | max     | 832    | 576        | x        |
| transistor   | good                | 34     | max     | 1280   | 1280       | x        |
| transistor   | bent_lead           | 10     | max     | 1280   | 1280       | x        |
| transistor   | cut_lead            | 10     | max     | 1280   | 1280       | x        |
| transistor   | damaged_case        | 10     | max     | 1280   | 1280       | x        |
| transistor   | misplaced           | 10     | max     | 1280   | 1280       | ~        |
| wood         | good                | 30     | max     | 1280   | 1280       | x        |
| wood         | color               | 10     | max     | 1280   | 1280       | x        |
| wood         | combined            | 10     | max     | 1280   | 1280       | ~        |
| wood         | hole                | 10     | max     | 1280   | 1280       | x        |
| wood         | liquid              | 10     | max     | 1280   | 1280       | x        |
| wood         | scratch             | 10     | max     | 1280   | 1280       | x        |
| zipper       | good                | 30     | max     | 2048   | 1536       | x        |
| zipper       | broken_teeth        | 10     | max     | 2048   | 1536       | x        |
| zipper       | combined            | 10     | max     | 2048   | 1536       | ~　       |
| zipper       | fabric_border       | 10     | max     | 2048   | 1536       | ~　       |
| zipper       | fabric_interior     | 10     | max     | 2048   | 1536       | x        |
| zipper       | rough               | 10     | max     | 2048   | 1536       | ~　       |
| zipper       | split_teeth         | 10     | max     | 2048   | 1536       | x        |
| zipper       | squeezed_teeth      | 10     | max     | 2048   | 1536       | ~        |
| hazelnut     | good                | 50     | max     | 1536   | 1536       | x        |
| hazelnut     | crack               | 10     | max     | 1536   | 1536       | x        |
| hazelnut     | cut                 | 10     | max     | 1536   | 1536       | x        |
| hazelnut     | hole                | 10     | max     | 1536   | 1536       | x        |
| hazelnut     | color               | 10     | max     | 1536   | 1536       | x        |

---------------

## Experiment
- clone [patchcore-demo](https://github.com/k-wakisaka/patchcore-demo)
- run experiment.sh

```shell
# ./experiment.sh {dataset_path} {output_dir_path} {input_image_height} {input_image_width} {preprocessing_dim} {aggregate_dims} {percentage} {number_of_starting_points} {dimension_to_project_features_to}
cd scripts
./experiment.sh ${HOME}/Desktop/ws/experiment/anomaly_experiment.v.1 ${HOME}/Desktop/ws/experiment/anomaly_experiment.v.1_log 288 288 1024 1024 0.1 10 128
```

- run profile.py
