__author__ = 'jawaad'
from unittest import TestCase, TextTestRunner, TestProgram, TestResult
import random
import time
import types


class webSocketJsonTestResult(TestResult):
    """
    A class that uses the limited IO interface provided by the Tornado websocket class
    and returns information in the JSON format.

    Tornado's websockets only have "write_message" and "close" available.

    """
    separator1 = '=' * 70
    separator2 = '-' * 70

    def __init__(self, stream, descriptions, verbosity):
        TestResult.__init__(self)
        self.stream = stream
        self.showAll = verbosity > 1
        self.dots = verbosity == 1
        self.descriptions = descriptions

    def getDescription(self, test):
        if self.descriptions:
            return test.shortDescription() or str(test)
        else:
            return str(test)

    def startTest(self, test):
        TestResult.startTest(self, test)
        if self.showAll:
            self.stream.write_message(self.getDescription(test))
            self.stream.write_message(" ... ")

    def addSuccess(self, test):
        TestResult.addSuccess(self, test)
        if self.showAll:
            self.stream.write_message("ok")
        elif self.dots:
            self.stream.write_message('.')

    def addError(self, test, err):
        TestResult.addError(self, test, err)
        if self.showAll:
            self.stream.write_message("ERROR")
        elif self.dots:
            self.stream.write_message('E')

    def addFailure(self, test, err):
        TestResult.addFailure(self, test, err)
        if self.showAll:
            self.stream.write_message("FAIL")
        elif self.dots:
            self.stream.write_message('F')

    def printErrors(self):
        if self.dots or self.showAll:
            self.stream.write_message("")
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            self.stream.write_message(self.separator1)
            self.stream.write_message("%s: %s" % (flavour, self.getDescription(test)))
            self.stream.write_message(self.separator2)
            self.stream.write_message("%s" % err)


class webSocketJsonTestRunner(TextTestRunner):

    def makeResult(self):
        return webSocketJsonTestResult(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        """Run the given test case or test suite."""
        result = self.makeResult()
        startTime = time.time()
        test(result)
        stopTime = time.time()
        timeTaken = stopTime - startTime
        result.printErrors()
        self.stream.write_message(result.separator2)
        run = result.testsRun
        self.stream.write_message("Ran %d test%s in %.3fs" %
                            (run, run != 1 and "s" or "", timeTaken))
        self.stream.write_message("")
        if not result.wasSuccessful():
            output = "FAILED ("
            failed, errored = map(len, (result.failures, result.errors))
            if failed:
                output += "failures=%d" % failed
            if errored:
                if failed:
                    output += ", "
                output += "errors=%d" % errored
            output += ")"
            self.stream.write_message(output)
        else:
            self.stream.write_message("OK")
        return result


class unittestWebSocketTestProgram(TestProgram):
    def runTests(self):
        if isinstance(self.testRunner, (type, types.ClassType)):
            try:
                testRunner = self.testRunner(verbosity=self.verbosity)
            except TypeError:
                # didn't accept the verbosity argument
                testRunner = self.testRunner()
        else:
            # it is assumed to be a TestRunner instance
            testRunner = self.testRunner
        testRunner.run(self.test)

