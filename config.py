# -*- coding: utf-8 -*-

import ConfigParser

class ConfigRead(object):

    def __init__(self):
        config = ConfigParser.SafeConfigParser()
        config.read('config.ini')
        self.adport= config.get('ADSerialMonitor', 'ADPort')
        self.baudrate= config.get('ADSerialMonitor', 'BaudRate')

    def read(self, param=None):
        if param == 'ADPort':
            return self.adport
        if param == 'BaudRate':
            return self.baudrate
        if param is None:
            return {'ADPort': self.adport, 'BaudRate': self.baudrate}
