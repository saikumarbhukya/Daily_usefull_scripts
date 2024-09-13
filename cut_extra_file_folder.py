import os
import shutil

# Define the folder paths
input_folder = '/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/inputs_jpg/'  # Folder containing .jpg and .json files
output_folder = '/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/inputs_jpg/extra_images'  # Folder to move extra .jpg files

# Create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get a set of the base filenames (without extensions) of the .json files
json_files = {os.path.splitext(f)[0] for f in os.listdir(input_folder) if f.endswith('.json')}

# Loop through the .jpg files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        # Get the base filename without the extension
        base_name = os.path.splitext(filename)[0]

        # Check if the .jpg file has a corresponding .json file
        if base_name not in json_files:
            # Move the extra .jpg file to the output folder
            src_path = os.path.join(input_folder, filename)
            dest_path = os.path.join(output_folder, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved {filename} to {output_folder}")
