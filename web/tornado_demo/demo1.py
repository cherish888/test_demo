#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
from tornado.options import define,options


define('port',default=8000,help='run port',type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('cherish')
        self.write('<br>')
        self.write(b'python')
        self.write('<br>')
        self.flush()
        toto = {
            'a':1,
            'b':2,
            'c':3,
            'li':['puthon','php','java']
        }
        self.write(toto)
class InoutHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name','no')
        self.write(name)
        name1 = self.get_arguments('name')
        print(name)

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        password = self.get_argument('password')
        self.write('姓名是：{},密码是：{}'.format(name,password))

class TemHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('demo_1.html')


class RecHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(3)
        self.redirect('/tem')

class ReqHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(self.request.remote_ip)
        print(self.request.remote_ip)
        print(self.request.full_url())
        print(self.request.request_time())

class UserHandler(tornado.web.RequestHandler):
    def get(self,name,age):
        self.write('name:{},age:{}'.format(name,age))

class StudentHandler(tornado.web.RequestHandler):
    def get(self,name,age,sex):
        self.write('name:{},age:{},sex:{}'.format(name,age,sex))


application = tornado.web.Application(
    handlers=[
        (r"/main",MainHandler),
        (r"/get",InoutHandler),
        (r"/tem",TemHandler),
        (r"/rec",RecHandler),
        (r"/req",ReqHandler),
        (r"/user/(.+)/([0-9]+)",UserHandler),
        (r"/stu/(?P<name>[a-zA-Z]+)/(?P<age>[1-9]+)/(?P<sex>[a-zA-z]+)",StudentHandler),
],
template_path= 'templates',
debug=True
)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()