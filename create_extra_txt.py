import os

# Define the folder path containing the .jpg files
folder_path = '/home/zestiot/Downloads/FOD_COD 1/Negatives/'  # Folder containing your .jpg files

# Loop through all the .jpg files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        # Get the base filename without the extension
        base_name = os.path.splitext(filename)[0]

        # Create the corresponding .txt file
        txt_file_path = os.path.join(folder_path, f"{base_name}.txt")

        # Create an empty .txt file
        open(txt_file_path, 'w').close()

        print(f"Created empty .txt file for {filename}")
