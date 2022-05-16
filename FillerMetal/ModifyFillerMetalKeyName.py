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
            if "size" in jsonData['filler_metals'].keys():
                jsonData['filler_metals']['size_of_electrode'] = jsonData['filler_metals']['size']
                del jsonData['filler_metals']['size']
            with open(file_path, 'w', encoding='utf-8') as mk_f:
                json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
