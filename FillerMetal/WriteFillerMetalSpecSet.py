import json
import os
from openpyxl import Workbook

dir_path = "/Users/youngjin/workspace/json-data/asme-pqr"
counts = dict()

write_wb = Workbook()

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
                            key = sfa_no[process] + "," + aws_class[process]
                            counts[key] = counts.get(key, 0)+1
                    else:
                        key = sfa_no + "," + aws_class
                        counts[key] = counts.get(key, 0) + 1

write_ws = write_wb.active
write_ws['A1'] = 'sfa no'
write_ws['B1'] = 'aws class'
write_ws['C1'] = 'count'

for key, val in counts.items():
    arr = key.split(',')
    write_ws.append([arr[0], arr[1], val])

write_wb.save('/Users/youngjin/Desktop/test/asme-filler-metal4.xlsx')
