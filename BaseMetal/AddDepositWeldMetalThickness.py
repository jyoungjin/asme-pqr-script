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
                if '_thickness(mm)' in jsonData['base_metals'] and '_to_thickness(mm)' in jsonData['base_metals']:
                    if jsonData['pqr_info']['welding_process2'] != "":
                        sum_of_thickness = 0
                        for item in jsonData['filler_metals']['_deposit_weld_metal_thickness(mm)']:
                            sum_of_thickness += jsonData['filler_metals']['_deposit_weld_metal_thickness(mm)'][item]

                        if round(sum_of_thickness, 2) != min(jsonData['base_metals']['_thickness(mm)'], jsonData['base_metals']['_to_thickness(mm)']):
                            print("========================================================================================================")
                            print(round(sum_of_thickness, 2))
                            print(min(jsonData['base_metals']['_thickness(mm)'], jsonData['base_metals']['_to_thickness(mm)']))
                            print(jsonData['pqr_info']['company'])
                            print(jsonData['pqr_info']['procedure_qualification_record_no'])
                    # with open(file_path, 'w', encoding='utf-8') as mk_f:
                    #     json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
