import json
from typing import Dict

def process_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data
