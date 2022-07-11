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
            if jsonData['base_metals']['_material_spec'] is None:
                jsonData['base_metals']['_material_spec'] = jsonData['base_metals']['material_spec']
                jsonData['base_metals']['_type_and_grade'] = jsonData['base_metals']['type_and_grade']
                jsonData['base_metals']['_p_no'] = "unlisted"
                jsonData['base_metals']['_gr_no'] = "unlisted"
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
            if jsonData['base_metals']['_to_material_spec'] is None:
                jsonData['base_metals']['_to_material_spec'] = jsonData['base_metals']['to_material_spec']
                jsonData['base_metals']['_to_type_and_grade'] = jsonData['base_metals']['to_type_and_grade']
                jsonData['base_metals']['_to_p_no'] = "unlisted"
                jsonData['base_metals']['_to_gr_no'] = "unlisted"
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)


