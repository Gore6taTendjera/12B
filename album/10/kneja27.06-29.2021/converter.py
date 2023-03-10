import os
from PIL import Image

# Define the folder where the images are located
img_folder = os.getcwd()

# Define the name of the output folder for the converted images
output_folder = 'webp_images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all the files in the folder
for filename in os.listdir(img_folder):
    if filename.endswith('.jpg'):
        # Open the image using PIL
        with Image.open(filename) as im:
            # Construct the output filename and path
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_folder, output_filename)
            # Convert the image to WEBP format and save it
            im.save(output_path, 'webp')

print('All JPEG files in the folder have been converted to WEBP format and saved in the ' + output_folder + ' folder.')
