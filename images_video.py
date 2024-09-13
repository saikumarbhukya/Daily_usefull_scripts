import cv2
import os
image_folder="/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/training/1/27_08_24_copy"
output_video="output_video"
frame_rate=20
images=[img for img in os.listdir(image_folder) if img.endswith('.png','.jpg','.jpeg')]
images.sort()
#read the first image to read hight and width of the video
first_image_path=os.path.join(image_folder,images[0])
frame=cv2.imread(first_image_path)
height,width,layer=frame.shape

#creating video writer
video=cv2.VideoWriter_vid(*'mp4v')
video_write=cv2.VideoWrite(output_video,video,frame_rate,(width,height))

#iterate through all images
for image in images:
