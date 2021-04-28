# -*-coding:utf-8-*-


# How to convert ui file to py file:
# pyside2-uic mainwindow.ui -o mainwindow.py

import os
import re
import shutil
import sys
import sttool
import pyperclip
from files import File_Checker
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtGui, QtWidgets, QtCore


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui = sttool.Ui_Dialog()
        self.ui.setupUi(self)
        self.flchck = File_Checker()

######################
        self.ui.get_dest_folder.clicked.connect(self.set_dest_fldr)
        self.ui.get_rsc_folder.clicked.connect(self.set_rsc_fldr)
        self.ui.prpr_btn.clicked.connect(self.prepare)
        self.ui.rplc_btn.clicked.connect(self.rplc_files)
        self.ui.reset_btn.clicked.connect(self.rst_brd)
        self.ui.cp_clpbrd.clicked.connect(self.sent_clp)
#######################

    def set_dest_fldr(self):
        self.flchck.get_dest_fldr(QtWidgets.QFileDialog.getExistingDirectory())

    def set_rsc_fldr(self):
        self.flchck.get_rsc_fldr(QtWidgets.QFileDialog.getExistingDirectory())

    def prepare(self):
        self.flchck.get_files_ready()
        log = self.flchck.generate_log()
        self.ui.mssg_brd.clear()
        self.ui.mssg_brd.append(log)

    def rplc_files(self):
        self.flchck.replace_files()
        self.ui.mssg_brd.append(".....OK!")

    def rst_brd(self):
        self.flchck.reset()
        self.ui.mssg_brd.clear()

    def sent_clp(self):
        pyperclip.copy(self.flchck.log)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # a_blank_tm = MyTableModel()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
