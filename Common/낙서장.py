import json
import os
import sys

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr"
counts = dict()

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)
                if "singlepass_or_multipass" in jsonData['technique'] and "multipass_or_singlepass(per side)" in jsonData['technique']:
                    print("Company: ", jsonData['pqr_info']['company'])
                    print("PQR No: ", jsonData['pqr_info']['procedure_qualification_record_no'])
