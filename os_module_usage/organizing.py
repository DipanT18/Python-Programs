#!/usr/bin/env python3
"""
FIXED Image Organizer Script
This program organizes images from the 'Images' folder into the 'image_folder' 
by their file extensions (jpg, png, etc.)
"""

import os
import shutil

def organize_images():
    """
    Organize images by their extensions
    """
    print("🖼️  Starting Image Organization...")
    
    # FIXED: Use relative paths and correct source/destination
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory where script is located
    source_folder = os.path.join(script_dir, "Images")
    dest_folder = os.path.join(script_dir, "image_folder")
    
    print(f"📁 Source folder: {source_folder}")
    print(f"📁 Destination folder: {dest_folder}")
    
    # FIXED: Check if source folder exists
    if not os.path.exists(source_folder):
        print(f"❌ Error: Source folder '{source_folder}' does not exist!")
        print("💡 Make sure you have an 'Images' folder with your image files.")
        pass
    
    # FIXED: Create destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"✅ Created destination folder: {dest_folder}")
    
    # Define file types and their extensions
    file_types = {
        'JPG_Images': ['.jpg', '.jpeg'],
        'PNG_Images': ['.png'],
        'WEBP_Images': ['.webp'],
        'Other_Images': ['.gif', '.bmp', '.tiff', '.svg']
    }
    
    # Track organized files
    organized_files = {key: [] for key in file_types}
    moved_count = 0
    
    # FIXED: Look in the SOURCE folder (Images), not destination
    print(f"\n🔍 Scanning source folder for images...")
    
    if not os.listdir(source_folder):
        print("📭 Source folder is empty!")
        return
    
    for item in os.listdir(source_folder):
        full_source_path = os.path.join(source_folder, item)
        
        # Only process files, not directories
        if os.path.isfile(full_source_path):
            _, ext = os.path.splitext(item)
            ext = ext.lower()
            
            # Find which category this file belongs to
            moved = False
            for type_name, extensions in file_types.items():
                if ext in extensions:
                    # FIXED: Create subfolder for this file type
                    type_folder = os.path.join(dest_folder, type_name)
                    if not os.path.exists(type_folder):
                        os.makedirs(type_folder)
                        print(f"📁 Created folder: {type_folder}")
                    
                    # FIXED: Actually MOVE the file
                    dest_path = os.path.join(type_folder, item)
                    
                    try:
                        shutil.move(full_source_path, dest_path)
                        organized_files[type_name].append(item)
                        moved_count += 1
                        print(f"📦 Moved: {item} → {type_name}")
                        moved = True
                        break
                    except Exception as e:
                        print(f"❌ Error moving {item}: {e}")
            
            if not moved and ext:  # File has extension but not in our categories
                print(f"⚠️  Skipped: {item} (extension '{ext}' not in categories)")
    
    # FIXED: Show meaningful results
    print(f"\n🎉 Organization Complete!")
    print(f"📊 Total files moved: {moved_count}")
    
    for type_name, files in organized_files.items():
        if files:  # Only show categories with files
            print(f"   {type_name}: {len(files)} files")
            for file in files[:3]:  # Show first 3 files as example
                print(f"      - {file}")
            if len(files) > 3:
                print(f"      - ... and {len(files) - 3} more files")

def main():
    """Main function"""
    try:
        organize_images()
    except KeyboardInterrupt:
        print("\n⏹️  Organization stopped by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()