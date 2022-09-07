import json
import pprint

import xlrd
from utils.handle_path import data_path, configs_path
from utils.handle_yaml import get_yaml_data
import os

"""
#用例挑选
    1- 全部运行 all    默认模式
    2- 只选择某一个  tc003
    3- 连续用例 tc003-tc005
    4- 组合型  ['tc003','tc005-tc007','tc009']
"""


def get_excel_data(sheet_name, case_name, run_case=['all']):
    excelConfig_path = get_yaml_data(os.path.join(configs_path, 'excelConfig.yaml'))

    file_path = os.path.join(data_path, excelConfig_path['file_name'])
    args = excelConfig_path['col_name']

    work_book = xlrd.open_workbook(file_path, formatting_info=True)
    work_sheet = work_book.sheet_by_name(sheet_name)

    col_indexs = []
    for col_name in args:
        col_indexs.append(work_sheet.row_values(0).index(col_name))

    run_case_data = []
    if 'all' in run_case:
        run_case_data = work_sheet.col_values(0)
    else:
        for one in run_case:
            if '-' in one:
                start, end = one.split('-')
                for num in range(int(start), int(end) + 1):
                    run_case_data.append(case_name + f'{num:0>3}')
            else:
                run_case_data.append(case_name + f'{one:0>3}')
    print('需要运行的用例:', run_case_data)

    res_list = []

    row_idx = 0
    for one in work_sheet.col_values(0):
        if case_name in one and one in run_case_data:
            col_datas = []
            for num in col_indexs:
                tmp = is_json(work_sheet.cell(row_idx, num).value)
                col_datas.append(tmp)
            res_list.append(tuple(col_datas))
        row_idx += 1
    return res_list


def is_json(str):
    try:
        return json.loads(str)
    except:
        return str


if __name__ == '__main__':
    res = get_excel_data('登录模块', 'Login', run_case='all')
    pprint.pprint(res)
