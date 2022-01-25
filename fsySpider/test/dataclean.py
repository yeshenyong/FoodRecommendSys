# -*- coding: utf-8 -*-

# @Time    : 2022/1/22 4:15
# @Author  : yeshenyong
# @File    : dataclean.py

import os
import sys


def clean(file_name):
    # · 首创股份(600008)
    # · *首创股份(600008)
    # ignore
    fd = open(file_name, 'r', encoding='gbk')
    transmit = ""
    while True:
        line = fd.readline()
        if not line:
            break
        line = line.strip().strip(')').split('(')
        # map[line[0]] = line[1]
        # print(line)
        if len(line) < 2:
            continue
        transmit += line[0] + ":" + line[1] + "\n"
    fd.close()
    fd = open(file_name, 'w', encoding='gbk')
    fd.write(transmit)
    fd.close()


if __name__ == '__main__':
    cur_path = os.path.join(os.path.dirname(os.getcwd()), 'data')
    cur_dir = os.path.join(cur_path, 'map.txt')
    # print(cur_dir)
    clean(cur_dir)
