import serial
import threading
import time

class SerialMonitor:
    def __init__(self,port,baudrate):
        #self.ser = serial.serial_for_url("loop://",timeout=1)
        self.port=port
        self.baudrate=baudrate
        self.closing = False
        self.sleeptime=0.00005

    def start(self):
        self.closing = True
        self.ser = serial.Serial(self.port,self.baudrate)
        self.th=threading.Thread(target=self._receive)
        self.th.start()

    def stop(self):
        self.closing = False
        self.th.join()
        self.ser.close()

    def _receive(self):
        self.data=""
        while self.closing:
            self.data+=str(self.ser.readline())
            time.sleep(self.sleeptime)
