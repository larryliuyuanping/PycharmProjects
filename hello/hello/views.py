#coding=utf-8
__author__ = 'Administrator'
from django.shortcuts import  render



stu1 = {'id':'1','name': '张三', 'password': '111111111', 'age': '18', 'class': 'python'}
stu2 = {'id':'2','name': '李四', 'password': '222222222', 'age': '18', 'class': 'python'}
stu3 = {'id':'3','name': '王五', 'password': '333333333', 'age': '18', 'class': 'python'}
stu4 = {'id':'4','name': '来瓶', 'password': '44444444444', 'age': '18', 'class': 'python'}
stu_list = [stu1, stu2, stu3, stu4]



def login(request):

    print("a")
    name=(request.GET.get('username'))
    print(name)
    password=(request.GET.get('password'))
    context={'name':name,'password':password}



    return render(request, 'login.html',context,)



def stu_dele(request):
    print 111
    id=(request.GET.get('id'))

    for stu in stu_list :
        if (stu['id']==id):
            stu_list.remove(stu)
        context = {
            "stu_list": stu_list
        }
    return render(request, 'student_list.html',context)


def stu(request):

    print 22222
    context={
        "stu_list": stu_list
    }
    return render(request, 'student_list.html',context)