# -*- coding: utf-8 -*-

# @Time    : 2021/10/26 19:35
# @Author  : yeshenyong
# @File    : mysql.py

import pymysql

conn = pymysql.connect(host='localhost', user='root', passwd='123456', database='foodserver', charset='utf8')
cursor = conn.cursor()
sql = 'insert into food(fname, fcomment, ffunc, fstep, ftaste, url) values(%s,%s,%s,%s,%s,%s) '

def init_db():
    pass


def save_db(dataList):
    for i in range(0, len(dataList)):
        # print(dataList[i])
        try:
            cursor.execute(sql, dataList[i])
            conn.commit()
        except Exception as e:
            print('插入数据失败', e)
            conn.rollback()  # 回滚

    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    pass
