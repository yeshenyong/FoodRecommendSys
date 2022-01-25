# -*- coding: utf-8 -*-

# @Time    : 2022/1/22 4:11
# @Author  : yeshenyong
# @File    : test01.py

import json
import os


def calculate_percent(company_list, data_path):
    mmap = {}
    fd = open(data_path, 'r')
    while True:
        line = fd.readline()
        if not line:
            break
        line = line.strip().split(':')
        mmap[line[0]] = line[1]
        print(line[0] + ":" + mmap[line[0]])
    fd.close()

    for idx in range(len(company_list)):
        if company_list[idx] not in mmap:
            print("without {}".format(company_list[idx]))


if __name__ == '__main__':
    path = os.path.join(os.path.dirname(os.getcwd()), 'config.json')
    # path = os.path.join(path, 'map.txt')
    with open(path, encoding='utf-8') as f:
        data = json.loads(f.read())
    path = os.path.join(os.path.dirname(os.getcwd()), 'data')
    path = os.path.join(path, 'map.txt')
    calculate_percent(data["company_list"][0].split(','), path)