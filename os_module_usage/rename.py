#!/usr/bin/env python3
"""
Fixed PNG File Renamer
This program checks if a directory exists and renames PNG files in ascending order (1.png, 2.png, etc.)
"""

import os
import shutil

def check_existence(dir_path):
    """Check if directory exists and return True/False"""
    if os.path.exists(dir_path):
        print(f"✅ {dir_path} exists")
        return True
    else:
        print(f"❌ {dir_path} doesn't exist")
        return False

def sequential_rename(directory, file_extension='.png'):
    """
    Rename files in directory to sequential numbers (1.png, 2.png, etc.)
    
    Args:
        directory (str): Path to directory containing files
        file_extension (str): Extension of files to rename (default: '.png')
    """
    try:
        # FIXED: Check if directory exists first
        if not check_existence(directory):
            return
        
        # FIXED: Get only PNG files and sort them
        all_files = os.listdir(directory)
        png_files = []
        
        for filename in all_files:
            # Check if it's a file and has the right extension
            full_path = os.path.join(directory, filename)
            if os.path.isfile(full_path) and filename.lower().endswith(file_extension.lower()):
                png_files.append(filename)
        
        if not png_files:
            print(f"📭 No {file_extension} files found in the directory!")
            return
        
        # Sort files for consistent renaming
        png_files.sort()
        print(f"📊 Found {len(png_files)} {file_extension} files to rename")
        
        # Show what will be renamed
        print("\n📋 Files to be renamed:")
        for i, filename in enumerate(png_files, 1):
            print(f"   {filename} → {i}{file_extension}")
        
        # Ask for confirmation
        confirm = input(f"\n❓ Proceed with renaming {len(png_files)} files? (y/n): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("⏹️  Operation cancelled")
            return
        
        # FIXED: Create backup folder
        backup_folder = os.path.join(directory, 'backup_original_names')
        if not os.path.exists(backup_folder):
            os.makedirs(backup_folder)
            print(f"💾 Created backup folder: {backup_folder}")
        
        # Backup original files
        for filename in png_files:
            src = os.path.join(directory, filename)
            dst = os.path.join(backup_folder, filename)
            shutil.copy2(src, dst)
        print(f"💾 Backed up {len(png_files)} files")
        
        # FIXED: Use temporary names to avoid conflicts
        temp_renames = []
        counter = 1
        
        print("\n🔄 Renaming files...")
        
        # Step 1: Rename to temporary names
        for filename in png_files:
            old_path = os.path.join(directory, filename)
            temp_name = f"temp_{counter}_{filename}"
            temp_path = os.path.join(directory, temp_name)
            
            os.rename(old_path, temp_path)
            temp_renames.append((temp_name, f"{counter}{file_extension}"))
            counter += 1
        
        # Step 2: Rename from temp to final names
        renamed_count = 0
        for temp_name, final_name in temp_renames:
            temp_path = os.path.join(directory, temp_name)
            final_path = os.path.join(directory, final_name)
            
            os.rename(temp_path, final_path)
            print(f"✅ Renamed to '{final_name}'")
            renamed_count += 1
        
        print(f"\n🎉 Successfully renamed {renamed_count} {file_extension} files!")
        
    except FileNotFoundError:
        print(f"❌ {directory} not found")
    except PermissionError:
        print(f"❌ Permission denied. Run as administrator or check folder permissions")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        
        # Try to restore from temp names if something went wrong
        print("🔧 Attempting to restore...")
        try:
            for temp_name, _ in temp_renames:
                temp_path = os.path.join(directory, temp_name)
                if os.path.exists(temp_path):
                    # Extract original name from temp name
                    original_name = temp_name.split('_', 2)[-1]  # Get part after "temp_X_"
                    original_path = os.path.join(directory, original_name)
                    os.rename(temp_path, original_path)
        except:
            print("❌ Could not restore. Check backup folder.")

def main():
    """Main function with user-friendly interface"""
    print("🖼️  PNG FILE RENAMER")
    print("=" * 30)
    
    # FIXED: Use current directory or let user specify
    print("📁 Choose directory option:")
    print("1. Use current directory")
    print("2. Specify custom path")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        folder_to_rename = '.'  # Current directory
        print(f"Using current directory: {os.path.abspath('.')}")
    elif choice == '2':
        folder_to_rename = input("Enter full path to directory: ").strip()
        # FIXED: Remove quotes if user accidentally included them
        folder_to_rename = folder_to_rename.strip('\'"')
    else:
        print("❌ Invalid choice")
        return
    
    # Ask for file extension
    file_ext = input("Enter file extension (default: .png): ").strip()
    if not file_ext:
        file_ext = '.png'
    elif not file_ext.startswith('.'):
        file_ext = '.' + file_ext
    
    # Call the renaming function
    sequential_rename(folder_to_rename, file_ext)

# Alternative: Simple version without all the safety features
def simple_version():
    """Simplified version of your original intent"""
    
    # FIXED: Use raw string or forward slashes for Windows paths
    folder_to_rename = r"D:\Python-Programs\Python-Programs\os_module_usage\PNG_Files"
    # OR use forward slashes: "D:/Python-Programs/Python-Programs/os_module_usage/PNG_Files"
    
    # Check if directory exists
    if not os.path.exists(folder_to_rename):
        print(f"❌ Directory {folder_to_rename} doesn't exist")
        return
    
    # Get PNG files only
    png_files = [f for f in os.listdir(folder_to_rename) 
                 if f.lower().endswith('.png') and 
                 os.path.isfile(os.path.join(folder_to_rename, f))]
    
    if not png_files:
        print("❌ No PNG files found")
        return
    
    png_files.sort()
    print(f"📊 Renaming {len(png_files)} PNG files...")
    
    # Rename files
    for i, filename in enumerate(png_files, 1):
        old_path = os.path.join(folder_to_rename, filename)
        new_filename = f"{i}.png"
        new_path = os.path.join(folder_to_rename, new_filename)
        
        # Skip if already correctly named
        if filename != new_filename:
            try:
                os.rename(old_path, new_path)
                print(f"✅ {filename} → {new_filename}")
            except FileExistsError:
                print(f"⚠️  Skipped {filename} (target exists)")
            except Exception as e:
                print(f"❌ Error renaming {filename}: {e}")

if __name__ == "__main__":
    print("Choose version:")
    print("1. Full version (recommended)")
    print("2. Simple version")
    
    version = input("Enter choice (1 or 2): ").strip()
    
    if version == '1':
        main()
    elif version == '2':
        simple_version()
    else:
        print("❌ Invalid choice, running full version")
        main() 