
from PyQt5 import QtCore, QtGui, QtWidgets
import DbWork

class Ui_SignRegTest(object):
    def setupUi(self, SignRegTest):

        SignRegTest.setObjectName("SignRegTest")    #само окно
        SignRegTest.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SignRegTest)
        self.centralwidget.setObjectName("centralwidget")

        self.UsernameEdit = QtWidgets.QLineEdit(self.centralwidget)     #поле ввода юзернейма
        self.UsernameEdit.setGeometry(QtCore.QRect(200, 200, 340, 30))
        self.UsernameEdit.setObjectName("UsernameEdit")

        self.Usernamelable = QtWidgets.QLabel(self.centralwidget)   #вспомогательная надпись
        self.Usernamelable.setGeometry(QtCore.QRect(340, 150, 50, 30))
        self.Usernamelable.setLineWidth(5)
        self.Usernamelable.setMidLineWidth(2)
        self.Usernamelable.setObjectName("Usernamelable")

        self.PasswordEdit = QtWidgets.QLineEdit(self.centralwidget)     #поле ввода пароля
        self.PasswordEdit.setGeometry(QtCore.QRect(200, 300, 340, 30))
        self.PasswordEdit.setObjectName("PasswordEdit")

        self.Passwordlable = QtWidgets.QLabel(self.centralwidget)   #вспомогательная надпись
        self.Passwordlable.setGeometry(QtCore.QRect(340, 250, 50, 30))
        self.Passwordlable.setLineWidth(5)
        self.Passwordlable.setMidLineWidth(2)
        self.Passwordlable.setObjectName("Passwordlable")

        self.SignInBtn = QtWidgets.QPushButton(self.centralwidget)      #кнопка входа
        self.SignInBtn.setGeometry(QtCore.QRect(340, 350, 75, 30))
        self.SignInBtn.setObjectName("SignInBtn")

        self.RegBtn = QtWidgets.QPushButton(self.centralwidget)     #кнопка смены типа
        self.RegBtn.setGeometry(QtCore.QRect(30, 550, 75, 30))
        self.RegBtn.setObjectName("RegBtn")

        self.PasswordConfirmEdit = QtWidgets.QLineEdit(self.centralwidget)      #поле потверждения пароля
        self.PasswordConfirmEdit.hide()
        self.PasswordConfirmEdit.setGeometry(QtCore.QRect(200, 400, 340, 30))
        self.PasswordConfirmEdit.setObjectName("PasswordConfirmEdit")

        self.PasswordConfirmlable = QtWidgets.QLabel(self.centralwidget)    #вспомогательная надпись
        self.PasswordConfirmlable.hide()
        self.PasswordConfirmlable.setGeometry(QtCore.QRect(340, 350, 90, 30))
        self.PasswordConfirmlable.setLineWidth(5)
        self.PasswordConfirmlable.setMidLineWidth(2)
        self.PasswordConfirmlable.setObjectName("PasswordConfirmlable")

        self.RegisterBtn = QtWidgets.QPushButton(self.centralwidget)    #кнопка регистрации
        self.RegisterBtn.hide()
        self.RegisterBtn.setGeometry(QtCore.QRect(333, 500, 75, 30))
        self.RegisterBtn.setObjectName("RegisterBtn")
        SignRegTest.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignRegTest)
        QtCore.QMetaObject.connectSlotsByName(SignRegTest)



        self.typeNow="sign"

        self.db=DbWork.DbWork()     #база данных

        self.RegBtn.clicked.connect(self.changeType)
        self.SignInBtn.clicked.connect(self.SignIN)
        self.RegisterBtn.clicked.connect(self.Register)

        self.Viewbtn=QtWidgets.QPushButton(self.centralwidget)          #кнопка вывода всех пользователей(для проверки)
        self.Viewbtn.setGeometry(QtCore.QRect(250, 350, 75, 30))
        self.Viewbtn.setText("View Users")
        self.Viewbtn.clicked.connect(self.ViewUsers)

        self.DeleteUserbtn=QtWidgets.QPushButton(self.centralwidget)    #кнопка удаления пользователя
        self.DeleteUserbtn.setGeometry(QtCore.QRect(430, 350, 75, 30))
        self.DeleteUserbtn.setText("Delete User")
        self.DeleteUserbtn.clicked.connect(self.DeleteUser)

        self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)     #установка режима ввода пароля
        self.PasswordConfirmEdit.setEchoMode(QtWidgets.QLineEdit.Password)

    def retranslateUi(self, SignRegTest):   #это кт дизайнер наделал

        _translate = QtCore.QCoreApplication.translate
        SignRegTest.setWindowTitle(_translate("SignRegTest", "SignReg"))
        self.Usernamelable.setText(_translate("SignRegTest", "Username"))
        self.Passwordlable.setText(_translate("SignRegTest", "Password"))
        self.SignInBtn.setText(_translate("SignRegTest", "Sign in"))
        self.RegBtn.setText(_translate("SignRegTest", "Register"))
        self.PasswordConfirmlable.setText(_translate("SignRegTest", "Confirm Password"))
        self.RegisterBtn.setText(_translate("SignRegTest", "Register"))

    def changeType(self):   #деф который меняет надписи и видимость виджетов при нажатии на кнопку смены типа(в левом нижнем углу)
        if self.RegBtn.text() == "Register":
            self.RegBtn.setText("Sign in")
            self.RegisterBtn.show()
            self.PasswordConfirmlable.show()
            self.PasswordConfirmEdit.show()
            self.SignInBtn.hide()
            self.typeNow = "reg"
            self.Viewbtn.hide()
            self.DeleteUserbtn.hide()
        else:
            self.RegBtn.setText("Register")
            self.RegisterBtn.hide()
            self.PasswordConfirmlable.hide()
            self.PasswordConfirmEdit.hide()
            self.SignInBtn.show()
            self.typeNow = "sign"
            self.Viewbtn.show()
            self.DeleteUserbtn.show()
    def SignIN(self):   #деф для входа юзера

        msg=QtWidgets.QMessageBox.information(self.centralwidget, "info", str(self.db.CheckUser(self.UsernameEdit.text(), self.PasswordEdit.text())))

        self.UsernameEdit.setText("")
        self.PasswordEdit.setText("")
        self.PasswordConfirmEdit.setText("")

    def Register(self):     #регистрация юзера
        if self.PasswordEdit.text()==self.PasswordConfirmEdit.text():   #проверка на совпадение паролев
            print(self.PasswordEdit.text() + "passs")
            msg=QtWidgets.QMessageBox.information(self.centralwidget, "info", str(self.db.AddUser(self.UsernameEdit.text(), self.PasswordEdit.text())))
        else:
            msg = QtWidgets.QMessageBox.information(self.centralwidget, "info", "Password not confirmed")

        self.UsernameEdit.setText("")
        self.PasswordEdit.setText("")
        self.PasswordConfirmEdit.setText("")
    def DeleteUser(self):   #Удаление юзера
        msg = QtWidgets.QMessageBox.information(self.centralwidget, "info",str(self.db.DeleteUser(self.UsernameEdit.text(),self.PasswordEdit.text())))
        self.UsernameEdit.setText("")
        self.PasswordEdit.setText("")
        self.PasswordConfirmEdit.setText("")

    def ViewUsers(self):    #Просмотр юзеров
        msg = QtWidgets.QMessageBox.information(self.centralwidget, "info",str(self.db.ViewBase()))

    def Start(self):    #Деф для запуска проги
        import sys
        app = QtWidgets.QApplication(sys.argv)
        SignRegTest = QtWidgets.QMainWindow()
        ui = Ui_SignRegTest()
        ui.setupUi(SignRegTest)
        SignRegTest.show()
        self.db.CloseDB()
        sys.exit(app.exec_())

