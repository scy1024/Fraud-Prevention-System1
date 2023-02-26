#!D:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/12/3 18:10
# @Author : Su Chunyu
# @File : user.py.py
# @Software: PyCharm


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
# from database import Sign, User, tupleMsg  # importing database.py
# from shop import Ui_Dialog_shop
# from profile import Ui_Dialog_update, Ui_Dialog_updatecc, Ui_Dialog_updateshipadd
import sys


class Ui_Dialog_user(object):
    def setupUi(self, Dialog, cid):
        Dialog.setObjectName("User Center")
        Dialog.setFixedSize(600, 350)
        self.CID = cid


    def showMessage(self, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setFixedSize(597, 356)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_user()
    ui.setupUi(Dialog, '100000003')
    Dialog.show()
    sys.exit(app.exec_())


