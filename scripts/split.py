import os
import argparse
import glob
import tqdm
import shutil
import random
def split(input_sub_dataset_path, output_dir_path, good_test_sample=10):
    random.seed(777)
    good_sub_dataset_category_path = os.path.join(input_sub_dataset_path, 'good')
    anomaly_sub_dataset_category_path_list = [dir_path for dir_path in glob.glob(os.path.join(input_sub_dataset_path, '*')) if dir_path != good_sub_dataset_category_path]

    # good
    good_image_path_list = glob.glob(os.path.join(good_sub_dataset_category_path, '*.png'))
    random.shuffle(good_image_path_list)
    train_good_image_path_list, test_good_image_path_list = good_image_path_list[good_test_sample:], good_image_path_list[:good_test_sample]
    output_good_train_dir_path = os.path.join(output_dir_path, 'train', 'good')
    os.makedirs(output_good_train_dir_path, exist_ok=True)
    [shutil.copy2(train_good_image_path, os.path.join(output_good_train_dir_path, os.path.basename(train_good_image_path))) for train_good_image_path in train_good_image_path_list]
    output_good_test_dir_path = os.path.join(output_dir_path, 'test', 'good')
    os.makedirs(output_good_test_dir_path, exist_ok=True)
    [shutil.copy2(test_good_image_path, os.path.join(output_good_test_dir_path, os.path.basename(test_good_image_path))) for test_good_image_path in test_good_image_path_list]

    # anomaly
    for anomaly_sub_dataset_category_path in anomaly_sub_dataset_category_path_list:
        # test
        anomaly_image_path_list = [image_path for image_path in glob.glob(os.path.join(anomaly_sub_dataset_category_path, '*.png')) if '_mask' not in image_path]
        output_anomaly_test_dir_path = os.path.join(output_dir_path, 'test', anomaly_sub_dataset_category_path.split('/')[-1])
        os.makedirs(output_anomaly_test_dir_path, exist_ok=True)
        [shutil.copy2(anomaly_image_path, os.path.join(output_anomaly_test_dir_path, os.path.basename(anomaly_image_path))) for anomaly_image_path in anomaly_image_path_list]
        # ground_truth
        anomaly_mask_path_list = [image_path.replace('.png', '_mask.png') for image_path in anomaly_image_path_list]
        output_anomaly_mask_dir_path = os.path.join(output_dir_path, 'ground_truth', anomaly_sub_dataset_category_path.split('/')[-1])
        os.makedirs(output_anomaly_mask_dir_path, exist_ok=True)
        [shutil.copy2(anomaly_mask_path, os.path.join(output_anomaly_mask_dir_path, os.path.basename(anomaly_mask_path))) for anomaly_mask_path in anomaly_mask_path_list]

def main(input_dir_path, output_dir_path):
    os.makedirs(output_dir_path, exist_ok=True)
    sub_dataset_path_list = glob.glob(os.path.join(input_dir_path, '*'), recursive=True)
    for sub_dataset_path in tqdm.tqdm(sub_dataset_path_list, desc='main'):
        split(sub_dataset_path, os.path.join(output_dir_path, sub_dataset_path.split('/')[-1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='main')
    parser.add_argument('--input_dir_path', type=str, default='~/Desktop/dataset')
    parser.add_argument('--output_dir_path', type=str, default='~/Desktop/anomaly.v.0.0.3')

    args = parser.parse_args()

    args.input_dir_path = os.path.expanduser(args.input_dir_path)
    args.output_dir_path = os.path.expanduser(args.output_dir_path)

    main(**args.__dict__)
