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
                if 'material_spec' in jsonData['base_metals'] and 'type_and_grade' in jsonData['base_metals']:

                    material_spec = jsonData['base_metals']['material_spec']
                    to_material_spec = jsonData['base_metals']['to_material_spec']
                    type_and_grade = jsonData['base_metals']['type_and_grade']
                    to_type_and_grade = jsonData['base_metals']['to_type_and_grade']
                    p_no = jsonData['base_metals']['p_no']
                    to_p_no = jsonData['base_metals']['to_p_no']
                    gr_no = jsonData['base_metals']['gr_no']
                    to_gr_no = jsonData['base_metals']['to_gr_no']

                    key = material_spec+","+type_and_grade+","+p_no+","+gr_no
                    to_key = to_material_spec+","+to_type_and_grade+","+to_p_no+","+to_gr_no
                    counts[key] = counts.get(key, 0) + 1
                    counts[to_key] = counts.get(to_key, 0) + 1

write_ws = write_wb.active
write_ws['A1'] = 'material_spec'
write_ws['B1'] = 'type_and_grade'
write_ws['C1'] = 'p no'
write_ws['D1'] = 'gr no'
write_ws['E1'] = 'count'

for key, val in counts.items():
    arr = key.split(',')
    write_ws.append([arr[0], arr[1], arr[2], arr[3], val])

write_wb.save('/Users/youngjin/Desktop/test/test.xlsx')