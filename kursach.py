import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox

from login import Ui_Login
from mainemp import Ui_MainWindow as MainEmp
from register import Ui_Login as register
from rezum import Ui_MainWindow as rezum
from vac import Ui_MainWindow as vac
from delete import Ui_Delete as delete
from change_pass import Ui_Delete as Change_pass
from change_name import Ui_Delete as Change_name
from create_emp import Ui_Form as Create_emp
from filter_emp import Ui_Form as FilterEmp
from viewEMP import Ui_MainWindow as ViewEmp

from create_res import Ui_Form as Create_res
from mainseek import  Ui_MainWindow as MainSeek
from rezum_v2 import Ui_MainWindow as ViewRez
from filterSeeker import Ui_Form as FilterSeek
from afterFiltratinSeeker import Ui_Form as afterFilter

import work_with_db as wdb


class MyWin(QtWidgets.QMainWindow, QtWidgets.QMessageBox): 
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.password_2.hide()
        
        self.regi = Reg() 
        self.mainEMP = MainEMP()
        self.MainSeeker = MainSeeker()

        self.ui.log_2.clicked.connect(self.reg)
        self.ui.log.clicked.connect(self.auth)
        self.ui.pushButton_2.clicked.connect(self.cancel)


    def auth(self):
        self.log = self.ui.username.text()
        self.pas = self.ui.password.text()
        try:
            logging = wdb.login(str(self.log), str(self.pas))  
            if len(logging)>0:
                if str(logging[-1]) == 'employer':
                    self.mainEMP.ui.label.setText(f'Привет, {logging[0]}')
                    self.mainEMP.show()
                    self.close()
                elif str(logging[-1]) == 'seeker':
                    self.MainSeeker.ui.label.setText(f'Привет, {logging[0]}')
                    self.MainSeeker.show()
                    self.close()

        except:
            self.ui.password_2.show()
            self.ui.password_2.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
            self.ui.password_2.setText("Логин или пароль неверны")

    def reg(self):
        self.close()
        self.regi.show()

    def cancel(self):
        self.close()




class MainSeeker(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = MainSeek()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.change_name)
        self.ui.pushButton_7.clicked.connect(self.logout)
        self.ui.pushButton.clicked.connect(self.change_pass)
        self.ui.pushButton_6.clicked.connect(self.delete)
        self.ui.pushButton_4.clicked.connect(self.create_res)
        self.ui.pushButton_3.clicked.connect(self.viewRez)
        self.ui.pushButton_5.clicked.connect(self.filter)
        
    def filter(self):
        self.filterS = FilterSeeker()
        self.filterS.show()


    def viewRez(self):
        self.username = self.ui.label.text().replace('Привет,','').strip()
        self.viewres = ViewResum(self.username)
        self.viewres.show()

    def change_name(self):
        self.username = self.ui.label.text().replace('Привет,','').strip()
        self.change_nam = Change_nam(self.username)
        self.change_nam.show()

    def logout(self):
        masg = QMessageBox(QMessageBox.Question, "Выход из аккаунта", "Вы уверены, что хотите выйти ?")
        masg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        masg.setIcon(QMessageBox.Question)
        ret = masg.exec_()
        if ret == QMessageBox.Ok:
            self.close()
            self.logs = MyWin()
            self.logs.show()

    def change_pass(self):
        self.username = self.ui.label.text().replace('Привет,','').strip()
        self.change_pas = Change_pas(self.username)
        self.change_pas.show()

    def delete(self):
            self.username = self.ui.label.text().replace('Привет,','').strip()
            self.dele = Delete(self.username)
            self.close()
            self.dele.show()

    def create_res(self):
        self.username = self.ui.label.text().replace('Привет,','').strip()
        self.create = CreateRes(self.username)
        self.create.show()

