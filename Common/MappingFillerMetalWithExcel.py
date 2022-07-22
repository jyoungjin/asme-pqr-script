import json
import os
from openpyxl import Workbook

dir_path = "/Users/kimminju/Documents/asme-pqr"
map_path = "/Users/kimminju/Downloads/asme-mapping-fm-asmecode.json"
counts = dict()

write_wb = Workbook()
num = 0
dict_num = 0

for(root, directories, files) in os.walk(dir_path):
    # file 순회
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as file:
                jsonData = json.load(file)

                if 'aws_class' in jsonData['filler_metals']:
                    welding_process1 = jsonData['pqr_info']['welding_process1']
                    welding_process2 = jsonData['pqr_info']['welding_process2']
                    welding_process3 = jsonData['pqr_info']['welding_process3']
                    aws_class = jsonData['filler_metals']['aws_class']

                    if aws_class == None:
                        _sfa_no = None
                        _aws_class = None
                        _f_no = None
                        _a_no = None
                        jsonData["filler_metals"].update({
                            "_sfa_no": _sfa_no,
                            "_aws_class": _aws_class,
                            "_f_no": _f_no,
                            "_a_no": _a_no
                        })
                    else:
                        if type(aws_class) == dict: # dict 면 나눠서 update

                            _sfa_no1, _sfa_no2, _sfa_no3 = "", "", ""
                            _aws_class1, _aws_class2, _aws_class3 = "", "", ""
                            _f_no1, _f_no2, _f_no3 = "", "", ""
                            _a_no1, _a_no2, _a_no3 = "", "", ""
                            sfa_no = jsonData['filler_metals']['sfa_no']
                            aws_class = jsonData['filler_metals']['aws_class']
                            f_no = jsonData['filler_metals']['f_no']
                            a_no = jsonData['filler_metals']['a_no']

                            with open(map_path, 'r', encoding='utf-8') as map_fm_file:
                                fmData = json.load(map_fm_file)     # mapping 된 fm 데이터

                                for i in range(len(fmData)):
                                    fm_spec = fmData[i]['specification']
                                    fm_class = fmData[i]['classification']
                                    _fm_spec = fmData[i]["mapped specification"]
                                    _fm_class = fmData[i]["mapped classification"]
                                    _fm_f_no = str(fmData[i]["f no"])
                                    _fm_a_no = str(fmData[i]["a no"])

                                    if _fm_a_no == "None":
                                        _fm_a_no = None
                                    if _fm_a_no == "None":
                                        _fm_a_no = None
                                    # dict 하나씩 mapping fm data 랑 비교
                                    sfa1 = str(sfa_no.get(welding_process1))
                                    class1 = str(aws_class.get(welding_process1))
                                    if class1 == fm_class and sfa1 == fm_spec:
                                        _sfa_no1 = _fm_spec
                                        _aws_class1 = _fm_class
                                        _f_no1 = _fm_f_no
                                        _a_no1 = _fm_a_no

                                    # print(jsonData['filler_metals']['sfa_no'][welding_process1])
                                    if welding_process2 != "":
                                        sfa2 = str(sfa_no.get(welding_process2))
                                        class2 = str(aws_class.get(welding_process2))
                                        if class2 == fm_class and sfa2 == fm_spec:
                                            _sfa_no2 = _fm_spec
                                            _aws_class2 = _fm_class
                                            _f_no2 = _fm_f_no
                                            _a_no2 = _fm_a_no


                                    if welding_process3 != "":
                                        sfa3 = str(sfa_no.get(welding_process3))
                                        class3 = str(aws_class.get(welding_process3))
                                        if class3 == fm_class and sfa3 == fm_spec:
                                            _sfa_no3 = _fm_spec
                                            _aws_class3 = _fm_class
                                            _f_no3 = _fm_f_no
                                            _a_no3 = _fm_a_no

                                        # mk dict (process3)
                                        sfa_dict = {welding_process1:_sfa_no1, welding_process2:_sfa_no2, welding_process3:_sfa_no3}
                                        class_dict = {welding_process1:_aws_class1, welding_process2:_aws_class2, welding_process3:_aws_class3}
                                        f_dict = {welding_process1:_f_no1, welding_process2:_f_no2, welding_process3:_f_no3}
                                        a_dict = {welding_process1:_a_no1, welding_process2:_a_no2, welding_process3:_a_no3}


                                    else:      # mk dict (process2)
                                        sfa_dict = {welding_process1: _sfa_no1, welding_process2: _sfa_no2}
                                        class_dict = {welding_process1: _aws_class1, welding_process2: _aws_class2}
                                        f_dict = {welding_process1: _f_no1, welding_process2: _f_no2}
                                        a_dict = {welding_process1: _a_no1, welding_process2: _a_no2}




                            jsonData["filler_metals"].update({
                                "_sfa_no": sfa_dict,
                                "_aws_class": class_dict,
                                "_f_no": f_dict,
                                "_a_no": a_dict
                            })


                        else: # process 1개
                            key = str(aws_class)

                            with open(map_path, 'r', encoding='utf-8') as map_fm_file:
                                fmData = json.load(map_fm_file)  # mapping 된 fm 데이터

                                sfa_no = jsonData['filler_metals']['sfa_no']
                                aws_class = jsonData['filler_metals']['aws_class']
                                f_no = jsonData['filler_metals']['f_no']
                                a_no = jsonData['filler_metals']['a_no']

                                for i in range(len(fmData)):
                                    fm_spec = fmData[i]['specification']
                                    fm_class = fmData[i]['classification']
                                    _fm_spec = fmData[i]["mapped specification"]
                                    _fm_class = fmData[i]["mapped classification"]
                                    _fm_f_no = str(fmData[i]["f no"])
                                    _fm_a_no = str(fmData[i]["a no"])
                                    if _fm_a_no == "None":
                                        _fm_a_no = None
                                    if _fm_a_no == "None":
                                        _fm_a_no = None
                                    if fm_spec == sfa_no and fm_class == aws_class:     # mapping data 찾아서 저장
                                        _sfa_no = _fm_spec
                                        _aws_class = _fm_class
                                        _f_no = _fm_f_no
                                        _a_no = _fm_a_no
                                        num += 1

                            jsonData["filler_metals"].update({
                                "_sfa_no": _sfa_no,
                                "_aws_class": _aws_class,
                                "_f_no": _f_no,
                                "_a_no": _a_no
                            })

                with open(file_path, 'w', encoding='utf-8') as mk_f:
                    json.dump(jsonData, mk_f, indent=2, ensure_ascii=False)
print(num)
print(dict_num)