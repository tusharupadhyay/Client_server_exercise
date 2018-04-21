""" Test class to test AsyncServer and TwistedServer"""

import unittest
from clientThread import (ClientThread, InncorectResponseFromServerError)
import threading
import sys

"""
Test Plan
1. No Connection
2. Server should repond with reversed request message
3. Request without Header i.e. Without first 4 digits should throw an exception
4. Request with more than 30 character should throw an exception
"""

class ServerTest(unittest.TestCase):

    def setUp(self):
        self.numberOfThreads = 100
		self.tcpHost = 'localhost'
		self.tcpPort = 8081
		self.nonWorkingTcpPort = 8082
        pass

    def tearDown(self):
        main_thread = threading.current_thread()
        for t in threading.enumerate():
            if t is main_thread:
                continue
            """ Joining all threads so that no threads stay hanging"""
            t.join()

    def test_connectionRefuse(self):
        """Create client with wrong servername/port to get Connection exception"""
        threadName = "Thread_1"
        thread = ClientThread(threadName, "1010 Hello from " + threadName, self.tcpHost, self.nonWorkingTcpPort)
        with self.assertRaises(InncorectResponseFromServerError) as exp:
            thread.startProcess()
        err= exp.exception
        self.assertIsNotNone(err)
        self.assertIn('Connection refuse', err.message, 'Connection Refused exception was thrown')

    def test_ResponseReversedEquals(self):
        """ This test should not throw any expection as passed message meets criteria """
        threads = []
        for i in range(self.numberOfThreads):
            threadName = "Thread_" + str(i)
            threads.append(ClientThread(threadName, str("1010 Hello from " + threadName), self.tcpHost, self.tcpPort))

        for thread in threads:
            thread.startProcess()
        

    def test_MessageWithoutDigitsPrefixed(self):
        """ This method should throw an exception as message doesn't contain 4 digits at front of message """
        threads = []
        for i in range(self.numberOfThreads):
            threadName = "Thread_" + str(i)
            threads.append(ClientThread(threadName, "Hello from " + threadName, self.tcpHost, self.tcpPort))

            with self.assertRaises(InncorectResponseFromServerError) as exp:
                for thread in threads:
                    thread.startProcess()
            err= exp.exception
            self.assertIsNotNone(err)
            self.assertIn('BAD REQUEST 4 DIGIT MISSING', err.message, 'BAD REQUEST 4 DIGIT MISSING exception')


    def test_MessageGreaterThanMaxAllowed(self):
        """ This method should throw an exception as message exceeds the limit(30) """
        threadName = "Thread_1"
        messageToSend = "1111 " * 10
        thread = ClientThread(threadName, messageToSend, self.tcpHost, self.tcpPort)
        with self.assertRaises(InncorectResponseFromServerError) as exp:
            thread.startProcess()
        err= exp.exception
        self.assertIsNotNone(err)
        self.assertIn('REQUEST EXCEED MAX ALLOWED', err.message, 'REQUEST EXCEED MAX ALLOWED')


if __name__ == "__main__":
    unittest.main()