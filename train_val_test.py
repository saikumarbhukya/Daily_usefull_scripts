import os
import shutil
import random

# Paths
source_folder = '/home/zestiot/Downloads/To_Sai/Model_train_1_5_08_24_out'
train_folder = '/home/zestiot/Downloads/To_Sai/Training/Train'
val_folder = '/home/zestiot/Downloads/To_Sai/Training/val'
test_folder = '/home/zestiot/Downloads/To_Sai/Training/Test'

# Split ratios
train_ratio = 0.8
val_ratio = 0.2
test_ratio = 0.1

# Get list of files
all_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
txt_files = [f for f in all_files if f.lower().endswith('.txt')]

# Ensure that txt files correspond to image files
image_base_names = set(os.path.splitext(f)[0] for f in image_files)
txt_base_names = set(os.path.splitext(f)[0] for f in txt_files)
missing_txt_files = image_base_names - txt_base_names

if missing_txt_files:
    raise ValueError(f"Missing text files for images: {missing_txt_files}")

# Shuffle files
random.shuffle(image_files)

# Calculate split sizes
total_files = len(image_files)
train_end = int(train_ratio * total_files)
val_end = int((train_ratio + val_ratio) * total_files)

# Split files
train_files = image_files[:train_end]
val_files = image_files[train_end:val_end]
test_files = image_files[val_end:]

# Function to move files
def move_files(file_list, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    for file in file_list:
        # Move image files
        shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))
        # Move corresponding txt files
        txt_file = os.path.splitext(file)[0] + '.txt'
        if txt_file in txt_files:
            shutil.move(os.path.join(source_folder, txt_file), os.path.join(destination_folder, txt_file))

# Move files to respective folders
move_files(train_files, train_folder)
move_files(val_files, val_folder)
move_files(test_files, test_folder)

print(f"Data split completed:\nTrain: {len(train_files)}\nVal: {len(val_files)}\nTest: {len(test_files)}")
