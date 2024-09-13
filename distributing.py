import os
import shutil
from math import ceil


def clean_move_and_distribute_files(source_folder, output_folder):
    # Define custom folder names
    folder_names = [
        'Batch_9A', 'Batch_9B',
    ]
    num_folders = len(folder_names)

    # Ensure the source folder exists
    if not os.path.exists(source_folder):
        print(f"Source folder {source_folder} does not exist.")
        return

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder, exist_ok=True)

    # List all .jpg and .txt files
    jpg_files = sorted([f for f in os.listdir(source_folder) if f.endswith('.jpg')])
    txt_files = sorted([f for f in os.listdir(source_folder) if f.endswith('.txt')])

    # Check for extra .txt files
    jpg_bases = set(f.replace('.jpg', '') for f in jpg_files)
    txt_bases = set(f.replace('.txt', '') for f in txt_files)

    extra_txt_bases = txt_bases - jpg_bases

    # Delete extra .txt files
    for base in extra_txt_bases:
        extra_txt_file = f"{base}.txt"
        extra_txt_path = os.path.join(source_folder, extra_txt_file)
        if os.path.exists(extra_txt_path):
            os.remove(extra_txt_path)
            print(f"Deleted extra file: {extra_txt_file}")

    # Update list of .txt files after deletion
    txt_files = sorted([f for f in os.listdir(source_folder) if f.endswith('.txt')])

    # Create target folders with specified names
    for folder_name in folder_names:
        folder_path = os.path.join(source_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Calculate number of files per folder
    files_per_folder = ceil(len(jpg_files) / num_folders)

    # Move files into folders
    for idx, file in enumerate(jpg_files):
        folder_num = (idx // files_per_folder)
        folder_name = folder_names[folder_num]
        folder_path = os.path.join(source_folder, folder_name)

        # Move .jpg file
        shutil.move(os.path.join(source_folder, file), folder_path)

        # Move corresponding .txt file if it exists
        txt_file = file.replace('.jpg', '.txt')
        if txt_file in txt_files:
            shutil.move(os.path.join(source_folder, txt_file), folder_path)
        else:
            print(f"Warning: Missing corresponding .txt file for {file}")

    # Move folders to output directory
    for folder_name in folder_names:
        src_folder = os.path.join(source_folder, folder_name)
        dst_folder = os.path.join(output_folder, folder_name)
        shutil.move(src_folder, dst_folder)
        print(f"Moved {src_folder} to {dst_folder}")

    print("Files have been cleaned, distributed, and moved into the output folder successfully.")


# Example usage
source_folder = "/home/zestiot/Downloads/water_mark_22_08_24/water_mark_10_folders/Folder_9/"  # Change this to your source folder path
output_folder = "/home/zestiot/Downloads/water_mark_22_08_24/water_mark_10_folders/Folder_9_out"  # Change this to your output folder path
clean_move_and_distribute_files(source_folder, output_folder)
