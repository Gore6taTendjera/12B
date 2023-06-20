from PIL import Image
import os

def reduce_resolution(image_path):
    image = Image.open(image_path)
    width, height = image.size
    new_width = width // 2
    new_height = height // 2
    resized_image = image.resize((new_width, new_height))
    
    output_folder = "resized"
    os.makedirs(output_folder, exist_ok=True)

    file_name = os.path.basename(image_path)
    output_path = os.path.join(output_folder, file_name)

    resized_image.save(output_path)

def process_webp_files():
    current_directory = os.getcwd()
    for file_name in os.listdir(current_directory):
        if file_name.endswith(".webp"):
            file_path = os.path.join(current_directory, file_name)
            reduce_resolution(file_path)
            print(f"Reduced resolution of {file_name}")

process_webp_files()
