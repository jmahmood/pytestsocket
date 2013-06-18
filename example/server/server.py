__author__ = 'jawaad'

from pytestsocket.wsserver import *
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.options

tornado.options.define("port", default=1690, help="run on the given port", type=int)
tornado.options.parse_config_file("test_server.conf")
tornado.options.parse_command_line()
application = tornado.web.Application([
    (r'/tests', unittestWebSocketHandler),
])

logging.info("starting Tornado web server on port %d" % tornado.options.options['port'])
http_server = tornado.httpserver.HTTPServer(application)

port = tornado.options.options['port']
http_server.listen(int(port))
tornado.ioloop.IOLoop.instance().start()
