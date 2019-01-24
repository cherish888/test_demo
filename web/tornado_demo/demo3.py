#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from connect import session
from module import User
from tornado.options import define,options


define('port',default=8000,help='run port',type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # time.sleep(3)
        self.render('demo_3-1.html')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        pwd = self.get_argument('password')
        user = User.by_name(name)
        if user and user.password == pwd:
            self.render('demo_3-2.html',name=name,)
        else:
            self.write('用户名或密码错误~')


class CreatUser(tornado.web.RequestHandler):
    def get(self):
        self.render('demo_3-3.html')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        pwd = self.get_argument('password')
        new_user = User(name=name,password=pwd)
        session.add(new_user)
        session.commit()
        self.write('新增用户成功~')

class DeleteUser(tornado.web.RequestHandler):
    def get(self):
        self.render('demo_3-4.html')

    def post(self, *args, **kwargs):
        user_id = self.get_argument('id')
        delete_user = session.query(User).filter(User.id==user_id).delete()
        if delete_user:
            session.commit()
            self.write('删除用户成功')
        else:
            self.write('没有该用户，无需删除!')


application = tornado.web.Application(
    handlers=[
        (r"/main",IndexHandler),
        (r"/add",CreatUser),
        (r"/delete",DeleteUser),
],
template_path= 'templates',
debug=True
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()