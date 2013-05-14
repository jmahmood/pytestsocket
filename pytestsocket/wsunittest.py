__author__ = 'jawaad'
from unittest import TextTestRunner, TestProgram, TestResult, defaultTestLoader
import types
from helpers import wstiming


class webSocketTestResult(TestResult):
    """
    A class that uses the limited IO interface provided by the Tornado websocket class
    and returns information in the text format.

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


class webSocketTestRunner(TextTestRunner):

    def makeResult(self):
        return webSocketTestResult(self.stream, self.descriptions, self.verbosity)

    def output(self, result):
        result.printErrors()
        self.stream.write_message(result.separator2)
        run = result.testsRun
        self.stream.write_message("Ran %d test%s" % (run, run != 1 and "s" or ""))
        self.stream.write_message("")
        if not result.wasSuccessful():
            output = "FAILED ("
            failed, error_generated = map(len, (result.failures, result.errors))
            if failed:
                output += "failures=%d" % failed
            if error_generated:
                if failed:
                    output += ", "
                output += "errors=%d" % error_generated
            output += ")"
            self.stream.write_message(output)
        else:
            self.stream.write_message("OK")

    def run(self, test):
        """Run the given test case or test suite."""
        result = self.makeResult()

        with wstiming(self.stream):
            test(result)

        self.output(result)
        return result


class unittestWebSocketTestProgram(TestProgram):

    def __init__(self, module='__main__', defaultTest=None,
                 argv=None, testRunner=TextTestRunner,
                 testLoader=defaultTestLoader):
        """Augments the original init by reloading the test module when you re-run a test.
        This will be helpful for situations when you have a new """
        if isinstance(module, type(types)):
            # This confirms that the module is loaded and in memory.
            # Under that circumstance, you must force reload the module
            # This allows us to have dynamic test modules without rebooting
            # the server (IE: upload & automatically works)
            self.module = reload(module)
        super(unittestWebSocketTestProgram, self).__init__(module, defaultTest, argv, testRunner, testLoader)

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

