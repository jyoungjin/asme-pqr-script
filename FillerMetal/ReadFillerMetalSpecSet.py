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
                if 'sfa_no' in jsonData['filler_metals'] and 'aws_class' in jsonData['filler_metals']:

                    sfa_no = jsonData['filler_metals']['sfa_no']
                    aws_class = jsonData['filler_metals']['aws_class']

                    if type(sfa_no) == dict:
                        for process in sfa_no:
                            key = "spec: "+sfa_no[process] + ", class: " + aws_class[process]
                            counts[key] = counts.get(key, 0)+1
                    else:
                        key = "spec: " + sfa_no + ", class: " + aws_class
                        counts[key] = counts.get(key, 0) + 1

for item in counts.items():
    print(item)

print(len(counts))
# for item in counts.keys():
#     print(item, end=', ')