import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr"
counts = dict()
find_section = sys.argv[1]

if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
            if jsonData['pqr_info']['welding_process2'] != "":
                for key in jsonData[find_section].keys():
                    counts[key] = counts.get(key, 0)+1

for item in counts.items():
    print(item)

print(len(counts))
