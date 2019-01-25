#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define,options


define('port',default=8000,help='run port',type=int)


class SetHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_cookie('cookie','this_is_cookie')#有效期为访问到关闭
        self.set_cookie('cookie1','this_is_cookie1',expires=time.time()+60)#有效期60秒
        self.set_cookie('cookie2','this_is_cookie2',expires_days=1,path='/set/aaa')#有效期1天
        self.set_cookie('cookie3','this_is_cookie3',httponly = True)#设置无法被JS获取cookie
        self.set_cookie('cookie4','this_is_cookie4',max_age = 120,expires=time.time()+60)
        self.set_secure_cookie('cookie5','this_is_cookie5')#cookie内容加密
        self.write('set_cookie')

class GetHandler(tornado.web.RequestHandler):
    def get(self):
        a = self.get_cookie('cookie')
        print(a)
        self.write('get_cookie')


application = tornado.web.Application(
    handlers=[
        (r"/set",SetHandler),
        (r"/get",GetHandler),
    ],
    # template_path='templates',
    cookie_secret = 'abcdefg',
    debug=True
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()