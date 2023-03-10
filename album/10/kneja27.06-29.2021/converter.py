import os
from PIL import Image

img_folder = os.getcwd()

output_folder = 'webp_images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(img_folder):
    if filename.endswith('.jpg'):
        with Image.open(filename) as im:
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_folder, output_filename)
            im.save(output_path, 'webp')

print('All JPEG files in the folder have been converted to WEBP format and saved in the ' + output_folder + ' folder.')
