from typing import List

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()
