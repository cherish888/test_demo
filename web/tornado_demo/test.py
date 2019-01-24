#!/usr/bin/python
# -*- coding: UTF-8 -*-

from connect import session
from module import  Student

def add():
    stu = Student(name='么么踹',age='18',sex='男',address='上海市浦东新区')
    session.add(stu)
    session.commit()
    print('新增记录成功~')


def search():
    stu = session.query(Student).filter(Student.name=='么么踹').all()
    print(stu)


def  update():
    stu = session.query(Student).filter(Student.name=='么么踹').update({Student.age:'20'})
    session.commit()
    print(stu)


def delete():
    stu = session.query(Student).filter(Student.name=='么么踹').delete()
    session.commit()
    print(stu,'删除么么踹成功~')


if __name__ == '__main__':
    # add()
    search()
    # update()
    # delete()