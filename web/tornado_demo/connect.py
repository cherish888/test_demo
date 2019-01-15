#!/usr/bin/python
# -*- coding: UTF-8 -*-

from sqlalchemy import create_engine

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'tornado'
USERNAME = 'root'
PASSWORD = '123456'

db_url = 'mysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

engin = create_engine(db_url)

#创建数据库表
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(engin)

#使用数据库表
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engin)
session = Session()

if __name__ == '__main__':
    connection = engin.connect()
    print(connection,'连接成功~')