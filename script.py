
from pathlib import Path
import os, time

# Input file name
file_name = input("Enter your file name: ")

parent_dir = '/Users/hongphuc/Documents/PLAYGROUND/python-script-playground'

# ** = all sub-directories, *.txt = all files with .txt extension
matching_file_pattern = ('**/{}.txt').format(file_name)

for file in Path(parent_dir).glob(matching_file_pattern):
    print(file.parent)

    # Create target directory if not exists
    # target_dir = '/Users/hongphuc/Documents/PLAYGROUND/python-script-playground-backup'
    target_dir = str(file.parent).replace("python-script-playground", "python-script-playground-backup")
    print(target_dir)
    Path(target_dir).mkdir(parents=True, exist_ok=True)

    # Copy file to target directory
    new_file_path = Path(target_dir + '/' + file.name)
    Path(file).rename(new_file_path)