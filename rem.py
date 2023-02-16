from rembg import remove
import os
from PIL import Image
import shutil

# Warning 
print("Please dont rename this file, use this program only in folder with only photos that should be edited.\n In the folder should be only photos and this program.\nIf current folder gonna contain other files like : folders, zip, exe, etc. The program don't gonna work properly.")

# Create folders named by users input
 
input_result_folder = input("Name of result folder for images with backgound : ")
input_transparent_folder = input("Name of folder with transparent backgrounds : ")

# Input for RGB backgrounds :

input_color_red = int(input("Red : "))
input_color_green = int(input("Green  : "))
input_color_blue =  int(input("Blue : "))

# Variables initialization by users input, for future uses in code

fill_color = (input_color_red ,input_color_green,input_color_blue)
result_folder = input_result_folder
transparent_folder = input_transparent_folder

# Get photos from current folder
photos = os.listdir(os.getcwd())
output_photos_names = [ x  + '.jpg' for x in photos]

# Create Folders
is_exist_results = os.path.exists(result_folder)
is_exist_transparent = os.path.exists(transparent_folder)


if not is_exist_results:
  
   os.makedirs(result_folder)

if not is_exist_transparent:
  
   os.makedirs(transparent_folder)


#  Loop through photos
for i in range(len(photos)):

# Error handling to not handle folders and current running file as a photo
    if photos[i] != os.path.basename(__file__) and photos[i] != result_folder and photos[i] != transparent_folder and photos[i] == 'rem.exe' :    

        with open(photos[i], 'rb') as input_photo:

            with open(output_photos_names[i], 'wb') as ouput_photo:

                    # Removing backgrounds  
                    input = input_photo.read()
                    output = remove(input)
                    ouput_photo.write(output)

                    #  Setting backgrounds
                    im = Image.open(os.getcwd()  + "\\" + output_photos_names[i])
                    im = im.convert("RGBA")

                    if im.mode in ('RGBA', 'LA'):
                        background = Image.new(im.mode[:-1], im.size, fill_color)
                        background.paste(im, im.split()[-1])
                        im = background

                    # Put photos with setted background to the golder
                    im.convert("RGB").save(os.getcwd() +  '\\'+ result_folder +'\\' + output_photos_names[i])

                    im.close()
                    ouput_photo.close()

                    #  Put transparent photoss into folder
                    shutil.move(os.getcwd()  + "\\" + output_photos_names[i], os.getcwd()  + "\\" + transparent_folder +"\\" + output_photos_names[i])

                    
    else:

        continue