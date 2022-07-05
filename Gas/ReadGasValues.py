import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr"
counts = dict()
find_section = sys.argv[1]
find_key = sys.argv[2]

if len(sys.argv) != 3:
    print("Insufficient arguments")
    sys.exit()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
            if find_section in jsonData['gas']:
                if find_key in jsonData['gas'][find_section]:
                    key = jsonData['gas'][find_section][find_key]
                    if type(key) == dict:
                        for item in key.values():
                            counts[item] = counts.get(item, 0) + 1
                    else:
                        counts[key] = counts.get(key, 0) + 1

sum = 0

for key, value in counts.items():
    print(key, value)
    sum += value

print("종류 " + str(len(counts)))
print("합계: " + str(sum))

# for item in counts.keys():
#     print(item, end=', ')