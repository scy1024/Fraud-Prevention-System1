##以当前为准 2022-12-3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QLabel, QHBoxLayout, QWidget, QFormLayout, QPushButton, QLineEdit, \
    QInputDialog

from Database import Sign  # importing database.py
from signup import Ui_Dialog
# from admin_view import Ui_Dialog_admin
# from user import Ui_Dialog_user
from Cryp import Mac
from user import Ui_Dialog_user


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

        # self.loginbtn.clicked.connect(self.loginevent)

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

    # def user_page(self, cid):  # revising
    #     self.userDialog = QtWidgets.QDialog()
    #     self.ui = Ui_Dialog_user()
    #     self.ui.setupUi(self.userDialog, cid)
    #     self.userDialog.show()

    # def admin_page(self):
    #     self.adminDialog = QtWidgets.QDialog()
    #     self.ui = Ui_Dialog_admin()
    #     self.ui.setupUi(self.adminDialog)
    #     self.adminDialog.show()

    def loginCheck(self):  # 登录检查，如果成功跳转页面，失败就弹出错误信息
        # cid = self.txtCID.text()
        # # print(cid)
        # password = self.txtPassword.text()
        # mac=Mac(cid)#在Cryp的类Mac()
        # macResult=mac.getHMac()
        # print("这个值之后会由梁建威传来: {}".format(macResult))
        # if macResult==password:
        #     print("登录成功")
        #     # self.user_page(cid) # #TODO 尝试用这种情况调用
        #     user1.show()
        # else:
        #     print("password wrong")
        #     self.showMessage("Warning", "Invalid CID and Password")
        # user1.show()
        input.show()

    def showMessage(self, title, msg):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        # msgBox.setTitle(title)
        msgBox.setText(msg)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def signupButton(self):
        self.signDialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.signDialog)
        self.signDialog.show()

    def clearField(self):
        self.txtCID.setText(None)
        self.txtPassword.setText(None)



class adminMain(QDialog):#必须是Dialog不能是QWidget才能实现界面跳转
    def __init__(self):
        super().__init__()
        self.initUI()

    # ----------------------用户界面------------------------
    def initUI(self):
        # 欢迎标签
        qlwelcome = QLabel('欢迎', self)

        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(210, 250, 71, 41))
        self.btnLogin.setObjectName("btnLogin")

        # self.btnLogin.clicked.connect()
        # 箱布局
        # 欢迎
        welhbox = QHBoxLayout()
        welhbox.addWidget(qlwelcome)
        # welhbox.addWidget(qlaccnumber)
        welhbox.addStretch(1)
        self.setGeometry(50,50, 600, 300)
        self.setWindowTitle('user')

# 用户登录后的界面
class InputdialogDemo(QWidget):
    def __init__(self, parent=None):
        super(InputdialogDemo, self).__init__(parent)
        layout = QFormLayout()
        self.btn1 = QPushButton("获得列表里的选项")
        self.btn1.clicked.connect(self.getItem)
        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)

        self.btn2 = QPushButton("获得字符串")
        self.btn2.clicked.connect(self.getIext)
        self.le2 = QLineEdit()
        layout.addRow(self.btn2, self.le2)

        self.btn3 = QPushButton("获得整数")
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()
        layout.addRow(self.btn3, self.le3)

        self.btn4 = QPushButton("输出结果")
        self.btn4.clicked.connect(self.result)

        layout.addRow(self.btn4)

        self.setLayout(layout)
        self.setWindowTitle("Input Dialog 例子")



    def getItem(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "语言列表", items, 0, False)
        if ok and item:
            self.le1.setText(item)

    def getIext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', '输入姓名:')
        if ok:
            self.le2.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "输入数字")
        if ok:
            self.le3.setText(str(num))

    def result(self):
        user1.show()


#
# class adminMain(QDialog):#必须是Dialog不能是QWidget才能实现界面跳转
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     # ----------------------用户界面------------------------
#     def initUI(self):
#         # 欢迎标签
#         qlwelcome = QLabel('欢迎', self)
#
#
#
#         # 箱布局
#         # 欢迎
#         welhbox = QHBoxLayout()
#         welhbox.addWidget(qlwelcome)
#         # welhbox.addWidget(qlaccnumber)
#         welhbox.addStretch(1)
#
#
#
#
#
#
#
#
#         self.setGeometry(50,50, 600, 1200)
#         self.setWindowTitle('user')

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    user1 = adminMain()
    # admin1=adminMain()
    input=InputdialogDemo()

    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

