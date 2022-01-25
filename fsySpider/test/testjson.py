# -*- coding: utf-8 -*-

# @Time    : 2022/1/23 11:55
# @Author  : yeshenyong
# @File    : testjson.py

import os
import json

os.chdir(os.path.dirname(os.getcwd()))
config_file = 'ST一重.json'

with open(config_file, 'r', encoding='utf-8') as f:
    config = json.loads(f.read().encode('unicode_escape').decode('unicode_escape'))

print(config)