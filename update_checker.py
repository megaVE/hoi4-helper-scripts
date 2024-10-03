import os, filecmp
from utils.file_helper import write_json_file

def compare_files(folder1: str, folder2: str):
    """Compares files between two folders, including subfolders."""
    dir_cmp = filecmp.dircmp(folder1, folder2)
    
    differences = []

    # Check files in the current directory
    for file in dir_cmp.common_files:
        file1 = os.path.join(folder1, file)
        file2 = os.path.join(folder2, file)

        if not filecmp.cmp(file1, file2, shallow=False):
            differences.append(file1)
    
    # Check common subdirectories recursively
    for subdir in dir_cmp.common_dirs:
        subfolder1 = os.path.join(folder1, subdir)
        subfolder2 = os.path.join(folder2, subdir)
        
        sub_differences = compare_files(subfolder1, subfolder2)
        differences.extend(sub_differences)

    return differences

def main(first_folder: str, second_folder: str, output_path: str) -> None:
    if not os.path.isdir(first_folder) or not os.path.isdir(second_folder):
        raise Exception ("Both paths must be valid directories.")

    differences = compare_files(first_folder, second_folder)
    
    if not differences:
        return print("No files with different content.")

    write_json_file(file_content=differences, file_path=output_path, )
