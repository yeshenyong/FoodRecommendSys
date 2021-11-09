from flask import Flask, render_template, session, redirect, flash
from flask import request

import pymysql
import hashlib
import traceback
import random

app = Flask(__name__)
# 配置 SELECT_KEY
app.config['SECRET_KEY'] = '3c2d9d261a464e4e8814c5a39aa72f1c'

db = pymysql.connect(host="127.0.0.1", user="root", passwd="123456", db="foodserver")
cur = db.cursor()
recommendPath = "D:\\recommend.txt"

LOGIN = 1
REGIST = 2
RESET = 3

# 菜品推荐类型
RANDKIND = ['filter-card', 'filter-web', 'filter-app']

# 推荐结果
RECOM_MAP = {}


def SolveRecommend(path):
    for line in open(path):
        project = line.split("\t")
        recommend = project[1].split(":")
        list = []
        if project[0] in RECOM_MAP.keys():
            list = RECOM_MAP[project[0]]
        list.append(recommend[0])
        RECOM_MAP[project[0]] = list


SolveRecommend(recommendPath)


# 首页模块（默认无用户, 冷启动）
@app.route('/', methods=['GET'])
def hello_world():
    # 判断是否在登录状态上: 判断session是否有uname的值
    if 'uid' == session:
        # 已经登录，直接去往首页
        recommendlist = GetRecommendResult(session['uid'], 9)
        hotList = GetHotResult()
        return render_template("index.html", recommendlist=recommendlist, hotList=hotList)
    else:
        # 没有登录，继续向下判断cookie:
        if 'uid' in request.cookies:
            uid = request.cookies.get('uid')
            session['uid'] = uid
            recommendlist = GetRecommendResult(session['uid'], 9)
            hotList = GetHotResult()
            return render_template("index.html", recommendlist=recommendlist, hotList=hotList)
        else:
            # 默认推荐
            recommendlist = GetRecommendResult(0, 9)
            hotList = GetHotResult()
            """推荐列表
                {[fid, fname, fcomment, ffunc, fstep, ftaste, url],[...]}
            """
            print(recommendlist)
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
            return redirect('/login')
        except pymysql.Error:
            traceback.print_exc()
            db.rollback()
            return redirect('/registration')
    else:
        return redirect('/registration')


@app.route('/login', methods=['POST', 'GET'])
def login_check():
    if request.method == 'GET':
        if 'uid' in session:
            # 已经登录，直接去往首页
            return redirect('/')
        else:
            # 没有登录，继续向下判断cookie
            if 'uid' in request.cookies:
                # 曾经记住过密码, 取出值保存进session
                uid = request.cookies.get('uid')
                session['uid'] = uid
                return redirect('/')
            else:
                # 之前没有登录过，去往登录页
                return render_template('login.html')
    elif request.method == 'POST':
        recommendlist = {}
        username = request.form['username']
        passwd = request.form['password']

        passwd = Encryption(passwd)

        # 先处理登录，登录成功继续则保存进session，否则回到登录页
        sql = """ select uid, username, passwd from user where username='%s' and passwd='%s' """ % (username, passwd)
        cur.execute(sql)
        results = cur.fetchone()
        if results:
            # 声明重定向到首页的对象
            resp = redirect('/')
            # 登录成功保存session
            session['uid'] = results[0]
            if 'isSaved' in request.form:
                resp.set_cookie('uid', str(results[0]), 60 * 60 * 24 * 30)
            return resp
        else:
            flash("该用户名和密码不存在")
            return redirect('registration.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    resp = redirect('/')
    resp.delete_cookie('uid')
    session.pop('uid', None)
    return resp


# 加密函数
def Encryption(password):
    md5 = hashlib.md5()
    md5.update(password.encode())
    return md5.hexdigest()  # 返回加密的密码


# 推荐结果
def GetRecommendResult(uid, topK):
    recommendlist = []
    resultlist = []
    # print(type(uid))
    if uid == 0 or (str(uid) not in RECOM_MAP.keys()):
        sql = """select fname, fcomment, ffunc, fstep, ftaste, url from food limit 9 offset 2"""
        cur.execute(sql)
        resultlist = cur.fetchall()
    else:
        for i in range(0, topK):
            sql = """select fname, fcomment, ffunc, fstep, ftaste, url from food where fid='%s'""" % \
                  RECOM_MAP[str(uid)][i]
            cur.execute(sql)
            resultlist.append(list(cur.fetchone()))
        for i in range(0, len(resultlist)):
            tmplist = list(resultlist[i])
            tmplist.append(RANDKIND[random.randint(0, 2)])
    for i in range(0, len(resultlist)):
        tmplist = list(resultlist[i])
        tmplist.append(RANDKIND[random.randint(0, 2)])

        recommendlist.append(tmplist)
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
