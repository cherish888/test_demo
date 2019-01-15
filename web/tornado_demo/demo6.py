#!/usr/bin/python
# -*- coding: UTF-8 -*-
from connect import session
from module import User,UserDetails

# print(session.query(User,UserDetails).all())
# print(session.query(User.name,UserDetails.lost_login).join(UserDetails,UserDetails.id==User.id).all())
# print(session.query(User.name,UserDetails.lost_login).outerjoin(UserDetails,UserDetails.id==User.id).all())
q1 = session.query(User.id)
q2 = session.query(UserDetails.id)
# print(q1.union(q2).all())

sql_0 = session.query(UserDetails.lost_login).subquery()
# print(session.query(User,sql_0.c.lost_login).all())

#原生sql查询
sql_1 = """
select * from `user`
"""
rows = session.execute(sql_1)
# print(rows,dir(rows))
# print(rows.fetchone())
# print(rows.fetchmany())
# print(rows.fetchall())
for i in rows:
    print(i)
