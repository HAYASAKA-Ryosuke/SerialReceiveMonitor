# -*- coding: utf-8 -*-

import unittest
import config


class testConfigRead(unittest.TestCase):
    def testread(self):
        con = config.ConfigRead()
        self.assertEqual('/dev/tty.usbserial-A400hMRN', con.read(param='ADPort'))
        self.assertEqual('38400', con.read(param='BaudRate'))
        self.assertEqual('/dev/tty.usbserial-A400hMRN', con.read()['ADPort'])
        self.assertEqual('38400', con.read()['BaudRate'])
unittest.main()
