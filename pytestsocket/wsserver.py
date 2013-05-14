__author__ = 'jawaad'
import tornado
import tornado.websocket
import logging
import os
import sys

# Used for loading the test module requests we get from the HTML server.
# This is not "secure".  Anything in the imported test file will be executed.
# Why would you let someone have access to your testbed if you want it
# to stay secure?
# TODO: Stop being lame and find a way to make this more secure.
from importlib import import_module
import getopt
from wsunittest import *


def module_exists(module_name):
    #http://stackoverflow.com/questions/5847934/how-to-check-if-python-module-exists-and-can-be-imported
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True


class unittestWebSocketHandler(tornado.websocket.WebSocketHandler):
    """A Tornado websocket server that outputs flat text from incoming test requests."""
    def is_valid_module(self, module):
        # TODO: valid modules should be in a config file or something like that.
        return True

    def open(self):
        logging.info('new connection')
        self.write_message("Hello World")

    def on_message(self, message):
        logging.info('Test Module Message Received: %s' % message)
        module = False
        if module_exists(message) and self.is_valid_module(message):
            logging.info("Module Exists: %s" % message)
            module = message
        elif message == "":
            logging.info("Empty message passed" % message)
            module = "__main__"
        else:
            logging.warning("Could not find module")
            logging.warning(os.path.realpath(__file__))
            logging.warning(sys.path)

        if module:
            # TODO: Reload module if the module has already been loaded. (reload(module))
            # You may pass the port to the server by commandline; this removes it.
            return unittestWebSocketTestProgram(
                module=import_module(module),
                testRunner=webSocketTestRunner(stream=self)
            )

    def on_close(self):
        logging.info('connection closed')