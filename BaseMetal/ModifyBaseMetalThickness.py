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
                if 'thickness' in jsonData['base_metals'] and 'to_thickness' in jsonData['base_metals']:

                    jsonData['base_metals']['_thickness(mm)'] = float(jsonData['base_metals']['_thickness(mm)'].upper().strip("MM"))
                    jsonData['base_metals']['_to_thickness(mm)'] = float(jsonData['base_metals']['_to_thickness(mm)'].upper().strip("MM"))

                    with open(file_path, 'w', encoding='utf-8') as mk_f:
                        json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
