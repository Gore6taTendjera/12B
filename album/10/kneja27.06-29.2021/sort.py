import os
import datetime

# Get the directory name of the Python script file
dir_path = os.path.dirname(os.path.realpath(__file__))

# Set the current working directory to the directory of the Python script file
os.chdir(dir_path)

# Get a list of all .jpg files in the directory
jpg_files = [f for f in os.listdir() if f.endswith('.jpg')]

# Sort the list of .jpg files by creation time, with the oldest files first
jpg_files.sort(key=lambda x: os.path.getctime(x))

# Loop through the sorted .jpg files, renaming them with a numbered prefix
for i, filename in enumerate(jpg_files):
    # Generate a new name for the file, using a numbered prefix
    new_name = f"{i+1:03d}.jpg"
    # Rename the file
    os.rename(filename, new_name)
