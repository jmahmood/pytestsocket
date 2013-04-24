import time


class wstiming:
    def __init__(self, stream):
        self.stream = stream

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, type, value, traceback):
        end = time.clock()
        elapsed_time = (end - self.start) / 1000
        self.stream.write_message("Elapsed Time: %.2f" % elapsed_time)
