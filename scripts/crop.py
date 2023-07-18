import os
import argparse
import glob
import json
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
    crop_image_array = image_array[max(0, center_y-height//2):min(image_array.shape[0], center_y+height//2),
                 max(0, center_x-width//2):min(image_array.shape[1], center_x+width//2),
                 :]
    # output
    crop_image = Image.fromarray(crop_image_array)
    crop_image.save(png_crop_path)
def main(input_dir_path, height, width, output_dir_path):
    os.makedirs(output_dir_path, exist_ok=True)
    png_path_list = glob.glob(os.path.join(input_dir_path, '**/*.png'), recursive=True)
    for png_path in png_path_list:
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
