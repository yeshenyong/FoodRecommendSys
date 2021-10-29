# -*- coding: utf-8 -*-

# @Time    : 2021/10/26 20:26
# @Author  : yeshenyong
# @File    : excel.py

import xlwt


def save_excel(datalist, path):
    print("saving...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('食品', cell_overwrite_ok=True)
    """
        1.食品名字
        2.食品评论和人气
        3.食品的功效
        4.食品总共步骤
        5.食品的口味
        6.食品的图片URL
    """
    col = ("食品名字", "食品评论和人气", "食品功效", "食品步骤", "食品口味", "图片链接")
    for i in range(len(col)):
        sheet.write(0, i, col[i])

    for i in range(0, len(datalist)):
        # print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, len(data)):
            sheet.write(i + 1, j, data[j])
    book.save(path)

