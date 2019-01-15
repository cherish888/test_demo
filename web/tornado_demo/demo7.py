#!/usr/bin/python
# -*- coding: UTF-8 -*-
from connect import session
from module import User,UserDetails,Article

if __name__ == '__main__':
    #一对一
    row = session.query(User).get(1)
    # print(row,dir(row))
    # print(row.name,row.details)
    row1 = session.query(UserDetails).get(2)
    # print(row1)
    # print(row1.userdetails)

    #多对多
    row2 = session.query(User).get(1)
    # print(row2)
    print(row2.article)

    row3 = session.query(Article).get(2)
    print(row3.article_user)