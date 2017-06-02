#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Administrator'

import math
# # print (sin(pi/2))
#
# print (math.sin(math.pi/2))
#
#
# a=0
# b=a+1
#
# def test_return(x):
#     if x > 0:
#         return x
#     else:
#         return 0

# if __name__ == '__main__':
#     class student:
#         x = 0
#         c = 0
#     def f(stu):
#         stu.x = 20
#         stu.c = 'c'
#     a= student()
#     a.x = 3
#     a.c = 'a'
#     f(a)
# print( a.x,a.c)

# class Person:
#     def __init__(self):
#         pass
#
#     def getAge(self):
#         print __name__
#
# p = Person()
# p.getAge()

#!/usr/bin/python
dict1 =  {'user':'runoob','num':[1,2,3]}

dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用

# # 修改 data 数据
# dict1['user']='root'
# dict1['num'].remove(1)
#
# # 输出结果
# print(dict1)
# print(dict2)
# print(dict3)
# k=1000
# while k>1:
# 	print k
# 	k = k/2


#!/usr/bin/python
# Filename: func_global.py

#!/usr/bin/python
# Filename: func_global.py
class Person:
    def __init__(self):
        pass

    def getAge(self):
        print __name__

p = Person()
p.getAge()
