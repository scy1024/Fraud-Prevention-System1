##以当前为准 2022-12-3
from car_infer import Module

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QDialog, QLabel, QHBoxLayout, QWidget, QFormLayout, QPushButton, QLineEdit, \
    QInputDialog, QMessageBox

# from Database import Sign  # importing database.py
# from signup import Ui_Dialog
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
        self.label.setText(_translate("Dialog", "UserName:"))
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
        cid = self.txtCID.text()
        # print(cid)
        password = self.txtPassword.text()
        mac=Mac(cid)#在Cryp的类Mac()
        macResult=mac.getHMac()
        print("这个值之后会由梁建威传来: {}".format(macResult))
        if macResult==password:
            print("登录成功")
            # self.user_page(cid) # #TODO 尝试用这种情况调用
            input.show()
        else:
            print("password wrong")
            self.showMessage("Warning", "Invalid CID and Password")



        # input.show()

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

        # 箱布局
        # 欢迎
        welhbox = QHBoxLayout()
        welhbox.addWidget(qlwelcome)
        # welhbox.addWidget(qlaccnumber)
        welhbox.addStretch(5)
        self.setGeometry(50,50, 600, 300)
        self.setWindowTitle('user')





# 用户登录后的界面
class InputdialogDemo(QWidget):
    def __init__(self, parent=None):
        # 输入数据 部分写死
        #全设置的是平均值，输入直接覆盖

        self.inputList=[204, 39, 546000, '1990/1/8', 'OH', '250/500', 1140, 1260, 1100000, 501000, 'FEMALE', 'JD', 'machine-op-inspct', 'reading', 'own-child', 25100, -26800, '2015/1/1', 'Multi-vehicle Collision', 'Rear Collision', 'Minor Damage', 'Police', 'Springfield', 'Columbus', '7121 Francis Lane', 11, 2, 'NO', 1, 2, 'NO', 528000, 7400, 7400, 380000, 'Saab', 'RAM', 2015, 'N', 0]


        super(InputdialogDemo, self).__init__(parent)
        layout = QFormLayout()
        # self.resize(400, 100)
        # +++policy_number, 保单号 + +++++
        # incident_date, 事故日期 + +++++
        # incident_type, 事故类型 + +++++
        # collision_type, 碰撞类型 + +++++
        # incident_severity, 事故_严重性 + +++++
        # authorities_contacted, 当局联系 + +++++
        # incident_state, 事故_严重程度 + +++++
        # incident_city, 事故_城市 + +++++
        # incident_location, 事故_位置 + +++++
        # incident_hour_of_the_day, 事故_时间点 + +++++
        # number_of_vehicles_involved, 涉及车辆数目 + +++++
        # property_damage, 财产损失 + +++++
        # bodily_injuries, 身体伤害 + +++++
        # witnesses, 目击者 + +++++
        # police_report_available, 警方报告，++++++
        # injury_claim, 伤害索赔, ++++++
        # property_claim, 财产索赔, ++++++
        # vehicle_claim, 车辆索赔, ++++++
        # auto_make, 汽车, ++++++
        # auto_model, 汽车型号 + +++++
        # fraud_reported, 欺诈报告, ++++++

        # int
        self.btn1 = QPushButton("Get Policy_number")
        self.btn1.clicked.connect(self.getpolicy_number)
        self.le1 = QLineEdit("6132")
        layout.addRow(self.btn1, self.le1)

        # str
        self.btn2 = QPushButton("Get Incident_date")
        self.btn2.clicked.connect(self.getincident_date)
        self.le2 = QLineEdit("2015/1/25")
        layout.addRow(self.btn2, self.le2)

        # 选项
        # Multi-vehicle Collision
        # Single Vehicle Collision
        # Vehicle Theft
        # Parked Car
        self.btn3 = QPushButton("Get Incident_type")
        self.btn3.clicked.connect(self.getincident_type)
        self.le3 = QLineEdit("Single Vehicle Collision")
        layout.addRow(self.btn3, self.le3)

        # 选项
        # Rear Collision
        # Side Collision
        # Front Collision
        # ?
        self.btn4 = QPushButton("Get Collision_type")
        self.btn4.clicked.connect(self.getcollision_type)
        self.le4 = QLineEdit("Side Collision")
        layout.addRow(self.btn4, self.le4)

        # Minor Damage
        # Total Loss
        # Major Damage
        # Trivial Damage
        self.btn5 = QPushButton("Get Incident_severity")
        self.btn5.clicked.connect(self.getincident_severity)
        self.le5 = QLineEdit("Major Damage")
        layout.addRow(self.btn5, self.le5)

        # Police
        # Fire
        # Other
        # Ambulance
        # None
        self.btn6 = QPushButton("Authorities_Contacted")
        self.btn6.clicked.connect(self.authorities_contacted)
        self.le6 = QLineEdit("Police")
        layout.addRow(self.btn6, self.le6)

        # str
        self.btn7 = QPushButton("Incident_State")
        self.btn7.clicked.connect(self.incident_state)
        self.le7 = QLineEdit("SC")
        layout.addRow(self.btn7, self.le7)

        # str
        self.btn8 = QPushButton("Incident_City")
        self.btn8.clicked.connect(self.incident_city)
        self.le8 = QLineEdit("Columbus")
        layout.addRow(self.btn8, self.le8)

        # ?
        # NO
        # YES
        self.btn9 = QPushButton("Incident_Location")
        self.btn9.clicked.connect(self.incident_location)
        self.le9 = QLineEdit("9935 4th Drive")
        layout.addRow(self.btn9, self.le9)

        # int
        self.btn10 = QPushButton("Number_Of_Vehicles_Involved")
        self.btn10.clicked.connect(self.number_of_vehicles_involved)
        self.le10 = QLineEdit("1")
        layout.addRow(self.btn10, self.le10)

        self.btn11 = QPushButton("Property_Damage")
        self.btn11.clicked.connect(self.property_damage)
        self.le11 = QLineEdit("YES")
        layout.addRow(self.btn11, self.le11)

        # int
        self.btn12 = QPushButton("Bodily_Injuries")
        self.btn12.clicked.connect(self.bodily_injuries)
        self.le12 = QLineEdit("1")
        layout.addRow(self.btn12, self.le12)

        # int
        self.btn13 = QPushButton("Witnesses")
        self.btn13.clicked.connect(self.witnesses)
        self.le13 = QLineEdit("2")
        layout.addRow(self.btn13, self.le13)

        # ?
        # NO
        # YES
        self.btn14 = QPushButton("Police_Report_Available")
        self.btn14.clicked.connect(self.police_report_available)
        self.le14 = QLineEdit("YES")
        layout.addRow(self.btn14, self.le14)

        # int
        self.btn15 = QPushButton("Injury_Claim")
        self.btn15.clicked.connect(self.injury_claim)
        self.le15 = QLineEdit("6510")
        layout.addRow(self.btn15, self.le15)

        # int
        self.btn16 = QPushButton("Property_Claim")
        self.btn16.clicked.connect(self.property_claim)
        self.le16 = QLineEdit("13020")
        layout.addRow(self.btn16, self.le16)
        # int
        self.btn17 = QPushButton("Vehicle_Claim")
        self.btn17.clicked.connect(self.vehicle_claim)
        self.le17 = QLineEdit("52080")
        layout.addRow(self.btn17, self.le17)
        # str
        self.btn18 = QPushButton("Auto_Make")
        self.btn18.clicked.connect(self.auto_make)
        self.le18 = QLineEdit("Saab")
        layout.addRow(self.btn18, self.le18)
        # str
        self.btn19 = QPushButton("Auto_Model")
        self.btn19.clicked.connect(self.auto_model)
        self.le19 = QLineEdit("92x")
        layout.addRow(self.btn19, self.le19)

        self.btn20 = QPushButton("ResultMsg")
        self.btn20.clicked.connect(self.resultMsg)

        layout.addRow(self.btn20)

        self.setLayout(layout)
        self.setWindowTitle("Input Dialog ")

        # module = Module(self.inputList)
        # result = module.getResult()
        # print()


    def getpolicy_number(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "Enter the Policy Number:")
        if ok:
            self.le1.setText(str(num))
            self.inputList.insert(2,num)

    def getincident_date(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Fill in the date of accident:')
        if ok:
            self.le2.setText(str(text))
            self.inputList.insert(17, text)

    def getincident_type(self):
        items = ("Multi-vehicle Collision", "Single Vehicle Collision", "Vehicle Theft", "Parked Car")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "List of accident types", items, 0, False)
        if ok and item:
            self.le3.setText(item)
            self.inputList.insert(18, item)

    def getcollision_type(self):
        items = ("Rear Collision", "Side Collision", "Front Collision", "?")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "List of collision types", items, 0, False)
        if ok and item:
            self.le4.setText(item)
            self.inputList.insert(19, item)

    def getincident_severity(self):
        items = ("Minor Damage", "Total Loss", "Major Damage", "Trivial Damage")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "Accident severity selection", items, 0, False)
        if ok and item:
            self.le5.setText(item)
            self.inputList.insert(20, item)

    def authorities_contacted(self):
        items = ("Police", "Fire", "Ambulance", "Other", "None")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "Which authorities to contact", items, 0, False)
        if ok and item:
            self.le6.setText(item)
            self.inputList.insert(21, item)

    def incident_state(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'State of accident:')
        if ok:
            self.le7.setText(str(text))
            self.inputList.insert(22, text)

    def incident_city(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'City of accident:')
        if ok:
            self.le8.setText(str(text))
            self.inputList.insert(23, text)

    def incident_location(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Location of accident:')
        if ok:
            self.le9.setText(str(text))
            self.inputList.insert(24, text)

    def number_of_vehicles_involved(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", " the number of vehicles involved:")
        if ok:
            self.le10.setText(str(num))
            self.inputList.insert(26,num)


    def property_damage(self):
        items = ("YES", "NO", "?")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "Cause property damage", items, 0, False)
        if ok and item:
            self.le11.setText(item)
            self.inputList.insert(27, item)

    def bodily_injuries(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "the number of damage:")
        if ok:
            self.le12.setText(str(num))
            self.inputList.insert(28,num)

    def witnesses(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "the number of witnesses:")
        if ok:
            self.le13.setText(str(num))
            self.inputList.insert(29,num)

    def police_report_available(self):
        items = ("YES", "NO", "?")
        item, ok = QInputDialog.getItem(self, "select input dialog",
                                        "Police report", items, 0, False)
        if ok and item:
            self.le14.setText(item)
            self.inputList.insert(30, item)

    def injury_claim(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "The amount of injury Claim:")
        if ok:
            self.le15.setText(str(num))
            self.inputList.insert(32,num)

    def property_claim(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "The amount of property Claim:")
        if ok:
            self.le16.setText(str(num))
            self.inputList.insert(33,num)

    def vehicle_claim(self):
        num, ok = QInputDialog.getInt(self, "integer input dualog", "he amount of Car Claim:")
        if ok:
            self.le17.setText(str(num))
            self.inputList.insert(34,num)

    def auto_make(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Car Made:')
        if ok:
            self.le18.setText(str(text))
            self.inputList.insert(35, text)

    def auto_model(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', 'Car Model:')
        if ok:
            self.le19.setText(str(text))
            self.inputList.insert(36, text)


    def resultMsg(self):
        # # print(self.inputList)
        # module = Module(self.inputList)
        # result = module.getResult()
        reply = QMessageBox.about(self, "Auto insurance fraud identification results","Auto insurance fraud identification results: does not involve auto insurance fraud!")
        print(reply)


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

