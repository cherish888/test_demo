#!/usr/bin/python
# -*- coding: UTF-8 -*-
from connect import session
from module import User

#增
def add_user():
    person = User(name='cherish002',password='686868')
    session.add(person) #增加单个
    # session.add_all(
    #     [
    #         User(name='memeda',password='111111'),
    #         User(name='lalala',password='112233aa'),
    #         User(name='hahaha',password='qq123456'),
    #     ]
    # )   #增加多个
    session.commit()    #提交
    print(person,'增加成功~')
#查
def search_user():
    rows = session.query(User).all()
    print(rows,'查询成功')

#改
def update_user():
    row = session.query(User).filter(User.name=='cherish').update({User.password:123})
    session.commit()
    print(row,'修改成功~')

#删
def delete_user():
    row = session.query(User).filter(User.name=='learn tornado').delete()
    session.commit()
    print(row,'删除成功~')


if __name__ == '__main__':
    add_user()
    # search_user()
    # update_user()
    # delete_user()