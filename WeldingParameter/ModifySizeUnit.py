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
            for object in jsonData['welding_parameters']:
                if "size(mm)" in object:
                    sizeVal = object["size(mm)"]
                    if sizeVal is None:
                        object["size(mm)"] = None
                    else:
                        sizeVal = sizeVal.strip("ø")
                        object["_size(mm)"] = float(sizeVal)
                    with open(file_path, 'w', encoding='utf-8') as mk_f:
                        json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
