__author__ = 'jawaad'

from pytestsocket.wsserver import *
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options

tornado.options.parse_config_file("test_server.conf")
tornado.options.parse_command_line()
application = tornado.web.Application([
    (r'/tests', unittestWebSocketHandler),
])

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(1690)
tornado.ioloop.IOLoop.instance().start()
