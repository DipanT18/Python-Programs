import os
import shutil

base_file = "D:\\Python-Programs\\Python-Programs\\os_module_usage"
image_folder = os.path.join(base_file, "Images")

if not os.path.exists(image_folder):
    os.makedirs(image_folder)

for file_names in os.listdir(base_file):
    if file_names.endswith((".png", ".jpg", ".jpeg")):
        shutil.move(os.path.join(base_file, file_names), image_folder)

