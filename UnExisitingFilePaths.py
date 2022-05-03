import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr"
counts = dict()
exceptCompany = '07. BUHEUNG'
find_section = sys.argv[1]
find_key = sys.argv[2]

aa = list()

if len(sys.argv) != 3:
    print("Insufficient arguments")
    sys.exit()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root,file)
            if exceptCompany not in file_path:
                with open(file_path, 'r') as file:
                    jsonData = json.load(file)
                    flag = 0
                for key in jsonData[find_section].keys():
                    counts[key] = counts.get(key, 0)+1
                    if key == find_key:
                        flag = 1
                if flag == 0:
                    aa.append(file_path)


# for item in counts.items():
#     print(item)

for item in aa:
    print(item)