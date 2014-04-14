# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import config
import datetime
import ADReceived
import threading


class sampleWidget(Widget):
    labelstatus = ObjectProperty(None)
    buttonADEnable = ObjectProperty(None)
    textAD = ObjectProperty(None)


class MyApp(App):

    def outputtext(self):
        while self.thflag:
            # self.root.textAD.text+=str(self.adrecv.data)
            data = self.adrecv.datapop()
            f = open(self.filename, 'a')
            f.writelines(data)
            self.root.textAD.text += data
            f.close()
            # print(self.adrecv.data)

    def buttonADEnable_clicked(self, src):
        if self.root.buttonADEnable.text == "Start":
            self.root.buttonADEnable.text = "Stop"
            dtnow = datetime.datetime.now()
            self.filename = str(dtnow.month)+'-'+str(dtnow.day)+'-'+str(dtnow.hour)+'-'+str(dtnow.minute)+'-'+str(dtnow.second)+'-'+str(dtnow.microsecond)+'.csv'
            self.adrecv.start(datetimeadd=True)
            self.th = threading.Thread(target=self.outputtext)
            self.thflag = True
            self.th.start()
        else:
            self.root.buttonADEnable.text = "Start"
            self.adrecv.stop()
            self.thflag = False
            self.th.join()

    def build(self):
        self.root = sampleWidget()
        self.root.buttonADEnable.bind(on_press=self.buttonADEnable_clicked)
        self.conf = config.ConfigRead().read()
        self.adport = self.conf['ADPort']
        self.baudrate = self.conf['BaudRate']
        # self.adrecv = ADReceived.SerialMonitor(self.adport,self.baudrate)
        self.adrecv = ADReceived.SerialMonitor("/dev/tty.usbserial", 38400)

        return self.root

if __name__ == '__main__':
    MyApp().run()
