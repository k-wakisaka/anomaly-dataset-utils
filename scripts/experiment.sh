#!/bin/bash

echo "./experiment.sh {dataset_path} {output_dir_path} {input_image_height} {input_image_width} {preprocessing_dim} {aggregate_dims} {percentage} {number_of_starting_points} {dimension_to_project_features_to}"

# cd
this_repo_dir_path=$(pwd)
patchcore_repo_dir_path="${HOME}/GitHub/patchcore-demo/"
cd ${patchcore_repo_dir_path}

# build image
docker build -t vaik-patchcore-demo-image -f ./cpu.Dockerfile .

# get category path list
category_path_list=($(find "$1" -maxdepth 1 -mindepth 1 -type d))

# experiment
for category_path in "${category_path_list[@]}"; do
    category=$(basename "${category_path}")
    # train
    docker run --name vaik-patchcore-demo-container \
               --rm \
               --gpus all \
               --entrypoint python3 \
               -v $(pwd):/opt/project \
               -w /opt/project \
               -v /tmp/output/${category}/model:/tmp/output/${category}/model \
               -v ${category_path}/train/good:/tmp/dataset/${category}/train/good \
               -it vaik-patchcore-demo-image \
               train.py \
               --train_good_image_dir_path /tmp/dataset/${category}/train/good \
               --input_image_height $3 \
               --input_image_width $4 \
               --preprocessing_dim $5 \
               --aggregate_dims $6 \
               --percentage $7 \
               --number_of_starting_points $8 \
               --dimension_to_project_features_to $9 \
               --output_model_dir_path /tmp/output/${category}/model

    # inference
    docker run --name vaik-patchcore-demo-container \
               --rm \
               --gpus all \
               --entrypoint python3 \
               -v $(pwd):/opt/project \
               -w /opt/project \
               -v /tmp/output/${category}/model:/tmp/output/${category}/model \
               -v /tmp/output/${category}/dataset_inf:/tmp/output/${category}/dataset_inf \
               -v ${category_path}/test:/tmp/dataset/${category}/test \
               -it vaik-patchcore-demo-image \
               inference.py \
               --input_faiss_path /tmp/output/${category}/model/model.faiss \
               --input_json_path /tmp/output/${category}/model/model.json \
               --test_image_dir_path /tmp/dataset/${category}/test \
               --output_dir_path /tmp/output/${category}/dataset_inf

    # experiment
    mkdir -p $2
    docker run --name vaik-patchcore-demo-container \
               --rm \
               --gpus all \
               --entrypoint python3 \
               -v $(pwd):/opt/project \
               -w /opt/project \
               -v /tmp/output/${category}/dataset_inf:/tmp/output/${category}/dataset_inf \
               -v ${category_path}/ground_truth:/tmp/dataset/${category}/ground_truth \
               -it vaik-patchcore-demo-image \
               experiment.py \
               --inference_output_dir_path /tmp/output/${category}/dataset_inf \
               --mask_image_dir_path /tmp/dataset/${category}/ground_truth > $2/${category}_experiment.log
done

cd ${this_repo_dir_path}
python parse_log.py $2 $2/log.csv
