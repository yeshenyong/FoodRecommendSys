# -*- coding: utf-8 -*-

# @Time    : 2022/1/22 22:32
# @Author  : yeshenyong
# @File    : testhtml.py
# 导入urllib
import urllib.request
# 定义一个头部
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36',
    'cookie': 'spversion=20130314; searchGuide=sg; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1642760784,1642857185; reviewJump=nojump; historystock=601518%7C*%7C000777%7C*%7C601611%7C*%7C601179; usersurvey=1; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1642941541; v=A9jR3KcDDVYEXCHSjt8nuXBZqQ1vwTxLniUQzxLJJJPGrXYzutEM2-414Fth'
}
# 给url加头部
_url = urllib.request.Request('http://stockpage.10jqka.com.cn/601179/finance/#finance', headers=headers)
# 打开url
response = urllib.request.urlopen(_url, None, 10)
# 读取返回的内容
html = response.read().decode('utf-8')
# 写入txt
print(html)
# with open('html','w',encoding='utf-8') as f:
    # f.write(html)