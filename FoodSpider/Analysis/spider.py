# -*- coding: utf-8 -*-

# @Time    : 2021/10/26 19:40
# @Author  : yeshenyong
# @File    : fsy.py

import urllib.request, urllib.error
import re
from bs4 import BeautifulSoup

# 正则表达式

# 食品名字
findName = re.compile(r'<strong>(.*)</strong>')
# 食品评论和人气 和 食品的功效
findComment = re.compile(r'<span>(.*)</span>')
# 食品总共步骤
findStep = re.compile(r'<li class="li1">(.*?)</li>')
# 食品的口味
findTaste = re.compile(r'<li class="li2">(.*)</li>')
# 食品图像
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包含在字符中


def getData(baseUrl, page):
    dataList = []
    for i in range(0, page):
        url = baseUrl + str(i+1)
        html = getEachHtml(url)
        # print(html)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="listtyle1"):
            data = []
            item = str(item)

            name = re.findall(findName, item)
            data.append(name)

            comment = re.findall(findComment, item)
            if len(comment) == 2:
                foodcomment = comment[0]
                data.append(foodcomment)
                foodfunc = comment[1]
                data.append(foodfunc)
            else:
                foodcomment = comment[0]
                data.append(foodcomment)
                data.append(' ')

            step = re.findall(findStep, item)
            if len(step) == 1:
                data.append(step)
                # print(step)
            else:
                data.append(' ')

            taste = re.findall(findTaste, item)
            data.append(taste)

            imgsrc = re.findall(findImgSrc,item)
            data.append(imgsrc)

            dataList.append(data)
        """
            1.食品名字
            2.食品评论和人气
            3.食品的功效
            4.食品总共步骤
            5.食品的口味
            6.食品的图片URL
        """
    return dataList

def getEachHtml(baseUrl):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }
    request = urllib.request.Request(baseUrl, headers=head)
    html = ""
    try:
        respones = urllib.request.urlopen(request)
        html = respones.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html