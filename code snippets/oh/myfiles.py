import os
from os.path import expanduser

def get_files(pattern='.py', directory = expanduser('~')):
    # default for python code files in home directory
    found_files = []
    dir_list = os.listdir(directory)
    for file in dir_list:
        if (pattern in file):
            found_files.append(file)
    return found_files


text_files = get_files('.txt', '.')
print(text_files)