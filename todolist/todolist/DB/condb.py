#coding=utf-8
__author__ = 'Administrator'
import pymysql
import pymysql.cursors


def dec_make_conn_cursor():
    conn=pymysql.connect(host="localhost",user="root",passwd="root",db="todolist",cursorclass = pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tolist" )
    data = cursor.fetchall()
    conn.close()

    return  data

print (dec_make_conn_cursor())



def dele_id(id):
    conn=pymysql.connect(host="localhost",user="root",passwd="root",db="todolist",cursorclass = pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    sql="""delete  FROM tolist where  id =%s"""
    cursor.execute(sql,(id))
    conn.commit()
    return

def add_conten(name):

    conn=pymysql.connect(host="localhost",user="root",passwd="root",db="todolist",cursorclass = pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    sql="""INSERT into tolist (name,is_done) value(%s,'doing')"""
    cursor.execute(sql,(name))
    conn.commit()
    return


