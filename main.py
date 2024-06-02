import subprocess
import os
import shutil

def copy_files_from_mobile(source_path, destination_path):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    
    # List files in the source directory on the Android device
    adb_command_list = f'adb shell ls "{source_path}"'
    result = subprocess.run(adb_command_list, shell=True, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error listing files: {result.stderr}")
        return

    files = result.stdout.splitlines()

    # Copy each file from the Android device to the destination directory
    for file in files:
        src_file = os.path.join(source_path, file).replace("\\", "/")
        dest_file = os.path.join(destination_path, file)
        adb_command_copy = f'adb pull "{src_file}" "{dest_file}"'
        result = subprocess.run(adb_command_copy, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"Copied {src_file} to {dest_file}")
        else:
            print(f"Error copying {src_file}: {result.stderr}")

# Define source and destination paths
source_path = "/storage/emulated/0/Your folder path"  # Change this to your source folder on the Android device
destination_path = "Destination path"  # Change this to your destination folder on the E: drive

# Copy files from mobile to D: drive
copy_files_from_mobile(source_path, destination_path)
