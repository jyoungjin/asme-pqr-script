import json
import os

dir_path = "/Users/youngjin/workspace/otos/pqr-json-data"
counts = dict()
exceptCompany = '07. BUHEUNG'
aa = list()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root,file)
            if exceptCompany not in file_path:
                with open(file_path, 'r') as file:
                    jsonData = json.load(file)
                    flag = 0;
                for key in jsonData.keys():
                    if key == 'notes':
                       flag = 1
                       aa.append(file_path)
                    counts[key] = counts.get(key,0)+1

                if flag == 0:
                    jsonData['notes'] = {}
                    with open(file_path, 'w', encoding='utf-8') as mk_f:
                        json.dump(jsonData, mk_f, indent='\t')

for item in counts.items():
    print(item)

for file_path in aa:
    print(file_path)

# print("=============================================")