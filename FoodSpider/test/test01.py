# -*- coding: utf-8 -*-

# @Time    : 2022/1/3 18:24
# @Author  : yeshenyong
# @File    : test01.py

# class person():
#     def __init__(self, age, name):
#         self.__age = age
#         self.name = name
#
#
# class people(person):
#     def __init__(self, age, name, score):
#         person.__init__(self, age, name)
#         self.score = score
#
#
# s = people(18, "ye", 81)
# print(dir(s))
# print(s._person__age)

# class A:
#     def say(self):
#         print("A recalled!!!")
#
# class C:
#     def say(self):
#         print("C recalled!!!")
#
# class B(C, A):
#     def say(self):
#         #A.say(self)
#         super().say()
#         print("B recalled!!!")
#
# b = B()
# b.say()

# class man():
#     pass
#
# class Chinese(man):
#     def eat(self):
#         print("chinese use chopsticks!!")
# class English(man):
#     def eat(self):
#         print("english use knives!!!")
#
# def manEat(m):
#     if isinstance(m, man):
#         m.eat()
#     else:
#         print("不能吃饭")
#
# manEat(English())

# class person:
#     def __init__(self, name):
#         self.name = name
#
#     def __add__(self, other):
#         if isinstance(other, person):
#             return "{0} + {1}".format(other.name, self.name)
#         else:
#             return "error"
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return other * self.name
#         else:
#             return "error"
#
#     def __rmul__(self, other):
#         if isinstance(other, int):
#             return other * self.name
#         else:
#             return "error"
#
#
# p = person("ye")
# print(p + p)
# print(p * 2)
# print(2 * p)
#
# class A:
#     pass
# class B:
#     pass
# class C(B, A):
#     def __init__(self, nn):
#         self.nn = nn
#     def cc(self):
#         print("cc recalled")
#
# classc = C(3)
# print(classc.__dict__)
# print(classc.__class__)
# print(C.__bases__)
# print(C.mro())
# print(A.__subclasses__())

# import copy
# class phone:
#     def __init__(self, cpu, screen):
#         self.cpu = cpu
#         self.screen = screen
# class cpu:
#     pass
# class screen:
#     pass
# c1 = cpu()
# s1 = screen()
# m1 = phone(c1, s1)
# # 赋值
# m2 = m1
# print(m1, m1.cpu, m1.screen)
# print(m2, m2.cpu, m2.screen)
# # 浅拷贝
# m2 = copy.copy(m1)
# print(m1, m1.cpu, m1.screen)
# print(m2, m2.cpu, m2.screen)
# # 深拷贝
# m2 = copy.deepcopy(m1)
# print(m1, m1.cpu, m1.screen)
# print(m2, m2.cpu, m2.screen)

# import threading
# class MySingleton:
#     _instance_lock = threading.Lock()
#
#     def __init__(self):
#         pass
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(MySingleton, "_instance"):
#             with MySingleton._instance_lock:
#                 if not hasattr(MySingleton, "_instance"):
#                     MySingleton._instance = object.__new__(cls)
#         return MySingleton._instance
# obj1 = MySingleton()
# obj2 = MySingleton()
# print(obj1)
# print(obj2)

# a = input("input a")
# b = input("input b")
#
# try:
#     a = int(a)
#     b = int(b)
#     c = a / b
#     print(c)
# except ValueError:
#     print('error')
# except ZeroDivisionError:
#     print('error1')
# except Exception:
#     print('其他异常')
# print('123')

import os


# # 这里有个小坑，open如果由于权限不足报错被try-except 捕获，到最后的finally 会报错(文件压根没打开)
# try:
#     fd = open('read.txt', 'w', encoding='utf-8')
#     fd.write("yeye")
#     fd.write("ysys")
#     fd.write([1, 2, 3])
# except Exception as e:
#     print(e.args)
# else:
#     print("没有异常")
# finally:
#     # 最后一定要确保执行的代码
#     fd.close()
#     print("关闭文件蟹蟹使用")

# def test01():
#     print("test1开始")
#     print(aa)
# def test02():
#     print("test2开始")
#     test01()
#     print("test2结束")
# def test03():
#     print("test3开始")
#     try:
#         test02()
#     except:
#         pass
#     print("test3结束")
# test03()


# class GenderException(Exception):
#     def __init__(self):
#         super().__init__()
#         self.errMsg = "性别只能设置男和女"
#
# class student():
#     def __init__(self, name, gender):
#         self.name = name
#         self.setGener(gender)
#     def setGener(self, gender):
#         if gender == '男' or gender == '女':
#             self.__gender = gender
#         else:
#             raise GenderException()
#     def getGender(self):
#         return self.__gender
#     def showInfo(self):
#         print("name = %s, gender = %s" % (self.name, self.__gender))
# try:
#     stu = student("学生1", '123')
#     stu.showInfo()
# except Exception as e:
#     print(type(e))
#     print(e.errMsg)

# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#     def setAge(self, age):
#         if isinstance(age, int):
#             self.__age = age
#         else:
#             raise TypeError("类型错误")
#     def getAge(self):
#         return self.__age
#     age = property(getAge, setAge)
#
# s1 = Student("ysy", 18)
# s1.age = 19
# print(s1.age)
import pymysql

sql = """select * from food where fid = 1"""
conn = pymysql.connect(host='localhost', user='root', passwd='123456', database='foodserver', charset='utf8')

cursor = conn.cursor()
cursor.execute(sql)

data = cursor.fetchone()

print(type(data))
print(data)

conn.close()




