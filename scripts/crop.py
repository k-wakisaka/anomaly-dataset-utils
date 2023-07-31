import os
import argparse
import glob
import json
import tqdm
from PIL import Image
import numpy as np
def convert_crop(png_path, json_path, height, width, png_crop_path):
    # read png
    image_array = np.array(Image.open(png_path))
    # read json
    with open(json_path, 'r') as f:
        json_dict = json.load(f)
        center_x, center_y = int(json_dict['shapes'][0]['points'][0][0]), int(json_dict['shapes'][0]['points'][0][1])
    # crop
    start_y, end_y = max(0, center_y-height//2), min(image_array.shape[0], center_y+height//2)
    start_x, end_x = max(0, center_x-width//2), min(image_array.shape[1], center_x+width//2)

    crop_height, crop_width = end_y - start_y, end_x - start_x
    diff_height, diff_width = height - crop_height, width - crop_width
    if diff_height > 0:
        if start_y == 0:
            end_y = end_y + diff_height
        if end_y == 0:
            start_y = start_y + diff_height
    if diff_width > 0:
        if start_x == 0:
            end_x = end_x + diff_width
        if end_x == 0:
            start_x = start_x + diff_width

    crop_image_array = image_array[start_y:end_y, start_x:end_x, :]

    # output
    crop_image = Image.fromarray(crop_image_array)
    crop_image.save(png_crop_path)
def main(input_dir_path, height, width, output_dir_path):
    os.makedirs(output_dir_path, exist_ok=True)
    png_path_list = glob.glob(os.path.join(input_dir_path, '**/*.png'), recursive=True)
    for png_path in tqdm.tqdm(png_path_list, desc='main'):
        json_path = f'{os.path.splitext(png_path)[0]}.json'
        png_crop_path = os.path.join(output_dir_path, os.path.basename(png_path))
        convert_crop(png_path, json_path, height, width, png_crop_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='main')
    parser.add_argument('--input_dir_path', type=str, default='~/Desktop/org_png')
    parser.add_argument('--height', type=int, default=768)
    parser.add_argument('--width', type=int, default=768)
    parser.add_argument('--output_dir_path', type=str, default='~/Desktop/crop_png')

    args = parser.parse_args()

    args.input_dir_path = os.path.expanduser(args.input_dir_path)
    args.output_dir_path = os.path.expanduser(args.output_dir_path)

    main(**args.__dict__)
