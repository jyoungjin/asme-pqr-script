import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr/07. BUHEUNG"
counts = dict()
cnt = 0

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
            if 'joint_details' in jsonData.keys():
                cnt += 1
                for key, value in jsonData['joint_details'].items():
                    jsonData['joint_design'][key] = value
                del jsonData['joint_details']
                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=4, ensure_ascii=False)

# for item in counts.keys():
#     print(item, end=', ')

print(cnt)