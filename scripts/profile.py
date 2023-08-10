import argparse
import glob
import os
from io import StringIO
import pandas as pd
from PIL import Image
import numpy as np
import json
import matplotlib.pyplot as plt
import seaborn as sns
import shutil

def convert_heatmap(image, vmin, vmax, cmap='viridis'):
    plt.figure(figsize=(5, 5))
    sns.heatmap(image, vmin=vmin, vmax=vmax, cmap=cmap, cbar=False)

    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    plt.savefig('/tmp/heatmap.png', bbox_inches='tight', pad_inches=0, dpi=100)
    plt.close()

    heatmap_img = plt.imread('/tmp/heatmap.png')
    heatmap_image = (heatmap_img * 255).astype(np.uint8)

    resize_heatmap_image = Image.fromarray(heatmap_image).resize((image.shape[1], image.shape[0]))
    return resize_heatmap_image
def prepare_heatmap(score_df, low_std_times=1, high_std_times=4):
    heatmap_dict = {}
    for _, data in score_df.iterrows():
        image_path = data['image_path']
        json_path = os.path.splitext(image_path)[0] + '.json'
        with open(json_path, 'r') as f:
            json_dict = json.load(f)
        image = np.asarray(Image.open(image_path).convert('L'))
        image = (image / 255. * (json_dict['max_raw'] - json_dict['min_raw'])) + json_dict['min_raw']
        heatmap_dict[image_path] = image
    all_image = np.stack([image for image in heatmap_dict.values()])
    mean = np.mean(all_image)
    max_value = np.max(all_image)
    high_std = np.std(all_image[all_image > mean])
    low_std = np.std(all_image[all_image < mean])

    for key in heatmap_dict.keys():
        heatmap_dict[key] = convert_heatmap(heatmap_dict[key], max(0, mean-low_std*low_std_times), min(mean+high_std*high_std_times, max_value))

    return heatmap_dict

def dump(score_df, detail_heatmap_dict, input_dataset_dir_path, output_dir_path):
    os.makedirs(output_dir_path, exist_ok=True)
    for _, data in score_df.iterrows():
        score = int(data['score'] * 10000)
        label = data['label']
        image_path = glob.glob(os.path.join(input_dataset_dir_path, f'**/{os.path.basename(data["image_path"])}'), recursive=True)[0]
        shutil.copy2(image_path, os.path.join(output_dir_path, f'{score:08d}_{label}_raw_{os.path.basename(data["image_path"])}'))
        image = Image.open(image_path).convert('RGBA')

        name, ext = os.path.splitext(os.path.basename(data["image_path"]))
        if label == 'good':
            Image.fromarray(np.zeros((image.size[1], image.size[0], 3), dtype=np.uint8)).save(os.path.join(output_dir_path, f'{score:08d}_{label}_{name}_mask{ext}'))
        else:
            mask_image_path = glob.glob(os.path.join(input_dataset_dir_path, f'**/{name}_mask{ext}'), recursive=True)[0]
            shutil.copy2(mask_image_path, os.path.join(output_dir_path, f'{score:08d}_{label}_{os.path.basename(mask_image_path)}'))

        heatmap_image = detail_heatmap_dict[data["image_path"]].resize(image.size)
        blended_image = Image.blend(image, heatmap_image, alpha=0.5)
        blended_image.save(os.path.join(output_dir_path, f'{score:08d}_{label}_inf_{os.path.basename(data["image_path"])}'))
def profile(log_path, input_dataset_dir_path, output_dir_path, delimiter='---'):
    with open(log_path, 'r') as f:
        data = f.read()
    category = os.path.basename(log_path).split('_')[0]
    detail_by_max_score_df = pd.read_csv(StringIO(data.split(delimiter)[1]), skiprows=2, skipinitialspace=True)
    detail_by_mean_score_df = pd.read_csv(StringIO(data.split(delimiter)[3]), skiprows=2, skipinitialspace=True)
    detail_heatmap_dict = prepare_heatmap(detail_by_max_score_df)

    sub_output_dir_path = os.path.join(output_dir_path, category, 'mean_score')
    dump(detail_by_mean_score_df, detail_heatmap_dict, input_dataset_dir_path, sub_output_dir_path)

    sub_output_dir_path = os.path.join(output_dir_path, category, 'max_score')
    dump(detail_by_max_score_df, detail_heatmap_dict, input_dataset_dir_path, sub_output_dir_path)
def main(input_log_dir_path, input_dataset_dir_path, output_dir_path):
    log_path_list = sorted(glob.glob(os.path.join(input_log_dir_path, '*.log')))
    for log_path in log_path_list:
        profile(log_path, input_dataset_dir_path, output_dir_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='main')
    parser.add_argument('--input_log_dir_path', type=str, default='~/Desktop/anomaly.v.0.0.1_experiment_log')
    parser.add_argument('--input_dataset_dir_path', type=str, default='~/Desktop/anomaly.v.0.0.1')
    parser.add_argument('--output_dir_path', type=str, default='~/Desktop/anomaly.v.0.0.1_experiment_profile')

    args = parser.parse_args()

    args.input_log_dir_path = os.path.expanduser(args.input_log_dir_path)
    args.input_dataset_dir_path = os.path.expanduser(args.input_dataset_dir_path)
    args.output_dir_path = os.path.expanduser(args.output_dir_path)

    main(**args.__dict__)