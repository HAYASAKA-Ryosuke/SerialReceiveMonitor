import serial
import threading
import time
import datetime


class SerialMonitor:

    def __init__(self, port, baudrate):
        #self.ser = serial.serial_for_url("loop://",timeout=1)
        self.port = port
        self.baudrate = int(baudrate)
        self.closing = False
        self.sleeptime = 0.00005

    def start(self, datetimeadd=False):
        self.datetimeadd = datetimeadd
        self.closing = True
        self.ser = serial.Serial(self.port, self.baudrate)
        self.th = threading.Thread(target=self._receive)
        self.th.start()

    def stop(self):
        self.closing = False
        self.th.join()
        self.ser.close()

    def _receive(self):
        self.data = ""
        while self.closing:
            if self.datetimeadd:
                dtnow = datetime.datetime.now()
                timeinfo = str(dtnow.hour)+":"+str(dtnow.minute)+":"+str(dtnow.second)+"."+str(dtnow.microsecond)
                self.data += timeinfo+","+str(self.ser.readline())
            else:
                self.data += str(self.ser.readline())
            time.sleep(self.sleeptime)

    def datapop(self):
        data = self.data
        self.data = ""
        return data
