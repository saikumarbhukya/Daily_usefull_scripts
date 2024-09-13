import os

def create_empty_txt_for_images(folder_path):
    # List all files in the directory
    files = os.listdir(folder_path)

    # Separate images and annotations
    images = [f for f in files if f.endswith('.jpg')]
    annotations = [f for f in files if f.endswith('.txt')]

    # Create a set of base filenames for images and annotations
    image_basenames = {os.path.splitext(img)[0] for img in images}
    annotation_basenames = {os.path.splitext(txt)[0] for txt in annotations}

    # Find images that don't have corresponding .txt files
    orphaned_images = image_basenames - annotation_basenames

    # Create empty .txt files for those orphaned images
    for img_base in orphaned_images:
        txt_path = os.path.join(folder_path, f"{img_base}.txt")
        with open(txt_path, 'w') as f:
            pass  # Create an empty file

    print(f"Created {len(orphaned_images)} empty .txt files for images without annotations.")

if __name__ == "__main__":
    # Set the path to your folder where both .jpg and .txt files are located
    folder_path = '/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/11.0924_split_out'  # Change this to your actual folder path
    create_empty_txt_for_images(folder_path)
