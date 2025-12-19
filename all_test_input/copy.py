import shutil
from pathlib import Path
import os

def copy_files_by_extension_flat(source_dir, destination_dir, extension):
    """
    Recursively finds all files with a specific extension in the source directory
    and copies them to a flat destination directory.

    Args:
        source_dir (str): The path to the source directory (e.g., './source_folder').
        destination_dir (str): The path to the destination directory (e.g., './destination_folder').
        extension (str): The file extension to search for (e.g., '*.txt' or '*.jpg').
    """
    # Convert directory strings to Path objects for easy manipulation
    source_path = Path(source_dir)
    destination_path = Path(destination_dir)

    # 1. Ensure the destination directory exists.
    #    We use exist_ok=True so it doesn't raise an error if the directory
    #    is already there. This is different from shutil.copytree, which
    #    requires the destination not to exist.
    destination_path.mkdir(parents=True, exist_ok=True)

    print(f"Starting file search in: {source_path}")
    print(f"Targeting extension: {extension}")

    # 2. Recursively find all files matching the extension using pathlib.rglob
    #    The '**/' part is implicit with rglob, and the extension pattern
    #    locates the relevant files across all subdirectories.
    found_files = source_path.rglob(f"*{extension}")

    # 3. Iterate through the found files and copy each one to the destination
    copied_count = 0
    for file_path in found_files:
        if file_path.is_file(): # Ensure it's a file, not a directory that matched a pattern
            # Construct the destination file path.
            # We use only the original file name to keep the destination directory flat.
            destination_file = destination_path / file_path.name
            
            # In case multiple files with the same name exist in different
            # source subdirectories, you might need a naming strategy.
            # Here, shutil.copy2 will overwrite any existing file with the
            # same name.
            try:
                shutil.copy2(file_path, destination_file)
                print(f"  Copied: {file_path.name}")
                copied_count += 1
            except shutil.SameFileError:
                print(f"  Skipped (same file): {file_path.name}")
            except Exception as e:
                print(f"  Error copying {file_path.name}: {e}")

    print(f"\nOperation complete. Total files copied: {copied_count}")

# --- Example Usage ---
# Define your source and destination directories and the extension


# --- Example Usage ---
if __name__ == "__main__":
    SOURCE = './source_directory'
    DESTINATION = './flat_destination'
    EXTENSION = '.txt' # Can be '.jpg', '.csv', etc.
    # Define your source and destination directories and the desired extension
    SOURCE = "C:/phits" # Replace with your source path
    DESTINATION = "C:/Users/nnQuynh_7490/Desktop/all_phits" # Replace with your destination path
    EXTENSION = ".inp" # Replace with the extension you want (e.g., '.jpg', '.pdf')

    copy_files_by_extension_flat(SOURCE, DESTINATION, EXTENSION)
