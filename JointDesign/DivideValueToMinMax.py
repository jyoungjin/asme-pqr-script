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

                # root_face
                # if 'root_face' in jsonData['joint_design']:
                #     value = jsonData['joint_design']['root_face'].upper().strip("MM")
                #     if "~" in value:
                #         arr = value.split('~')
                #         if float(arr[0]) > float(arr[1]):
                #             print("앞에 수가 더 큽니다.")
                #             print(jsonData['pqr_info']['procedure_qualification_record_no'])
                #         jsonData['joint_design']['_root_face_min(mm)']  = float(arr[0])
                #         jsonData['joint_design']['_root_face_max(mm)']  = float(arr[1])
                #     else:
                #         jsonData['joint_design']['_root_face_min(mm)'] = float(value)
                #         jsonData['joint_design']['_root_face_max(mm)'] = float(value)
                #
                # # root_opening
                # if 'root_opening' in jsonData['joint_design']:
                #     value = jsonData['joint_design']['root_opening'].upper().strip("MM")
                #     if "~" in value:
                #         arr = value.split('~')
                #         if float(arr[0]) > float(arr[1]):
                #             print("앞에 수가 더 큽니다.")
                #             print(jsonData['pqr_info']['procedure_qualification_record_no'])
                #         jsonData['joint_design']['_root_opening_min(mm)'] = float(arr[0])
                #         jsonData['joint_design']['_root_opening_max(mm)'] = float(arr[1])
                #     else:
                #         jsonData['joint_design']['_root_opening_min(mm)'] = float(value)
                #         jsonData['joint_design']['_root_opening_max(mm)'] = float(value)
                #
                # # groove_angle
                # if 'groove_angle' in jsonData['joint_design']:
                #     value = jsonData['joint_design']['groove_angle'].strip("°")
                #     if "~" in value:
                #         arr = value.split('~')
                #         if float(arr[0]) > float(arr[1]):
                #             print("앞에 수가 더 큽니다.")
                #             print(jsonData['pqr_info']['procedure_qualification_record_no'])
                #         jsonData['joint_design']['_groove_angle_min(°)'] = float(arr[0])
                #         jsonData['joint_design']['_groove_angle_max(°)'] = float(arr[1])
                #     else:
                #         jsonData['joint_design']['_groove_angle_min(°)'] = float(value)
                #         jsonData['joint_design']['_groove_angle_max(°)'] = float(value)
                #
                # # back_groove_angle
                # if 'back_groove_angle' in jsonData['joint_design']:
                #     value = jsonData['joint_design']['back_groove_angle'].strip("°")
                #     if "~" in value:
                #         arr = value.split('~')
                #         if float(arr[0]) > float(arr[1]):
                #             print("앞에 수가 더 큽니다.")
                #             print(jsonData['pqr_info']['procedure_qualification_record_no'])
                #         jsonData['joint_design']['_back_groove_angle_min(°)'] = float(arr[0])
                #         jsonData['joint_design']['_back_groove_angle_max(°)'] = float(arr[1])
                #     else:
                #         jsonData['joint_design']['_back_groove_angle_min(°)'] = float(value)
                #         jsonData['joint_design']['_back_groove_angle_max(°)'] = float(value)

                # back_groove_angle
                if 'bevel_angle' in jsonData['joint_design']:
                    value = jsonData['joint_design']['bevel_angle'].strip("°")
                    if "~" in value:
                        arr = value.split('~')
                        if float(arr[0]) > float(arr[1]):
                            print("앞에 수가 더 큽니다.")
                            print(jsonData['pqr_info']['procedure_qualification_record_no'])
                        jsonData['joint_design']['_bevel_angle_min(°)'] = float(arr[0])
                        jsonData['joint_design']['_bevel_angle_max(°)'] = float(arr[1])
                    else:
                        jsonData['joint_design']['_bevel_angle_min(°)'] = float(value)
                        jsonData['joint_design']['_bevel_angle_max(°)'] = float(value)

                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
