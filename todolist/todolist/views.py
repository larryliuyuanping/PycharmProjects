#coding=utf-8
__author__ = 'Administrator'
from django.shortcuts import  render
import todolist.DB.condb

from todolist.DB.condb import dec_make_conn_cursor
from todolist.DB.condb import dele_id


from django.core.urlresolvers import reverse
from django.http import HttpResponse
# def login(request):
#
#     print("a")
#     name=(request.GET.get('username'))
#     print(name)
#     password=(request.GET.get('password'))
#     context={'name':name,'password':password}
#
#     return render(request, 'login.html',context,)



def list_dele(request):
    print ( 111)
    id=int((request.GET.get('id')))

    print ('aaaaaaaaa')
    if id >0:
        Resutl=dele_id(id)

    todo_list = dec_make_conn_cursor()
    contect = {
    'todo_list': todo_list

    }


    return render(request, 'todo.html', contect)


def list_add(request):
    print ( 111)
    name=(request.GET.get('lname'))
    if name !=None:
        todolist.DB.condb.add_conten(name)
        todo_list = dec_make_conn_cursor()

        contect = {
            'todo_list': todo_list

        }
        print(contect)

    return render(request, 'todo.html', contect)


def todo_list(request):

    todo_list=dec_make_conn_cursor()

    contect={
        'todo_list':todo_list

    }
    print(contect)

    return render(request, 'todo.html',contect)


def get_back_url(request,check_url):

    referer = request.META.get('HTTP_REFERER')
    if check_url in referer:
        return  referer
    else:
        return check_url
