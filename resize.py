from PIL import Image
import os

def resize_images(input_folder, output_folder, width=2048, height=390):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        img_path = os.path.join(input_folder, filename)
        if os.path.isfile(img_path):
            with Image.open(img_path) as img:
                resized_img = img.resize((width, height))
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)
                print(f"Resized and saved {filename} to {output_folder}")

input_folder = '/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/dataset_24.08.24'
output_folder = '/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/dataset_24.08.24_out'

resize_images(input_folder, output_folder)
