import os

# Define the folder path containing .jpg and .json files
folder_path = '/home/zestiot/Downloads/water_mark_22_08_24/annotations_out/meta/'

# Get sets of base filenames (without extensions) for .jpg and .json files
jpg_files = {os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith('.jpg')}
json_files = {os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith('.txt')}

# Find extra .jpg files without a corresponding .json
extra_jpg_files = jpg_files - json_files
# Find extra .json files without a corresponding .jpg
extra_json_files = json_files - jpg_files

# Remove extra .jpg files
for base_name in extra_jpg_files:
    jpg_file_path = os.path.join(folder_path, f"{base_name}.jpg")
    os.remove(jpg_file_path)
    print(f"Removed {jpg_file_path}")

# Remove extra .json files
for base_name in extra_json_files:
    json_file_path = os.path.join(folder_path, f"{base_name}.txt")
    os.remove(json_file_path)
    print(f"Removed {json_file_path}")
