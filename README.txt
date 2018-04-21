# Steps to run and test AsyncServer and TwsitedServer

# AsyncServer:
    AsyncServer is a simple serve which handles the request and respond to clinet.
    It reverse the message send by sender and send it back.
    It also send error string, if message does not follow the message limitations.

    To Run:
    Run the below command with tcp port where you want to run:
    python AsyncServer.py 8080

# TwsitedServer:
    Twister server is a simple server created with Twisted Module
    It reverse the message send by sender and send it back.
    It also send error string, if message does not follow the message limitations.

    To Run:
	1. Need to install Twisted as it is a different module
	2. install python pip
	3. command to install: pip install twisted[tls]
    Now, Run the below command with tcp port where you want to run:
    python AsyncServer.py 8081

# To Run Test:
    Please Run the ServerTest.py file
    Now in set up method, numberOfThread is set to 100, please change if need to test with more threads
	Also, please change the host and tcpPort in ServerTest.py file where server is running, eg - 8081.
	To run test:
	ServerTest.py -v
	
    There are 4 tests:
    1. Test with No Connection (Connection Refused)
    2. Server should repond with reversed request message
    3. Request without Header i.e. Without first 4 digits should throw an exception
    4. Request with more than 30 character should throw an exception

Source Files:
AsyncServer.py
TwsitedServer.py
customRequestParser.py
ClientThread.py
ServerTest.py

Please download the files to a location and though terminal reach to that location.
Once reached, please run the server and test as mentioned above.

Note: Program have been written according to python 2.7, please use python 2.7 environment to run.
