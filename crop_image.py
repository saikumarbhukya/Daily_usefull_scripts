from PIL import Image
import os

input_folder="/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/11.0924"
output_folder="/home/zestiot/Desktop/Zestiot/PROJECTS/JSW/data/11.0924_split_out"
#create the output directory if does not exist
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

#process each image
for img in os.listdir(input_folder):
    if img.endswith('.jpg'):
        image_path=os.path.join(input_folder,img)
        image=Image.open(image_path)

        width,height=image.size

        if width==2048 and height==390:
            left_half=image.crop((0,0,width//2,height))
            right_half=image.crop((width//2,0,width,height))

            #save cropped images
            left_half.save(os.path.join(output_folder,f'{img[:-4]}_left.jpg'))
            right_half.save(os.path.join(output_folder,f'{img[:-4]}_right.jpg'))
print("image cropeed successfully")
