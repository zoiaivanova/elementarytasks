import json
import os


def from_file(directory, file):
    test_data_file_path = os.path.join(directory, file)
    with open(test_data_file_path, 'r') as file:
        return json.loads(file.read())
