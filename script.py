
from pathlib import Path
import os, time, datetime

# Input file date
# Date format: dd/mm/yyyy
file_date = input("Enter your datetime: ")

parent_dir = '/Users/hongphuc/Documents/PLAYGROUND/python-script-playground'

# ** = all sub-directories, *.txt = all files with .txt extension
# matching_file_pattern = ('**/*.txt').format(file_name)

for file in Path(parent_dir).glob('**/*.txt'):
    print("=====")
    print("File path: {}".format(file))

    file_created_at = datetime.datetime.fromtimestamp(os.path.getctime(file))
    file_created_at_date = file_created_at.strftime('%d/%m/%Y')
    print("File created at: {}".format(file_created_at_date))

    if file_created_at_date == file_date:
      print("File found")

      # Create target directory if not exists
      target_dir = '/Users/hongphuc/Documents/PLAYGROUND/python-script-playground-backup'
      target_dir = str(file.parent).replace("python-script-playground", "python-script-playground-backup")
      Path(target_dir).mkdir(parents=True, exist_ok=True)

      # Copy file to target directory
      new_file_path = Path(target_dir + '/' + file.name)
      Path(file).rename(new_file_path)
      print("File copied to: {}".format(new_file_path))
    else:
      print("File not found")

    print("====")
    print()