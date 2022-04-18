import json
import os

dir_path = "/Users/youngjin/workspace/otos/pqr-json-data"
counts = dict()
exceptCompany = '07. BUHEUNG'

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            if exceptCompany not in file_path:
                with open(file_path, 'r') as file:
                    jsonData = json.load(file)
                if 'other' in jsonData['base_metals']:
                   jsonData['base_metals']['others'] = jsonData['base_metals']['other']
                   del jsonData['base_metals']['other']
                   with open(file_path, 'w', encoding='utf-8') as mk_f:
                       json.dump(jsonData, mk_f, indent=4, ensure_ascii=False)
