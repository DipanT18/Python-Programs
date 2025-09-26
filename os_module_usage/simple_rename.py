#This program is written to rename the file simple using os module

import os

# Define the directory path
directory_path = r"D:\Python-Programs\Python-Programs\os_module_usage\PNG_Files"

# Get a sorted list of all items (files and folders)
files = sorted(os.listdir(directory_path))

i = 7
for file in files:
    # Check if the item is a file and ends with ".png"
    if file.endswith(".png"):
        # Construct the full old path
        old_path = os.path.join(directory_path, file)

        # Create the new filename with the sequential number and extension
        new_filename = f"{i}.png"
        new_path = os.path.join(directory_path, new_filename)

        # Rename the file
        os.rename(old_path, new_path)
        print(f"Renamed '{file}' to '{new_filename}'")
        
        i += 1


