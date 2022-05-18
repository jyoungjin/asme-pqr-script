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
            if "gas_backing" in jsonData['gas'].keys():
                if "gas" in jsonData['gas']['gas_backing'].keys():
                    jsonData['gas']['gas_backing']['gas(es)'] = jsonData['gas']['gas_backing']['gas']
                    del jsonData['gas']['gas_backing']['gas']
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
