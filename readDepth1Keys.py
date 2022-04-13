import json
import os

dir_path = "/Users/youngjin/workspace/otos/pqr-json-data"
counts = dict()
exceptCompany = '07. BUHEUNG'

for(root, directories, files) in os.walk(dir_path):
    # directory 순회
    # for d in directories:
    #     if d not in exceptDict:
    #         d_path = os.path.join(root,d)

    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root,file)
            if exceptCompany not in file_path:
                jsonData = json.load(open(file_path))
                for key in jsonData.keys():
                    if(key == 'pwht'):
                        key = 'postweld_heat_treatment'
                    counts[key] = counts.get(key,0)+1
                    json.dumps(jsonData,indent='\t')

itemlist = counts.items()
for item in itemlist:
    print(item)

print("=============================================")