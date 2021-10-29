from flask import Flask, render_template
from flask import request

import pymysql
import hashlib
import traceback
import random
import datetime
import urllib
import json

app = Flask(__name__)
db = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="foodserver")
cur = db.cursor()

LOGIN = 1
REGIST = 2
RESET = 3

# 菜品推荐类型
RANDKIND = ['filter-card', 'filter-web', 'filter-app']

# 首页模块（默认无用户, 冷启动）
@app.route('/', methods=['GET'])
def hello_world():
    recommendlist = GetRecommendResult(0)
    hotList = GetHotResult()
    """推荐列表
        {[fid, fname, fcomment, ffunc, fstep, ftaste, url],[...]}
    """
    return render_template("index.html", recommendlist=recommendlist, hotList=hotList)


# 注册模块
@app.route('/registration', methods=['GET'])
def register():
    return render_template("registration.html")


@app.route('/registration', methods=['POST'])
def register_check():
    username = request.form['username']
    password = request.form['password']
    sql = """select * from user where username='%s'"""

    n = cur.execute(sql % username)

    db.commit()

    if n <= 0:
        sql_insert = """insert into user(username, passwd) values('%s', '%s')"""
        password = Encryption(password)
        try:
            cur.execute(sql_insert % (username, password))
            db.commit()
            return render_template('login.html')
        except pymysql.Error:
            traceback.print_exc()
            db.rollback()
            return render_template('registration.html', result='注册失败')
    else:
        return render_template('registration.html', result='已存在用户名')


# 登录模块
@app.route('/login', methods=['GET'])
def login():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_check():
    recommendlist = {}
    username = request.form['username']
    passwd = request.form['password']

    passwd = Encryption(passwd)

    sql = """ select uid, username, passwd from user where username='%s' and passwd='%s' """ % (username, passwd)
    cur.execute(sql)
    results = cur.fetchone()
    if results:
        recommendlist = GetRecommendResult(results[0])
        hotlist = GetHotResult()
        return render_template('index.html', recommendlist=recommendlist, hotlist=hotlist)
    else:
        return render_template('registration.html')


# 加密函数
def Encryption(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()  # 返回加密的密码


# 推荐结果
def GetRecommendResult(uid):
    recommendlist = []
    resultlist = []
    if uid == 0:
        sql = """select fname, fcomment, ffunc, fstep, ftaste, url from food limit 9 offset 2"""
        cur.execute(sql)
        resultlist = cur.fetchall()
    else:
        resultlist = []
    for i in range(0, len(resultlist)):
        tmplist = list(resultlist[i])
        tmplist.append(RANDKIND[random.randint(0, 2)])

        recommendlist.append(tmplist)
        print(recommendlist)

    return recommendlist


# 热点新闻
def GetHotResult():
    hotlist = []
    sql = """select fname, fcomment, ffunc, fstep, ftaste, url from food limit 4"""

    try:
        cur.execute(sql)
        results = cur.fetchall()
        hotlist = results
    except pymysql.Error:
        db.rollback()

    return hotlist


if __name__ == '__main__':
    app.run()
