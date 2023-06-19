import os
from PIL import Image

script_dir = os.path.dirname(os.path.abspath(__file__))

compressed_dir = os.path.join(script_dir, 'compressed')
if not os.path.exists(compressed_dir):
    os.mkdir(compressed_dir)

for filename in os.listdir(script_dir):
    if filename.endswith('.webp'):
        with Image.open(filename) as img:
            quality = 50
            output_path = os.path.join(compressed_dir, filename)
            img.save(output_path, 'webp', quality=quality)

print("Image compression is complete!")