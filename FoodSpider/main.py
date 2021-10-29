# -*- coding: utf-8 -*-

# @Time    : 2021/10/26 19:28
# @Author  : yeshenyong
# @File    : main.py

from Excel.excel import save_excel
from MySql.mysql import init_db, save_db
from Analysis.spider import getData

baseUrl = "https://www.meishij.net/china-food/?&page="
dbName = ""
page = 10
Excelpath = "食品爬取结果.xls"


def main():
    dataList = getData(baseUrl, page)
    save_excel(dataList, Excelpath)
    save_db(dataList)


if __name__ == '__main__':
    init_db()
    main()
