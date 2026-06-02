import os
import shutil

# Source folder
path = r"C:\\Users\\antimyadav\\OneDrive\\Desktop\\intern Task"

# New folder for JPG files
image_folder = os.path.join(path, "Images")

# Create Images folder if it doesn't exist
if not os.path.exists(image_folder):
    os.mkdir(image_folder)

# Get all files from source folder
files = os.listdir(path)

# Move JPG files
for file in files:

    if file.endswith(".jpg"):

        source = os.path.join(path, file)

        destination = os.path.join(image_folder, file)

#file ko move kardo
        shutil.move(source, destination)

    
        print(f"Moved: {file}")

print("All JPG files moved successfully!")