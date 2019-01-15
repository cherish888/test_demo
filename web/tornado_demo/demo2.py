#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define,options



define('port',default=8000,help='run port',type=int)

class HeaderHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('hello python')
        self.set_header('food','meet')
        self.set_header('fruit','apple')

class AddHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('add hello python')
        self.add_header('aaa','memeda')
        self.add_header('bbb','papaap')
        self.clear_header('ccc')

class ErrorHandler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(404)

    def write_error(self, status_code, **kwargs):
        # self.write('status_code:{}'.format(status_code))
        self.write('<center>你的页面被我吃拉~</center>')
        self.render()

class IndexHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        print('set_default_headers:设置好默认的响应头')

    def initialize(self):
        print('initialize:初始化')

    def prepare(self):
        self.write('prepare:准备工作')

    def get(self):
        self.write('get:处理get请求')

    def post(self, *args, **kwargs):
        self.write('post:处理post请求')

    def write_error(self, status_code, **kwargs):
        print('write_error:处理错误')

    def on_finish(self):
        print('on_finish:结束，释放资源~')

class NotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        self.send_error(404)

    def write_error(self, status_code, **kwargs):
        self.write('<center>你的页面被cherish吃拉~</center>')

application = tornado.web.Application(
    handlers=[
        (r"/header",HeaderHandler),
        (r"/add",AddHandler),
        (r"/error",ErrorHandler),
        (r"/index",IndexHandler),
        (r"/(.*)",NotFoundHandler),
],
template_path= 'templates',
debug=True
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()