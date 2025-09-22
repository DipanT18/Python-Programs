#This program is written to demonstrate the use of the os module in Python for organizing files in a directory.
'''The main function of this program is to organize the pictures in a specific directory based on their file extensions.'''

import os

image_folder = "D:\Python-Programs\Python-Programs\os_module_usage\image_folder"  # <-- Set your folder path here

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.webp']
    # Add more file types and their corresponding extensions as needed
}

organized_files = {key: [] for key in file_types}

for item in os.listdir(image_folder):
    full_path = os.path.join(image_folder, item)
    if os.path.isfile(full_path):
        _, ext = os.path.splitext(item)
        ext = ext.lower()
        for type_name, extensions in file_types.items():
            if ext in extensions:
                organized_files[type_name].append(item)

for type_name, files in organized_files.items():
    print(f"{type_name}: {len(files)} files")
