import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr"
counts = dict()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
            if 'tungsten_electrode_type' in jsonData['electrical_characteristics']:
                if 'tungsten_electrode_size' not in jsonData['electrical_characteristics']:
                    print(jsonData['pqr_info']['company'])
                    print(jsonData['pqr_info']['original_file_name'])
