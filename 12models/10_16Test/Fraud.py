from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from Database import Sign  # importing database.py
from signup import Ui_Dialog
from Cryp import Mac
# from admin_view import Ui_Dialog_admin
# from user import Ui_Dialog_user


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Log In")
        Dialog.setFixedSize(600, 400)

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 160, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 190, 151, 21))
        self.label_2.setObjectName("label_2")
        self.txtCID = QtWidgets.QLineEdit(Dialog)
        self.txtCID.setGeometry(QtCore.QRect(300, 160, 191, 27))
        self.txtCID.setObjectName("txtUsername")
        self.txtPassword = QtWidgets.QLineEdit(Dialog)

        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.txtPassword.setGeometry(QtCore.QRect(300, 190, 191, 27))
        self.txtPassword.setObjectName("txtPassword")
        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(210, 250, 71, 41))
        self.btnLogin.setObjectName("btnLogin")

        self.btnLogin.clicked.connect(self.loginCheck)

        # self.btnSignup = QtWidgets.QPushButton(Dialog)
        # self.btnSignup.setGeometry(QtCore.QRect(290, 250, 81, 41))
        # self.btnSignup.setObjectName("btnSignup")

        # self.btnSignup.clicked.connect(self.signupButton)

        self.label_Heading = QtWidgets.QLabel(Dialog)
        self.label_Heading.setGeometry(QtCore.QRect(150, 90, 381, 51))
        self.label_Heading.setObjectName("label_Heading")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):  # ok
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Log In"))
        self.label.setText(_translate("Dialog", "CID:"))
        self.label_2.setText(_translate("Dialog", "Password:"))
        self.btnLogin.setText(_translate("Dialog", "Login"))
        # self.btnSignup.setText(_translate("Dialog", "SignUp"))
        self.label_Heading.setText(_translate("Dialog", "Welcome to Insurance system!"))

    def user_page(self, cid):  # revising
        # app = QApplication(sys.argv)
        self.userDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog_user()
        self.ui.setupUi(self.userDialog, cid)
        self.userDialog.show()
        # sys.exit(app.exec_())

    # def admin_page(self):
    #     self.adminDialog = QtWidgets.QDialog()
    #     self.ui = Ui_Dialog_admin()
    #     self.ui.setupUi(self.adminDialog)
    #     self.adminDialog.show()

    def loginCheck(self):  # 登录检查，如果成功跳转页面，失败就弹出错误信息
        cid = self.txtCID.text()
        # print(cid)
        password = self.txtPassword.text()
        mac=Mac(cid)#在Cryp的类Mac()
        macResult=mac.getHMac()
        print("这个值之后会由梁建威传来: {}".format(macResult))
        if macResult==password:
            print("登录成功")
            self.user_page(cid)
            # #TODO 尝试用这种情况调用

        else:
            print("password wrong")
            self.showMessage("Warning", "Invalid CID and Password")



        # print(password)
        # getDb = Sign()#在Database的类Sign()
        # result = getDb.login(cid, password)

        # print(result)

        # if (result):
        #     if cid == '100000001':
        #         self.admin_page()
        #     else:
        #         self.user_page(cid)
        #     self.clearField()
        #     print(result)
        # else:
        #     print("password wrong")
        #     self.showMessage("Warning", "Invalid CID and Password")

    # def showMessage(self, title, msg):
    #     msgBox = QtWidgets.QMessageBox()
    #     msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    #     # msgBox.setTitle(title)
    #     msgBox.setText(msg)
    #     msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
    #     msgBox.exec_()

    # def signupButton(self):
    #     self.signDialog = QtWidgets.QDialog()
    #     self.ui = Ui_Dialog()
    #     self.ui.setupUi(self.signDialog)
    #     self.signDialog.show()

    def clearField(self):
        self.txtCID.setText(None)
        self.txtPassword.setText(None)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

