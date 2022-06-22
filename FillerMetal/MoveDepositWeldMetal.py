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
            if "deposit_weld_metal_thickness" in jsonData['base_metals'].keys():
                jsonData['filler_metals']['deposit_weld_metal_thickness'] = jsonData['base_metals']['deposit_weld_metal_thickness']
                del jsonData['base_metals']['deposit_weld_metal_thickness']
            with open(file_path, 'w', encoding='utf-8') as mk_f:
                json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