class FilterSeeker(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = FilterSeek()
        self.ui.setupUi(self)


        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.pushButton.clicked.connect(self.getFilter)

    def getFilter(self):
        self.salary = self.ui.lineEdit_2.text()
        self.city = str(self.ui.lineEdit_3.text()).strip() + '%'
        if str(self.salary).strip() == '':
            self.salary = 0
        self.filtered = wdb.getFiltered(self.salary, self.city)
        self.keyWords = self.ui.lineEdit.text()
        self.after = AfterFilterSeeker(self.filtered, self.keyWords)
        self.after.show()
        self.close()


    def cancel(self):
        self.close()

class AfterFilterSeeker(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, filtered,keyWords, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = afterFilter()
        self.ui.setupUi(self)

        self.data = filtered
        self.keyWords = keyWords
        self.point = 0

        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.pushButton.clicked.connect(self.toFilters)

        if str(self.keyWords).strip() == '' :
            for item in self.data:
                self.point +=1
                self.ui.label_3.setText(f'Совпадений по запросу: {self.point}')
                self.text = f'{self.point}. Должность: {item[0]}; Зп: {item[1]}$; Город: {item[2]}; Описание: {item[3]}; Автор: {item[4]};\n'
                self.ui.textEdit_2.append(self.text)
        else:
            for item in self.data:
                if str(self.keyWords).strip().lower() in item[0].lower() or str(self.keyWords).strip().lower() in item[3].lower():
                    self.point +=1
                    self.text = f'{self.point}. Должность: {item[0]}; Зп: {item[1]}$; Город: {item[2]}; Описание: {item[3]}; Автор: {item[4]};\n'
                    self.ui.textEdit_2.append(self.text)
                    self.count = len(self.ui.textEdit_2.toPlainText().strip().split("\n"))
                    self.ui.label_3.setText(f'Совпадений по запросу: {self.count}')

    def cancel(self):
        self.close()
    
    def toFilters(self):
        self.filterS = FilterSeeker()
        self.filterS.show()

        self.close()



class ViewResum(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, username, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ViewRez()
        self.ui.setupUi(self)
        self.username = username

        self.ui.pushButton_3.clicked.connect(self.create_res)
        self.ui.pushButton_4.clicked.connect(self.cancel)



        self.allRes = wdb.getAllRes(self.username)
        self.ui.label_14.setText(f'Создано {len(self.allRes)} резюме')
        self.point = 0
        for item in range(1, len(self.allRes)+1):
            self.add1 = 'Активировать №{}'.format(item)
            self.add2 = 'Деактивировать №{}'.format(item)
            self.add3 = 'Обновить №{}'.format(item)
            self.add4 = 'Спрятать №{}'.format(item)
            self.all =[self.add1,self.add2,self.add4,self.add4]
            self.ui.comboBox_2.addItems(self.all)
        
        for item in range(1, len(self.allRes)+1):
            self.add1 = 'Cкачать .doc №{}'.format(item)
            self.add2 = 'Создать копию №{}'.format(item)
            self.add3 = 'Удалить №{}'.format(item)
            self.add4 = 'Редактировать №{}'.format(item)
            self.last = 'Предпросмотр №{}'.format(item)
            self.all =[self.add1,self.add2,self.add4,self.add4, self.last]
            self.ui.comboBox.addItems(self.all)


        for item in self.allRes:
            self.point +=1
            self.text = f'{self.point}. Должность: {item[0]}; Зп: {item[1]}$; Город: {item[2]}; Описание: {item[3]};\n'
            self.ui.textEdit.append(self.text)
    def cancel(self):
        self.close()

    def create_res(self):
        self.create = CreateRes(self.username)
        self.create.show()

class CreateRes(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, username, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Create_res()
        self.ui.setupUi(self)
        self.username = username
        self.ui.lineEdit_6.hide()
        
        self.ui.create.clicked.connect(self.create)
        self.ui.cancel.clicked.connect(self.cancel)

        
    def cancel(self):
        self.close()
        
    def create(self):
        self.salary = self.ui.lineEdit_2.text().strip()
        self.post = self.ui.lineEdit.text().strip()
        self.city = self.ui.lineEdit_5.text().strip()
        self.desc = self.ui.lineEdit_4.text().strip()
        self.path_image = self.ui.lineEdit_3.text().strip()
        self.point = 0
        try:
            self.salary = int(self.salary)
        except:
            self.point-=1
            self.ui.lineEdit_6.show()
            self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
            self.ui.lineEdit_6.setText("Salary must be integer")
        if len(self.path_image) == 0:
            self.path_image = ''
        if len(str(self.salary)) > 0:
            if len(self.post) > 0:
                if len(self.city) > 0:
                    if len(self.desc) > 0:
                        if self.point == 0:
                            wdb.create_res(self.post, self.salary, self.city, self.desc, self.path_image, self.username)
                            msg = QMessageBox()
                            msg.setText("Вакансия успешно создана")
                            msg.setIcon(QMessageBox.Information)
                            reіtt = msg.exec_()
                            self.close()
                    else:
                        self.point-=1
                        self.ui.lineEdit_6.show()
                        self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                        self.ui.lineEdit_6.setText("Заполните описание")
                else:
                    self.point-=1
                    self.ui.lineEdit_6.show()
                    self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                    self.ui.lineEdit_6.setText("Заполните город")
            else:
                    self.point-=1
                    self.ui.lineEdit_6.show()
                    self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                    self.ui.lineEdit_6.setText("Заполните должность")
        else:
                    self.point-=1
                    self.ui.lineEdit_6.show()
                    self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                    self.ui.lineEdit_6.setText("Заполните зарплату")

class AfterFilterEMP(QtWidgets.QMainWindow, QtWidgets.QMessageBox): #sda
    def __init__(self, filtered,keyWords, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = afterFilter()
        self.ui.setupUi(self)

        self.data = filtered
        self.keyWords = keyWords
        self.point = 0

        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.pushButton.clicked.connect(self.toFilters)

        if str(self.keyWords).strip() == '' :
            for item in self.data:
                self.point +=1
                self.ui.label_3.setText(f'Совпадений по запросу: {self.point}')
                self.text = f'{self.point}. Должность: {item[0]}; Зп: {item[1]}$; Город: {item[2]}; Описание: {item[3]}; Автор: {item[4]};\n'
                self.ui.textEdit_2.append(self.text)
        else:
            for item in self.data:
                if str(self.keyWords).strip().lower() in item[0].lower() or str(self.keyWords).strip().lower() in item[3].lower():
                    self.point +=1
                    self.text = f'{self.point}. Должность: {item[0]}; Зп: {item[1]}$; Город: {item[2]}; Описание: {item[3]}; Автор: {item[4]};\n'
                    self.ui.textEdit_2.append(self.text)
                    self.count = len(self.ui.textEdit_2.toPlainText().strip().split("\n"))
                    self.ui.label_3.setText(f'Совпадений по запросу: {self.count}')

    def cancel(self):
        self.close()
    
    def toFilters(self):
        self.filterS = FilterEMP()
        self.filterS.show()

        self.close()

class MainEMP(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = MainEmp()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.change_name)
        self.ui.pushButton_7.clicked.connect(self.logout)
        self.ui.pushButton_6.clicked.connect(self.delete)
        self.ui.pushButton.clicked.connect(self.change_pass)
        self.ui.pushButton_4.clicked.connect(self.create_emp)
        self.ui.pushButton_5.clicked.connect(self.filter)
        self.ui.pushButton_3.clicked.connect(self.viewEmp)

    def viewEmp(self):
        self.username = self.ui.label.text().replace('Привет,','').strip()
        self.viewemp = ViewEMP(self.username)
        self.viewemp.show()

    def filter(self):
        self.filterS = FilterEMP()
        self.filterS.show()
    
    def create_emp(self):
        self.username = self.ui.label.text().replace('Привет,','').strip()
        self.create = Create(self.username)
        self.create.show()

    def change_name(self):
        self.username = self.ui.label.text().replace('Привет,','').strip()
        self.change_nam = Change_nam(self.username)
        self.change_nam.show()

    def change_pass(self):
        self.username = self.ui.label.text().replace('Привет,','').strip()
        self.change_pas = Change_pas(self.username)
        self.change_pas.show()

    def logout(self):
        masg = QMessageBox(QMessageBox.Question, "Выход из аккаунта", "Вы уверены, что хотите выйти ?")
        masg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        masg.setIcon(QMessageBox.Question)
        ret = masg.exec_()
        if ret == QMessageBox.Ok:
            self.close()
            self.logs = MyWin()
            self.logs.show()

    def delete(self):
        self.username = self.ui.label.text().replace('Привет,','').strip()
        self.dele = Delete(self.username)
        self.close()
        self.dele.show()

class ViewEMP(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, username, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ViewEmp()
        self.ui.setupUi(self)
        self.username = username


        self.ui.pushButton_3.clicked.connect(self.create_emp)
        self.ui.pushButton_4.clicked.connect(self.cancel)



        self.allRes = wdb.getAllEmp(self.username)
        self.ui.label_14.setText(f'Создано {len(self.allRes)} вакансии')
        self.point = 0
        for item in range(1, len(self.allRes)+1):
            self.add1 = 'Активировать №{}'.format(item)
            self.add2 = 'Деактивировать №{}'.format(item)
            self.add3 = 'Обновить №{}'.format(item)
            self.add4 = 'Спрятать №{}'.format(item)
            self.all =[self.add1,self.add2,self.add4,self.add4]
            self.ui.comboBox_2.addItems(self.all)
        
        for item in range(1, len(self.allRes)+1):
            self.add1 = 'Cкачать .doc №{}'.format(item)
            self.add2 = 'Создать копию №{}'.format(item)
            self.add3 = 'Удалить №{}'.format(item)
            self.add4 = 'Редактировать №{}'.format(item)
            self.last = 'Предпросмотр №{}'.format(item)
            self.all =[self.add1,self.add2,self.add4,self.add4, self.last]
            self.ui.comboBox.addItems(self.all)


        for item in self.allRes:
            self.point +=1
            self.text = f'{self.point}. Должность: {item[0]}; Зп: {item[1]}$; Город: {item[2]}; Описание: {item[3]};\n'
            self.ui.textEdit.append(self.text)
    def cancel(self):
        self.close()

    def create_emp(self):
        self.create = Create(self.username)
        self.close()
        self.create.show()

class FilterEMP(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self,  parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = FilterEmp()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.getFilter)
        self.ui.pushButton_2.clicked.connect(self.cancel)
        
    def getFilter(self):
        self.salary = self.ui.lineEdit_2.text()
        self.city = str(self.ui.lineEdit_3.text()).strip() + '%'
        if str(self.salary).strip() == '':
            self.salary = 0
        self.filtered = wdb.getFilteredForEmp(self.salary, self.city)
        self.keyWords = self.ui.lineEdit.text()
        self.after = AfterFilterSeeker(self.filtered, self.keyWords)
        self.after.show()
        self.close()



    def cancel(self):
        self.close()

class Change_nam(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, username, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Change_name()
        self.ui.setupUi(self)
        self.username = username
        self.ui.password_3.hide()


        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.pushButton_3.clicked.connect(self.change)

    def cancel(self):
        self.close()

    def change(self):
        pas = wdb.delete(self.username)
        if str(pas[0]).strip() == str(self.ui.password_2.text()):
            if len(self.ui.password_5.text()) > 6:
                
                    if str(self.ui.password_5.text()) != str(self.username):
                        try:
                            wdb.change_name(str(self.ui.password_5.text()), str(pas[0]).strip())
                            msg = QMessageBox()
                            msg.setText("Имя успешно изменено")
                            msg.setIcon(QMessageBox.Information)
                            reіtt = msg.exec_()
                            self.close()
                        except:
                            self.ui.password_3.show()
                            self.ui.password_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                            self.ui.password_3.setText("Username alredy taken")
                    else:
                        self.ui.password_3.show()
                        self.ui.password_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                        self.ui.password_3.setText("Новей и старое имена не должны совпадать")
                
            else:
                self.ui.password_3.show()
                self.ui.password_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                self.ui.password_3.setText("Имя должно быть > 6")    
        else:
            self.ui.password_3.show()
            self.ui.password_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
            self.ui.password_3.setText("Пароль неверен")    

class Change_pas(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, username, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Change_pass()
        self.ui.setupUi(self)
        self.username = username
        self.ui.password_3.hide()

        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.pushButton_3.clicked.connect(self.change)

    def cancel(self):
        self.close()

    def change(self):
        pas = wdb.delete(self.username)
        if str(pas[0]).strip() == str(self.ui.password_2.text()):
            if len(self.ui.password_4.text()) > 10:
                if str(self.ui.password_4.text()) == str(self.ui.password_5.text()):
                    if str(self.ui.password_4.text()) != str(self.ui.password_2.text()):
                        wdb.change_pass(str(self.ui.password_5.text()), str(self.username))
                        msg = QMessageBox()
                        msg.setText("Пароль успешно изменен")
                        msg.setIcon(QMessageBox.Information)
                        reіtt = msg.exec_()
                        self.close()
                    else:
                        self.ui.password_3.show()
                        self.ui.password_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                        self.ui.password_3.setText("Новый и старый пароли не должны совпадать")
                else:
                    self.ui.password_3.show()
                    self.ui.password_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                    self.ui.password_3.setText("Пароли должны быть одинаковы")
            else:
                self.ui.password_3.show()
                self.ui.password_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                self.ui.password_3.setText("Пароль короткий")    
        else:
            self.ui.password_3.show()
            self.ui.password_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
            self.ui.password_3.setText("Пароль неверен")    

class Delete(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, username, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = delete()
        self.ui.setupUi(self)
        self.username = username
        self.ui.password_3.hide()

        self.ui.pushButton_2.clicked.connect(self.cancel)
        self.ui.pushButton_3.clicked.connect(self.delete)

    def cancel(self):
        self.close()
        self.logs = MyWin()
        self.logs.show()

    
    def delete(self):
        pas = wdb.delete(self.username)
        if str(pas[0]).strip() == str(self.ui.password_2.text()):
            wdb.del_acc(str(pas[0]))
            msg = QMessageBox()
            msg.setText("Аккаунт успешно удален")
            msg.setIcon(QMessageBox.Information)
            reіtt = msg.exec_()
            self.close()
            self.logs = MyWin()
            self.logs.show()

        else:
            self.ui.password_3.show()
            self.ui.password_3.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
            self.ui.password_3.setText("Пароль неверен")

class Reg(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = register()
        self.ui.setupUi(self)
        self.ui.errors.hide()

        self.ui.register_2.clicked.connect(self.reg)
        self.ui.cancel.clicked.connect(self.cancel)


    def create_new(self, username, password1, type):
            try:
                wdb.register(str(self.username), str(self.password1), str(self.type))
                self.close()
                self.logs = MyWin()
                self.logs.ui.username.setText(self.username)  #заполнение ника в форме входа
                self.logs.ui.password.setText(self.password1)   #заполнение пароля в форме входа
                self.logs.show()

            except:
                self.ui.errors.show()
                self.ui.errors.setStyleSheet('background-color : red; color :rgb(0, 0, 0);font-size:12pxpx')
                self.ui.errors.setText(f"Username alredy taken")



    def reg(self):
        self.username = self.ui.username.text()
        self.password1 = self.ui.password1.text()
        self.password2 = self.ui.password2.text()

        if self.password2 == self.password1:
            if len(self.password1) > 9 and len(self.password2) > 9:
                if len(self.username) > 6 :
                    if self.ui.seeker.isChecked() or self.ui.employer.isChecked():
                        if self.ui.seeker.isChecked():
                            self.type = 'seeker'
                            self.create_new(str(self.username), str(self.password1), str(self.type))
                        else:
                            self.type = 'employer'
                            self.create_new(str(self.username), str(self.password1), str(self.type))

                    else:
                        self.ui.errors.show()
                        self.ui.errors.setStyleSheet('background-color : red; color :rgb(0, 0, 0);font-size:12pxpx')
                        self.ui.errors.setText("Выберете тип регистрации")
                else:
                    self.ui.errors.show()
                    self.ui.errors.setStyleSheet('background-color : red; color :rgb(0, 0, 0);font-size:12pxpx')
                    self.ui.errors.setText("Длинна имени должна быть > 6")
            else:
                self.ui.errors.show()
                self.ui.errors.setStyleSheet('background-color : red; color :rgb(0, 0, 0);font-size:12pxpx')
                self.ui.errors.setText("Длинна пароля должна быть > 10")
        else:
            self.ui.errors.show()
            self.ui.errors.setStyleSheet('background-color : red; color :rgb(0, 0, 0);font-size:12pxpx')
            self.ui.errors.setText("Пароли должны совпадать")





    




    def cancel(self):
        self.close()
        self.logs = MyWin()
        self.logs.show()
    
class Create(QtWidgets.QMainWindow, QtWidgets.QMessageBox):
    def __init__(self, username, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Create_emp()
        self.ui.setupUi(self)
        self.username = username
        self.ui.lineEdit_6.hide()

        self.ui.create.clicked.connect(self.create)
        self.ui.cancel.clicked.connect(self.cancel)


    def cancel(self):
        self.close()
        
    def create(self):
        self.salary = self.ui.lineEdit.text().strip()
        self.head = self.ui.lineEdit_2.text().strip()
        self.city = self.ui.lineEdit_5.text().strip()
        self.body = self.ui.lineEdit_4.text().strip()
        self.path_image = self.ui.lineEdit_3.text().strip()
        self.point = 0
        try:
            self.salary = int(self.salary)
        except:
            self.point-=1
            self.ui.lineEdit_6.show()
            self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
            self.ui.lineEdit_6.setText("Salary must be integer")
        if len(self.path_image) == 0:
            self.path_image = ''
        if len(str(self.salary)) > 0:
            if len(self.head) > 0:
                if len(self.city) > 0:
                    if len(self.body) > 0:
                        if self.point == 0:
                            wdb.create_emp(self.head, self.salary, self.city, self.body, self.path_image, self.username)
                            msg = QMessageBox()
                            msg.setText("Вакансия успешно создана")
                            msg.setIcon(QMessageBox.Information)
                            reіtt = msg.exec_()
                            self.close()
                    else:
                        self.point-=1
                        self.ui.lineEdit_6.show()
                        self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                        self.ui.lineEdit_6.setText("Заполните описание")
                else:
                    self.point-=1
                    self.ui.lineEdit_6.show()
                    self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                    self.ui.lineEdit_6.setText("Заполните город")
            else:
                    self.point-=1
                    self.ui.lineEdit_6.show()
                    self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                    self.ui.lineEdit_6.setText("Заполните Head")
        else:
                    self.point-=1
                    self.ui.lineEdit_6.show()
                    self.ui.lineEdit_6.setStyleSheet('background-color : red; color :rgb(0, 0, 0);')
                    self.ui.lineEdit_6.setText("Заполните Salary")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())