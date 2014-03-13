import serial
import unittest
import io

class SerialMonitorTest(unittest.TestCase):
    def testSerial(self):
        sm = SerialMonitor('loop://',38400)
        ser = serial.serial_for_url('loop://',timeout=1)
        sio = io.TextIOWrapper(io.BufferedRWPair(sm,ser))
        sio.write(unicode("hello\n"))
        sio.flush() # it is buffering. required to get the data out *now*
        #hello = sio.readline()
        #print hello == unicode("hello\n")
unittest.main()
