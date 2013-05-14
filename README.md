pytestsocket
============

Version: 0.1

A Python websocket server that allows you to run, cancel, and re-run unittests.

Dependencies
============
- Tornado Server
- importlib (For Python < 2.7)

Installation
============
pip install pytestsocket

How?
====
1. Run server
    python ./example/server/server.py
    (Alternatively, import the class and create your own tornado server)
2. Open the example HTML page in your browser (./example/html/index.html)
3. Click "Basic Tests".


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
Current: _0.12_ Enabled dynamic test running

Roadmap
=======
- 0.2: Cancelling tests that are being run
- 0.3: Output results in JSON format instead of as pure text.

License
=======
Simplified BSD License

Copyright (c) 2013, Jawaad Mahmood
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
