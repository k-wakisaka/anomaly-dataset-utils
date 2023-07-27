import os
import argparse
import glob
import json
import tqdm
from PIL import Image
import numpy as np
from labelme.utils import shape
def convert_mask(png_path, json_path, mask_path):
    # read png
    image_array = np.array(Image.open(png_path))
    # read json
    canvas_mask_image_array = np.zeros(image_array.shape[:2], dtype=np.bool_)
    with open(json_path, 'r') as f:
        json_dict = json.load(f)
        for sub_json_dict in json_dict['shapes']:
            points = sub_json_dict['points']
            mask_image_array = shape.shape_to_mask(image_array.shape, points)
            canvas_mask_image_array = np.logical_or(canvas_mask_image_array, mask_image_array)

    # output
    mask_image = Image.fromarray((canvas_mask_image_array * 255).astype(np.uint8))
    mask_image.save(mask_path)
def main(input_dir_path, output_dir_path):
    os.makedirs(output_dir_path, exist_ok=True)
    png_path_list = glob.glob(os.path.join(input_dir_path, '**/*.png'), recursive=True)
    for png_path in tqdm.tqdm(png_path_list, desc='main'):
        json_path = f'{os.path.splitext(png_path)[0]}.json'
        mask_path = os.path.join(output_dir_path, f'{os.path.splitext(os.path.basename(png_path))[0]}_mask.png')
        convert_mask(png_path, json_path, mask_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='main')
    parser.add_argument('--input_dir_path', type=str, default='~/Desktop/crop_png')
    parser.add_argument('--output_dir_path', type=str, default='~/Desktop/anomaly_png')

    args = parser.parse_args()

    args.input_dir_path = os.path.expanduser(args.input_dir_path)
    args.output_dir_path = os.path.expanduser(args.output_dir_path)

    main(**args.__dict__)
