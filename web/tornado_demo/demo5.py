#!/usr/bin/python
# -*- coding: UTF-8 -*-
from connect import session
from module import User
from sqlalchemy import desc
from sqlalchemy import func,extract
from sqlalchemy import or_
from sqlalchemy import distinct


# print(session.query(User).filter_by(name='learn').all())
# print((session.query(User)).filter(User.name.like('h%')).all())
# print((session.query(User)).filter(User.name.notlike('h%')).all())
# print((session.query(User)).filter(User.password.in_
#                                    (['123','qq123456'])).all())
# print((session.query(User)).filter(User.password.notin_
#                                    (['123','qq123456'])).all())
# print((session.query(User)).filter(User.password.is_(None)).all())
# print((session.query(User)).filter(User.password.isnot(None)).all())
# print((session.query(User)).limit(2).all()) #限制查询条数
# print((session.query(User)).offset(3).all())    #偏移
# print((session.query(User)).slice(2,7).all())   #切片
# print((session.query(User)).filter(User.name=='cherish').one()) #查询唯一数据
# print((session.query(User)).order_by(desc(User.id)).all())  #降序
# print(session.query(User.password,func.count("*"))
#       .group_by(User.password).all())   #分组统计
# print(session.query(extract('minute',User.creatime).label('minute'),
#                     func.count("*")).group_by('minute').all())
print(session.query(User.name).filter(or_(User.name.isnot(None),User.password=='123')).all())