__author__ = 'jawaad'
from unittest import TestCase, TextTestRunner, TestProgram, TestResult
import tornado
import tornado.websocket
import tornado.httpserver
import random
import time
import types



application = tornado.web.Application([
    (r'/tests', unittestWebSocketHandler),
])


if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(169)
    tornado.ioloop.IOLoop.instance().start()
