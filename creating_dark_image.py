import os
from PIL import Image

# Define the source and destination folders
source_folder = '/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/revents/31.08.24_CBD'  # Folder containing the .jpg images
destination_folder = '/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/revents/31.08.24_CBD_dark'  # Folder where the blank .png images will be saved

# Ensure destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Iterate over all files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith('.jpg'):  # Check if the file is a .jpg image
        # Create a blank (0-pixel, completely dark) image with the same dimensions as the original
        img = Image.open(os.path.join(source_folder, filename))
        blank_img = Image.new('RGB', img.size, (0, 0, 0))  # Create a black image

        # Save the blank image as PNG with the same name in the destination folder
        new_filename = filename.replace('.jpg', '.png')
        blank_img.save(os.path.join(destination_folder, new_filename))

print("Blank images created successfully with the same names.")
