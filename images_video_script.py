import cv2
import os

# Define the path to the folder containing images
image_folder = '/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/training/1/27_08_24_copy'
output_video = '/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/training/1/output_video.mp4'
frame_rate = 7  # Set the desired frame rate

# Get a list of all image files in the folder
images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
images.sort()  # Sort images by name

if not images:
    print("No images found in the folder.")
    exit()

# Read the first image to determine the width and height of the video
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' is a codec for mp4
video = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

# Check if the video writer was successfully initialized
if not video.isOpened():
    print("Error: Could not open the output video file for writing.")
    exit()

# Iterate through all the images and write each one to the video
for image in images:
    image_path = os.path.join(image_folder, image)
    frame = cv2.imread(image_path)
    video.write(frame)

# Release the video writer object
video.release()

print(f"Video created successfully: {output_video}")
