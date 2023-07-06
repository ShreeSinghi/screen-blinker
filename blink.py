# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 10:52:29 2023

@author: Shree
"""
import sys
import time

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QDesktopWidget


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint |
                            QtCore.Qt.WindowStaysOnTopHint |
                            QtCore.Qt.X11BypassWindowManagerHint)

        self.label = QLabel("blink!", self)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 40px; color: black;")

        font = QFont("Century Gothic", 40, QFont.Bold)
        self.label.setFont(font)
        
        ########### center window ############
        frame_geo = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geo.moveCenter(center_point)
        self.setGeometry(frame_geo)
        label_geo = self.label.geometry()
        label_geo.moveCenter(self.rect().center())
        self.label.setGeometry(label_geo)
        ######################################

        self.setWindowState(QtCore.Qt.WindowNoState)

        self.flashing_timer = QtCore.QTimer(self)
        self.flashing_timer.timeout.connect(self.flash_fullscreen)
        self.flashing_timer.start(5000)  # flash every 5 seconds
        self.flashing_duration = 100  # duration of flashing in milliseconds


    def flash_fullscreen(self):
        self.setWindowOpacity(1.0)
        self.label.show()
        QtWidgets.qApp.processEvents()
        time.sleep(self.flashing_duration / 1000)
        self.label.hide()
        self.setWindowOpacity(0.0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MainWindow()
    mywindow.setWindowOpacity(0.0)
    mywindow.show()
    sys.exit(app.exec_())
