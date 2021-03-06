import json
import os

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr"
counts = dict()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
            if 'other' in jsonData['gas']:
               jsonData['gas']['others'] = jsonData['gas']['other']
               del jsonData['gas']['other']
               with open(file_path, 'w', encoding='utf-8') as mk_f:
                   json.dump(jsonData, mk_f, indent=4, ensure_ascii=False)
