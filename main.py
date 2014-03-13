# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
import config
import datetime
import ADReceived


class sampleWidget(Widget):
    labelstatus = ObjectProperty(None)
    buttonADEnable = ObjectProperty(None)
    textAD = ObjectProperty(None)


class MyApp(App):

    def buttonADEnable_clicked(self, src):
        if self.root.buttonADEnable.text == "start":
            self.root.buttonADEnable.text = "stop"
            self.adrecv.open()
            self.adrecv.receive()
            #self.adrecv.open()
        else:
            self.root.buttonADEnable.text = "start"
            self.adrecv.close()

    def build(self):
        self.root = sampleWidget()
        self.root.buttonADEnable.bind(on_press=self.buttonADEnable_clicked)
        self.conf = config.ConfigRead().read()
        self.adport = self.conf['ADPort']
        self.baudrate = self.conf['BaudRate']
        self.adrecv = ADReceived.SerialMonitor(self.adport,self.baudrate)

        return self.root

if __name__ == '__main__':
    MyApp().run()
