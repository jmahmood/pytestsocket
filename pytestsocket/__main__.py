from wsserver import *
import tornado.httpserver


class TestSequenceFunctions(TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

application = tornado.web.Application([
    (r'/tests', unittestWebSocketHandler),
])

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(1690)
tornado.ioloop.IOLoop.instance().start()
