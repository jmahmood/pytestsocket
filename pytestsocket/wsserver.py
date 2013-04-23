__author__ = 'jawaad'
import tornado
import tornado.websocket
from wsunittest import *


class unittestWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        self.write_message("Hello World")

    def on_message(self, message):
        print 'message received %s' % message
        return unittestWebSocketTestProgram(
            module="__main__",
            testRunner=webSocketJsonTestRunner(stream=self)
        )

    def on_close(self):
        print 'connection closed'
