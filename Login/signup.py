# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib, re

class Ui_SignUp(object):
    def signUpAsStaff(self,Dialog):
        self.connection = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',password = 'Al5qCS2i', user = 'cs4400_group59', db='cs4400_group59')
        self.cursor = self.connection.cursor()
        # the input data in registration screen
        email = self.reg_email_line.text()
        username = self.reg_username_line.text()
        password = self.reg_pass_line.text()
        hashedPw = hashlib.md5(password.encode()).hexdigest()
        conf_password = self.reg_conf_line.text()
        if (not re.match("[^@]+@[^@]+\.[^@]+", email)):
            self.failedMessage("Registration Failed", "Please enter the email in the following format('emailAddress@serviceprovider.domain')")
        elif (len(password) < 8):
            self.failedMessage("Registration Failed", "The length of the password must be at least 8 characters")
        elif (password != conf_password):
            self.failedMessage("Registration Failed", "Confirm password doesn't match with the password" )
        else:
            self.cursor.execute("SELECT * FROM cs4400_group59.USER AS USER WHERE USER.Email = '{}';".format(email))
            result = self.cursor.fetchall()
            self.cursor.execute("SELECT * FROM cs4400_group59.USER AS USER WHERE USER.Username = '{}';".format(username))
            result2 = self.cursor.fetchall()
            if (len(result) != 0):
                self.failedMessage("Registration Failed", "The email is already registered")
            elif (len(result2) != 0):
                self.failedMessage("Registration Failed", "The Username is already registered")
            else:
                self.cursor.execute("INSERT into cs4400_group59.USER Value ('{}','{}','{}');".format(username, email, hashedPw))
                self.cursor.execute("INSERT into cs4400_group59.STAFF Value ('{}');".format(username))
                self.connection.commit()
                self.d.reject()

    def signUpAsVisitor(self):
        self.connection = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',password = 'Al5qCS2i', user = 'cs4400_group59', db='cs4400_group59')
        self.cursor = self.connection.cursor()
        #the input data in registration screen
        email = self.reg_email_line.text()
        username = self.reg_username_line.text()
        password = self.reg_pass_line.text()
        hashedPw = hashlib.md5(password.encode()).hexdigest()
        conf_password = self.reg_conf_line.text()
        if (not re.match("[^@]+@[^@]+\.[^@]+", email)):
            self.failedMessage("Registration Failed", "Please enter the email in the following format('emailAddress@serviceprovider.domain')")
        elif (len(password) < 8):
            self.failedMessage("Registration Failed", "The length of the password must be at least 8 characters")
        elif (password != conf_password):
            self.failedMessage("Registration Failed", "Confirm password doesn't match with the password" )
        else:
            self.cursor.execute("SELECT * FROM cs4400_group59.USER AS USER WHERE USER.Email = '{}';".format(email))
            result = self.cursor.fetchall()
            self.cursor.execute("SELECT * FROM cs4400_group59.USER AS USER WHERE USER.Username = '{}';".format(username))
            result2 = self.cursor.fetchall()
            if (len(result) != 0):
                self.failedMessage("Registration Failed", "The email is already registered")
            elif (len(result2) != 0):
                self.failedMessage("Registration Failed", "The Username is already registered")
            else:
                self.cursor.execute("INSERT into cs4400_group59.USER Value ('{}','{}','{}');".format(username, email, hashedPw))
                self.cursor.execute("INSERT into cs4400_group59.VISITOR Value ('{}');".format(username))
                self.connection.commit()
                self.d.reject()


    def failedMessage(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 372)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(252, 175, 62, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 40, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 110, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 170, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.reg_email_line = QtWidgets.QLineEdit(Dialog)
        self.reg_email_line.setGeometry(QtCore.QRect(210, 110, 151, 25))
        self.reg_email_line.setObjectName("reg_email_line")
        self.reg_username_line = QtWidgets.QLineEdit(Dialog)
        self.reg_username_line.setGeometry(QtCore.QRect(210, 140, 151, 25))
        self.reg_username_line.setObjectName("reg_username_line")
        self.reg_pass_line = QtWidgets.QLineEdit(Dialog)
        self.reg_pass_line.setGeometry(QtCore.QRect(210, 170, 151, 25))
        self.reg_pass_line.setObjectName("reg_pass_line")
        self.reg_conf_line = QtWidgets.QLineEdit(Dialog)
        self.reg_conf_line.setGeometry(QtCore.QRect(210, 200, 151, 25))
        self.reg_conf_line.setObjectName("reg_conf_line")
        self.reg_visitor_button = QtWidgets.QPushButton(Dialog)
        self.reg_visitor_button.setGeometry(QtCore.QRect(70, 250, 121, 25))
        self.reg_visitor_button.setObjectName("reg_visitor_button")
        ############register as visitor#####################################
        self.d = Dialog
        self.reg_visitor_button.clicked.connect(self.signUpAsVisitor)

        ######################################################################
        self.reg_staff_button = QtWidgets.QPushButton(Dialog)
        self.reg_staff_button.setGeometry(QtCore.QRect(210, 250, 111, 25))
        self.reg_staff_button.setObjectName("reg_staff_button")
        ###############register as staff################################
        self.reg_staff_button.clicked.connect(self.signUpAsStaff)
        ###############################################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Atlanta Zoo Registration"))
        self.label_2.setText(_translate("Dialog", "Email"))
        self.label_3.setText(_translate("Dialog", "Username"))
        self.label_4.setText(_translate("Dialog", "Password"))
        self.label_5.setText(_translate("Dialog", "Confirm Password"))
        self.reg_visitor_button.setText(_translate("Dialog", "Register Visitor"))
        self.reg_staff_button.setText(_translate("Dialog", "Register Staff"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_SignUp()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

