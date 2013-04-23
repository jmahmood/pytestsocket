pytestsocket
============

Version: 0.1

A Python websocket server that allows you to run, cancel, and re-run unittests.

Dependencies
============
Tornado Server


How?
====
1. Run server
    python ./pytestsocket
2. Prep an HTML page that can send/receive messages from the server. (/example/index.html)
3. Click "Run All Tests".


Why?
====

At the company I work for, I do API designs, while a foreign team develops them.  There are multitude of possible issues that can come into the picture between our servers in Japan and their servers in the US.  Thus, we run tests at both ends of the pipe.

Having to log into our machines and run unit tests seems rather ludicrous in 2013.  Also, it seems much easier to actually show the test code with highlighting-enabled in the browser for people who are not using an IDE that has python buit-in.


Process
=======
- A user visits the internal website (http://internal-tests)
- This internal website offers a "Run Tests", with real-time output of tests as they run.
- The test results are output in the window.

Version
=======
Current: _0.1_

Roadmap
=======
- 0.2: Cancelling tests
- 0.3: Output results in JSON format instead of as pure text.
