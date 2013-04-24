__author__ = 'jawaad'

from pytestsocket.wsserver import *
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options


tornado.options.options['log_file_prefix'].set('./log/server.log')
tornado.options.options['logging'].set('info')
tornado.options.parse_command_line()
application = tornado.web.Application([
    (r'/tests', unittestWebSocketHandler),
])

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(1690)
tornado.ioloop.IOLoop.instance().start()
