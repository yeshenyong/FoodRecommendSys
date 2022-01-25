# -*- coding: utf-8 -*-

# @Time    : 2022/1/24 0:57
# @Author  : yeshenyong
# @File    : main.py

import time
from pyquery import PyQuery as pq
from selenium import webdriver
import pandas as pd
class FinanceCrawler:
    def __init__(self):
        pass

    def get_tag_index(self, target_name, data_title):
        tag_index = []
        for i in range(len(data_title)):
            if data_title[i] in target_name:
                tag_index.append(i-1)
        return tag_index

    def get_finance_forecast(self):
        options = webdriver.ChromeOptions()

        # 添加头部
        options.add_argument(
            'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"'
        )
        driver = webdriver.Chrome("./chromedriver", chrome_options=options)

        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get:() => undefined
            })        
        """
            },
        )

        driver.get(
            f"https://basic.10jqka.com.cn/601888/finance.html#stockpage"
        )

        print(driver.page_source)
        if "Nginx forbidden" in driver.page_source:
            print("爬虫被识别")
        doc = pq(driver.page_source)
        # print(doc)
        year_list = ['20' + ("%02d" % i) for i in range(20, 2, -1)]
        month_list = ['-12-31', '-09-30', '-06-30', '-03-31']
        year_list = [(year + month) for year in year_list for month in month_list]

        data_title = [i.text() for i in doc(f"table tbody tr th").items()]
        target_name = ["资产负债比率", "营业总收入(元)", "净利润"]
        dag_index = self.get_tag_index(target_name, data_title)
        print(dag_index)
        print(data_title)
        data_title = [i.text() for i in doc(f"table tbody tr td").items()]
        year_title = list(set([i.text() for i in doc(f"table tbody tr th div").items()]))
        year_title.sort(reverse=True)
        prof_list = []
        length = len(year_title)
        for idx in range(0, len(data_title)):
            if idx == 1*length:
                prof_list.append([data_title[idx + i] for i in range(length)])
                # print([data_title[idx + i] for i in range(length)])
            elif idx == 5*length:
                prof_list.append([data_title[idx + i] for i in range(length)])
                # print([data_title[idx + i] for i in range(length)])
            elif idx == 28*length:
                prof_list.append([data_title[idx + i] for i in range(length)])
                # print([data_title[idx + i] + '%' for i in range(length)])
        list1 = []
        list2 = []
        list3 = []
        for i in range(len(year_list)):
            if year_list[i] in year_title:
                list1.append(prof_list[0][year_title.index(year_list[i])])
                list2.append(prof_list[1][year_title.index(year_list[i])])
                list3.append(prof_list[2][year_title.index(year_list[i])])
            else:
                list1.append('--')
                list2.append('--')
                list3.append('--')
        print(list1)
        print(list2)
        print(list3)



        # dataframe = pd.DataFrame(prof_map)
        # # 将DataFrame存储为csv,index表示是否显示行名，default=True
        # dataframe.to_csv("净利润.csv", index=False, sep=',', encoding="utf_8_sig")
        # dataframe = pd.DataFrame(debt_map)
        # dataframe.to_csv("资产负债比率.csv", index=False, sep=',', encoding="utf_8_sig")
        # dataframe = pd.DataFrame(mone_map)
        # dataframe.to_csv("营业总收入.csv", index=False, sep=',', encoding="utf_8_sig")
        driver.quit()


obj = FinanceCrawler()
obj.get_finance_forecast()























