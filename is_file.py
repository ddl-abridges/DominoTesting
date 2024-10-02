import os
# Python Check if file exists

def is_file():
    if os.path.exists('/mnt/data/artifacts_backup/hey.txt'):
        print("File exists")
    else:
        print("File does not exist")