import serial
import thread


class SerialMonitor:

    def __init__(self,port,baudrate):
        self.ser = serial.Serial(port,baudrate)
        #self.ser = serial.serial_for_url(port,timeout=1)

    def open(self):
        self.ser.open()

    def close(self):
        self.ser.close()

    def _receive(self):
        readbuffer = ''
        while True:
            readbuffer += self.ser.read(self.ser.inWaiting() or 1)
            if '\n' in readbuffer:
                print self.readbuffer.rstrip()
                readbuffer = ""

    def receive(self):
        thread.start_new_thread(self._receive)
