# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Delete(object):
    def setupUi(self, Delete):
        Delete.setObjectName("Delete")
        Delete.resize(501, 210)
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
        Delete.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        Delete.setFont(font)
        self.label_2 = QtWidgets.QLabel(Delete)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Delete)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 291, 41))
        self.label_3.setObjectName("label_3")
        self.password_2 = QtWidgets.QLineEdit(Delete)
        self.password_2.setGeometry(QtCore.QRect(140, 90, 339, 30))
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setObjectName("password_2")
        self.pushButton_2 = QtWidgets.QPushButton(Delete)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 150, 149, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Delete)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 150, 149, 33))
        self.pushButton_3.setObjectName("pushButton_3")
        self.password_3 = QtWidgets.QLineEdit(Delete)
        self.password_3.setGeometry(QtCore.QRect(30, 50, 441, 30))
        self.password_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.password_3.setObjectName("password_3")

        self.retranslateUi(Delete)
        QtCore.QMetaObject.connectSlotsByName(Delete)

    def retranslateUi(self, Delete):
        _translate = QtCore.QCoreApplication.translate
        Delete.setWindowTitle(_translate("Delete", "Form"))
        self.label_2.setText(_translate("Delete", "Password"))
        self.label_3.setText(_translate("Delete", "Для удаления введите пароль"))
        self.pushButton_2.setText(_translate("Delete", "Cancel"))
        self.pushButton_3.setText(_translate("Delete", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Delete = QtWidgets.QWidget()
    ui = Ui_Delete()
    ui.setupUi(Delete)
    Delete.show()
    sys.exit(app.exec_())
