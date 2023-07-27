import os
import argparse
import glob
from PIL import Image
import pyheif
import tqdm


def convert_heic2png(heic_path, png_path):
    heif_file = pyheif.read(heic_path)
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(png_path, "PNG")


def main(input_dir_path, output_dir_path):
    os.makedirs(output_dir_path, exist_ok=True)
    heic_path_list = glob.glob(os.path.join(input_dir_path, '**/*.heic'), recursive=True)
    for heic_path in tqdm.tqdm(heic_path_list, desc='main'):
        output_png_path = os.path.join(output_dir_path, f'{os.path.basename(os.path.splitext(heic_path)[0])}.png')
        convert_heic2png(heic_path, output_png_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='main')
    parser.add_argument('--input_dir_path', type=str, default='~/Desktop/org_heic')
    parser.add_argument('--output_dir_path', type=str, default='~/Desktop/org_png')

    args = parser.parse_args()

    args.input_dir_path = os.path.expanduser(args.input_dir_path)
    args.output_dir_path = os.path.expanduser(args.output_dir_path)

    main(**args.__dict__)
