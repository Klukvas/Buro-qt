# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(555, 347)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Login.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        Login.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 80, 341, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.username.setObjectName("username")
        self.verticalLayout.addWidget(self.username)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(70, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 261, 41))
        self.label_3.setObjectName("label_3")
        self.password_2 = QtWidgets.QLineEdit(Login)
        self.password_2.setGeometry(QtCore.QRect(190, 200, 339, 30))
        self.password_2.setObjectName("password_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Login)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 290, 461, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.log = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.log.setObjectName("log")
        self.horizontalLayout.addWidget(self.log)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.log_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.log_2.setObjectName("log_2")
        self.horizontalLayout.addWidget(self.log_2)
        self.radioButton = QtWidgets.QRadioButton(Login)
        self.radioButton.setGeometry(QtCore.QRect(70, 250, 192, 28))
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.label.setText(_translate("Login", "Username"))
        self.label_2.setText(_translate("Login", "Password"))
        self.label_3.setText(_translate("Login", "Бюро працевлаштування"))
        self.log.setText(_translate("Login", "Login"))
        self.pushButton_2.setText(_translate("Login", "Cancel"))
        self.log_2.setText(_translate("Login", "Registration"))
        self.radioButton.setText(_translate("Login", "Keep me signed in"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
