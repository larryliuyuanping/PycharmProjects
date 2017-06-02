# -*- coding:utf-8 -*-

#请实现一个学生的类，有学号，有姓名，有年龄，以及成绩（100分）等私有属性，
# 并且实现一个公有的对象方法，get_level()，如果学员成绩大于等于80，
# 则返回“优等生”，小于80大于等于60，则返回“中等生”，小于60，则返回“差等生”

class Student2():
    id = 0
    name = ""
    english = 0



class Student():

    def __init__(self,id,name,age,score):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__score = score

    def set_level(self,score):
        self.__score = score
    def get_level(self):

        if self.__score >= 80:
            return "优等生"
        elif self.__score < 80 and self.__score >= 60:
            return "中等生"
        else:
            return "差等生"

stu1 = Student(1,"张三",18,90)
stu2 = Student(2,"李四",20,50)
stu3 = Student(3,"王五",30,70)

print(stu1.get_level())
print(stu2.get_level())
print(stu3.get_level())
