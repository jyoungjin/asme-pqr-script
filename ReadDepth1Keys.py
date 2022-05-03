import json
import os

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr"
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
                with open(file_path, 'r') as file:
                    jsonData = json.load(file)
                    flag = 0
                for key in jsonData.keys():
                    # if key == 'notes':
                    #    flag = 1
                    # if(key == 'pwht'):
                    #     jsonData[key] = 'postweld_heat_treatment'
                    counts[key] = counts.get(key,0)+1

                if flag == 0:
                    jsonData['notes'] = {}

for item in counts.items():
    print(item)

 # print("=============================================")