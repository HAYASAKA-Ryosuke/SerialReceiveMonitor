import serial
import unittest
import io
import ADReceived
import time

class SerialMonitorTest(unittest.TestCase):
    def testSerial(self):
        s1 = ADReceived.SerialMonitor("/dev/tty.usbserial",38400)
        s1.start()
        time.sleep(1.5) 
        print(s1.data)
        s1.stop()
        s1.start()
        time.sleep(1.5) 
        print(s1.data)
        s1.stop()
unittest.main()
