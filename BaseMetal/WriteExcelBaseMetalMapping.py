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
                    type_and_grade = jsonData['base_metals']['type_and_grade']
                    p_no = jsonData['base_metals']['p_no']
                    gr_no = jsonData['base_metals']['gr_no']
                    uns_no = ""
                    if 'uns_no' in jsonData['base_metals']:
                        uns_no = jsonData['base_metals']['uns_no']
                    mapped_material_spec = jsonData['base_metals']['_material_spec']
                    mapped_type_and_grade = jsonData['base_metals']['_type_and_grade']
                    mapped_p_no = jsonData['base_metals']['_p_no']
                    mapped_gr_no = jsonData['base_metals']['_gr_no']

                    mapped_uns_no = ""
                    if '_uns_no' in jsonData['base_metals']:
                        mapped_uns_no = jsonData['base_metals']['_uns_no']

                    to_material_spec = jsonData['base_metals']['to_material_spec']
                    to_type_and_grade = jsonData['base_metals']['to_type_and_grade']
                    to_p_no = jsonData['base_metals']['to_p_no']
                    to_gr_no = jsonData['base_metals']['to_gr_no']
                    to_uns_no = ""
                    if 'to_uns_no' in jsonData['base_metals']:
                        to_uns_no = jsonData['base_metals']['to_uns_no']
                    mapped_to_material_spec = jsonData['base_metals']['_to_material_spec']
                    mapped_to_type_and_grade = jsonData['base_metals']['_to_type_and_grade']
                    mapped_to_p_no = jsonData['base_metals']['_to_p_no']
                    mapped_to_gr_no = jsonData['base_metals']['_to_gr_no']

                    mapped_to_uns_no = ""
                    if '_to_uns_no' in jsonData['base_metals']:
                        mapped_to_uns_no = jsonData['base_metals']['_to_uns_no']

                    key = material_spec+"?"+type_and_grade+"?"+p_no+"?"+gr_no+"?"+uns_no
                    key += "?"
                    if mapped_material_spec is not None:
                        key += mapped_material_spec
                    key += "?"
                    if mapped_type_and_grade is not None:
                        key += mapped_type_and_grade
                    key += "?"
                    if mapped_p_no is not None:
                        key += mapped_p_no
                    key += "?"
                    if mapped_gr_no is not None:
                        key += mapped_gr_no
                    key += "?"
                    if mapped_uns_no is not None:
                        key += mapped_uns_no

                    to_key = to_material_spec+"?"+to_type_and_grade+"?"+to_p_no+"?"+to_gr_no+"?"+to_uns_no
                    to_key += "?"
                    if mapped_to_material_spec is not None:
                        to_key += mapped_to_material_spec
                    to_key += "?"
                    if mapped_to_type_and_grade is not None:
                        to_key += mapped_to_type_and_grade
                    to_key += "?"
                    if mapped_to_p_no is not None:
                        to_key += mapped_to_p_no
                    to_key += "?"
                    if mapped_to_gr_no is not None:
                        to_key += mapped_to_gr_no
                    to_key += "?"
                    if mapped_to_uns_no is not None:
                        to_key += mapped_to_uns_no
                    counts[key] = counts.get(key, 0) + 1
                    counts[to_key] = counts.get(to_key, 0) + 1

write_ws = write_wb.active
write_ws['A1'] = 'Material Spec'
write_ws['B1'] = 'Type and Grade'
write_ws['C1'] = 'P No'
write_ws['D1'] = 'GR No'
write_ws['E1'] = 'UNS No'
write_ws['F1'] = 'Count'
write_ws['G1'] = 'Mapped Material Spec'
write_ws['H1'] = 'Mapped Type and Grade'
write_ws['I1'] = 'Mapped P No'
write_ws['J1'] = 'Mapped GR No'
write_ws['K1'] = 'Mapped UNS No'

for key, val in counts.items():
    arr = key.split('?')
    write_ws.append([arr[0], arr[1], arr[2], arr[3], arr[4], val, arr[5], arr[6], arr[7], arr[8], arr[9]])

write_wb.save('/Users/youngjin/Desktop/test/asme-base-metal.xlsx')

for item in counts.items():
    print(item)

print(len(counts))