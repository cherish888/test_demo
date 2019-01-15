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



application = tornado.web.Application(
    handlers=[
        (r"/main",IndexHandler),
],
template_path= 'templates',
debug=True
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()