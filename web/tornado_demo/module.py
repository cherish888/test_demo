#!/usr/bin/python
# -*- coding: UTF-8 -*-
from sqlalchemy import Column,Integer,String,DateTime,Boolean,ForeignKey,Table
from sqlalchemy.orm import relationship
from connect import Base,session
from datetime import datetime

class User(Base):
    __tablename__ = 'user'  #固定语法
    id = Column(Integer,primary_key=True,autoincrement=True)    #primary_key:主键 autoincrement:自增长
    name = Column(String(20),nullable=False)    #nullable:非空
    password = Column(String(50))
    creatime = Column(DateTime,default=datetime.now)
    _locked = Column(Boolean,default=False,nullable=False)

    @classmethod
    def by_name(cls,name):
        return session.query(cls).filter(cls.name==name).first()

    def __repr__(self):
        return 'User(id=%s,name=%s,password=%s,creatime=%s,_locked=%s)'%(
            self.id,
            self.name,
            self.password,
            self.creatime,
            self._locked
        )

class UserDetails(Base):
    __tablename__ = 'user_details'
    id = Column(Integer,primary_key=True,autoincrement=True)
    id_card = Column(Integer,nullable=ForeignKey,unique=True)
    lost_login = Column(DateTime)
    login_num = Column(Integer,default=0)
    user_id = Column(Integer,ForeignKey('user.id'))

    #声明表关系
    userdetails = relationship('User',backref='details',uselist='False',cascade='all')

    def __repr__(self):
        return 'User(id=%s,id_card=%s,lost_login=%s,login_num=%s,user_id=%s)'%(
            self.id,
            self.id_card,
            self.lost_login,
            self.login_num,
            self.user_id
        )

user_article = Table('user_article',Base.metadata,
                     Column('user_id',Integer,ForeignKey('user.id'),primary_key=True),
                     Column('article_id',Integer,ForeignKey('article.id'),primary_key=True)
                     )

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    content = Column(String(500),nullable=True)
    creat_time = Column(DateTime,default=datetime.now)

    def __repr__(self):
        return "article(id:%s,content:%s,creat_time:%s)"%(
            self.id,
            self.content,
            self.creat_time
        )

    article_user = relationship('User',backref='article',secondary='user_article')

if __name__ =='__main__':
    Base.metadata.create_all()