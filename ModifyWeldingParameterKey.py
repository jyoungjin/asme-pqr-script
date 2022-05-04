import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr"
counts = dict()
exceptCompany = '07. BUHEUNG'
find_key = sys.argv[1]
change_key = sys.argv[2]

if len(sys.argv) != 3:
    print("Insufficient arguments")
    sys.exit()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            if exceptCompany not in file_path:
                with open(file_path, 'r') as file:
                    jsonData = json.load(file)
                for object in jsonData['welding_parameters']:
                    if find_key in object:
                        print("aa")
                        object[change_key] = object[find_key]
                        del object[find_key]
                        with open(file_path, 'w', encoding='utf-8') as mk_f:
                            json.dump(jsonData, mk_f, indent=4, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')