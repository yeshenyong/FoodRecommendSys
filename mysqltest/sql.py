# -*- coding: utf-8 -*-

# @Time    : 2021/10/29 12:14
# @Author  : yeshenyong
# @File    : sql.py

import pymysql
import random
import hashlib

db = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="foodserver")
cur = db.cursor()


# 加密函数
def Encryption(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()  # 返回加密的密码


if __name__ == '__main__':
    username = "yeshenyong"
    passwd = "123456"
    passwd = Encryption(passwd)
    # print(passwd)
    # regissql = """insert into user(username, passwd) values('%s', '%s')"""
    #
    # try:
    #     cur.execute(regissql % (username, passwd))
    #     db.commit()
    #     print("sucessfully")
    # except pymysql.Error:
    #     print("unsucessfully")
    #     db.rollback()

    # loginsql = """ select uid, username, passwd from user where username='%s' and passwd='%s' """ % (username, passwd)
    # cur.execute(loginsql)
    #
    # results = cur.fetchone()
    # print(results[0])
    # print(results[1])
    # print(results[2])
    # def GetHotResult():
    # hotlist = []
    # sql = """select fname, fcomment, ffunc, fstep, ftaste, url from food limit 4"""
    #
    # try:
    #     cur.execute(sql)
    #     results = cur.fetchall()
    #     hotlist = results
    #     # for i in (0, len(results)):
    #     #     print(results[i])
    #         # hotlist.append(results[i])
    # except pymysql.Error:
    #     db.rollback()
    #
    # print(hotlist[0])

    print(random.randint(0, 1))

    db.close()


