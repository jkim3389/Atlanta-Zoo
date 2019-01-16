# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnimalCare.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from time import gmtime, strftime
from loadData import *

class Ui_Dialog(object):
    def __init__(self, animalItems, username):
        self.animalItems = animalItems
        self.username = username
        self.connection = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',password = 'Al5qCS2i', user = 'cs4400_group59', db='cs4400_group59')
        self.sqlheaderList = ["staff", 'text', 'time']
        self.orderdict = ["asc", "asc", "asc"]

    def sortbyHeader(self):
        i = self.tableheader.sortIndicatorSection()
        query = ("SELECT staff, text, time FROM cs4400_group59.NOTE where"
                 " Name = '{}' and Species = '{}' order by {} {};".format(self.animalName, self.animalSpecies,
                                                                          self.sqlheaderList[i], self.orderdict[i]))
        if self.orderdict[i] == "asc":
            self.orderdict[i] = "desc"
        else:
            self.orderdict[i] = "asc"

        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.noteListTable, result, ['Staff Member', 'Note', 'Time'], 3)
        cursor.close()

    def tableLoad(self):
        cursor = self.connection.cursor()
        query = "SELECT staff, text, time FROM cs4400_group59.NOTE where Name = '{}' and Species = '{}';".format(self.animalName, self.animalSpecies)
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.noteListTable, result, ['Staff Member', 'Note', 'Time'], 3)


    def setLabel(self):
        self.animalName = self.animalItems[0]
        self.animalSpecies = self.animalItems[1]
        self.animalAge = self.animalItems[2]
        self.animaltype =self.animalItems[3]
        self.exhibit = self.animalItems[4]

        self.nameOutputLabel.setText(self.animalName)
        self.speciesOutputLabel.setText(self.animalSpecies)
        self.ageOutputLabel.setText(str(self.animalAge))
        self.typeOutpuLabel.setText(self.animaltype)
        self.exhibitOutputLabel.setText(self.exhibit)

    def notesLog(self):
        note = self.noteInputPlainText.toPlainText()
        if (note ==""):
            self.failedMessage("Add Failed", "Please do not create log with empty note")
        else:
            query = "INSERT INTO cs4400_group59.NOTE values ('{}', '{}', '{}', '{}', now() );".format(self.animalName, self.animalSpecies, self.username, note)
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            self.tableLoad()


    def failedMessage(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(566, 376)
        # Dialog.setStyleSheet("QDialog{\n"
        #                      "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(252, 175, 62, 255), stop:1 rgba(255, 255, 255, 255));\n"
        #                      "}")
        # Dialog = QtWidgets.QWidget(Dialog)
        # Dialog.setObjectName("centralwidget")
        self.atlantaZooLabel = QtWidgets.QLabel(Dialog)
        self.atlantaZooLabel.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.atlantaZooLabel.setObjectName("atlantaZooLabel")
        self.animalDetailLabel = QtWidgets.QLabel(Dialog)
        self.animalDetailLabel.setGeometry(QtCore.QRect(190, 10, 101, 16))
        self.animalDetailLabel.setObjectName("animalDetailLabel")
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(20, 60, 60, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.speciesLabel = QtWidgets.QLabel(Dialog)
        self.speciesLabel.setGeometry(QtCore.QRect(140, 60, 60, 16))
        self.speciesLabel.setObjectName("speciesLabel")
        self.exhibitLabel = QtWidgets.QLabel(Dialog)
        self.exhibitLabel.setGeometry(QtCore.QRect(20, 90, 60, 16))
        self.exhibitLabel.setObjectName("exhibitLabel")
        self.typeLabel = QtWidgets.QLabel(Dialog)
        self.typeLabel.setGeometry(QtCore.QRect(140, 90, 60, 16))
        self.typeLabel.setObjectName("typeLabel")
        self.ageLabel = QtWidgets.QLabel(Dialog)
        self.ageLabel.setGeometry(QtCore.QRect(350, 60, 60, 16))
        self.ageLabel.setObjectName("ageLabel")
        self.noteInputPlainText = QtWidgets.QPlainTextEdit(Dialog)
        self.noteInputPlainText.setGeometry(QtCore.QRect(20, 120, 241, 91))
        self.noteInputPlainText.setObjectName("noteInputPlainText")
        self.logNotePushButton = QtWidgets.QPushButton(Dialog)
        self.logNotePushButton.setGeometry(QtCore.QRect(300, 140, 113, 32))
        self.logNotePushButton.setObjectName("logNotePushButton")
        self.logNotePushButton.clicked.connect(self.notesLog)
        self.noteListTable = QtWidgets.QTableWidget(Dialog)
        self.noteListTable.setGeometry(QtCore.QRect(20, 220, 501, 101))
        self.noteListTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.noteListTable.setObjectName("noteListTable")
        self.nameOutputLabel = QtWidgets.QLabel(Dialog)
        self.nameOutputLabel.setGeometry(QtCore.QRect(70, 60, 60, 16))
        self.nameOutputLabel.setObjectName("nameOutputLabel")
        self.speciesOutputLabel = QtWidgets.QLabel(Dialog)
        self.speciesOutputLabel.setGeometry(QtCore.QRect(200, 60, 91, 16))
        self.speciesOutputLabel.setObjectName("speciesOutputLabel")
        self.ageOutputLabel = QtWidgets.QLabel(Dialog)
        self.ageOutputLabel.setGeometry(QtCore.QRect(400, 60, 60, 16))
        self.ageOutputLabel.setObjectName("ageOutputLabel")
        self.exhibitOutputLabel = QtWidgets.QLabel(Dialog)
        self.exhibitOutputLabel.setGeometry(QtCore.QRect(70, 90, 60, 16))
        self.exhibitOutputLabel.setObjectName("exhibitOutputLabel")
        self.typeOutpuLabel = QtWidgets.QLabel(Dialog)
        self.typeOutpuLabel.setGeometry(QtCore.QRect(200, 90, 60, 16))
        self.typeOutpuLabel.setObjectName("typeOutputLabel")
        self.backButton = QtWidgets.QPushButton(Dialog)
        self.backButton.setGeometry(QtCore.QRect(420, 140, 113, 32))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(Dialog.reject)
        # Dialog.setCentralWidget(Dialog)
        # self.menubar = QtWidgets.QMenuBar(Dialog)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 22))
        # self.menubar.setObjectName("menubar")
        # Dialog.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(Dialog)
        # self.statusbar.setObjectName("statusbar")
        # Dialog.setStatusBar(self.statusbar)

        self.tableheader = self.noteListTable.horizontalHeader()
        self.tableheader.sectionClicked.connect(self.sortbyHeader)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.setLabel()
        self.tableLoad()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.atlantaZooLabel.setText(_translate("Dialog", "Atlanta Zoo"))
        self.animalDetailLabel.setText(_translate("Dialog", "Animal Detail"))
        self.nameLabel.setText(_translate("Dialog", "Name:"))
        self.speciesLabel.setText(_translate("Dialog", "Species:"))
        self.exhibitLabel.setText(_translate("Dialog", "Exhibit:"))
        self.typeLabel.setText(_translate("Dialog", "Type:"))
        self.ageLabel.setText(_translate("Dialog", "Age:"))
        self.logNotePushButton.setText(_translate("Dialog", "Log Notes"))
        self.backButton.setText(_translate("Dialog", "Back"))
        self.nameOutputLabel.setText(_translate("Dialog", "TextLabel"))
        self.speciesOutputLabel.setText(_translate("Dialog", "TextLabel"))
        self.ageOutputLabel.setText(_translate("Dialog", "TextLabel"))
        self.exhibitOutputLabel.setText(_translate("Dialog", "TextLabel"))
        self.typeOutpuLabel.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(['AB', 'Human', 1, 'Mammal', 'Wild'], 'Staff1')
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

