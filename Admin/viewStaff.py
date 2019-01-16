# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewstaffTablestaff.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtSql import *
import pymysql
# import adminfunc
from loadData import loadTable



class Ui_viewStaffDialouge(object):

    def __init__(self):
        object.__init__(self)


        self.connection = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',password = 'Al5qCS2i', user = 'cs4400_group59', db='cs4400_group59')
        self.sqlheaderList = ['username', 'email']
        self.orderdict = ['asc', 'asc']

    def loaddata(self):
        cursor = self.connection.cursor()
        cursor.execute("USE cs4400_group59;")
        query = "SELECT username, email from USER NATURAL JOIN STAFF; "
        cursor.execute(query)
        result = cursor.fetchall()
        # self.staffTable.setRowCount(0)
        # self.staffTable.setColumnCount(2)
        # self.staffTable.setHorizontalHeaderLabels(['Username', 'Email'])
        # for row_number, row_data in enumerate(result):
        #     #first we insert a row then the data is inserted
        #     self.staffTable.insertRow(row_number)
        #     for column_number, data in enumerate(row_data):
        #         self.staffTable.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
        loadTable(table=self.staffTable,querydata= result,header= ['Username', 'Email'], attNo=2)

    def sortbyHeader(self):
        i = self.tableheader.sortIndicatorSection()
        query = "SELECT username, email from USER NATURAL JOIN STAFF order by {} {}; ".format(
            self.sqlheaderList[i], self.orderdict[i])
        if self.orderdict[i] == "asc":
            self.orderdict[i] = "desc"
        else:
            self.orderdict[i] = "asc"

        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.staffTable, result, ['Username', 'Email'], 2)
        cursor.close()

        # self.db.close()
    def deletestaff(self):
        cursor = self.connection.cursor()
        cursor.execute("USE cs4400_group59;")

        deletedstaff = self.staffTable.selectedItems()
        staffToText = []

        for i in range(0,len(deletedstaff),2):
            staffToText.append(deletedstaff[i].text())
        for staff in staffToText:
            query = "DELETE FROM USER WHERE username = "+"'"+staff+"'"
            cursor.execute(query)
            result=cursor.fetchall()
        self.connection.commit()
        self.loaddata()

        #type of deleted staffTablestaff is QTableWidgetItem. So no I am going to change this to a list of strings.

        # requires a function to delete a staff


    def back(self):
        print("back")
        # requires a function to go back to the previous screen

    def setupUi(self, viewstaffTablestaffDialouge):
        viewstaffTablestaffDialouge.setObjectName("viewstaffTablestaffDialouge")
        viewstaffTablestaffDialouge.resize(800, 600)

        self.atlantaZooLabel = QtWidgets.QLabel(viewstaffTablestaffDialouge)
        self.atlantaZooLabel.setGeometry(QtCore.QRect(50, 30, 150, 30))
        self.atlantaZooLabel.setObjectName("Atlanta Zoo")

        self.viewstaffTablestaffLabel = QtWidgets.QLabel(viewstaffTablestaffDialouge)
        self.viewstaffTablestaffLabel.setGeometry(QtCore.QRect(400, 30, 150, 30))
        self.viewstaffTablestaffLabel.setObjectName("View Staff")

        self.staffTable = QtWidgets.QTableWidget(viewstaffTablestaffDialouge)
        self.staffTable.setGeometry(QtCore.QRect(50, 80, 700, 400 ))
        self.staffTable.setObjectName("staffTable")
        self.staffTable.setAlternatingRowColors(True)
        self.staffTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)


        self.staffTable.setColumnCount(2)
        self.staffTable.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.staffTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.staffTable.setHorizontalHeaderItem(1, item)
        self.staffTable.horizontalHeader().setVisible(True)
        self.staffTable.verticalHeader().setVisible(False)
        self.loaddata()







        self.deletestaffButton = QtWidgets.QPushButton(viewstaffTablestaffDialouge)
        self.deletestaffButton.setGeometry(QtCore.QRect(100, 500, 150, 40))
        self.deletestaffButton.setObjectName("deletestaffButton")
        self.deletestaffButton.clicked.connect(self.deletestaff)


        self.backButton = QtWidgets.QPushButton(viewstaffTablestaffDialouge)
        self.backButton.setGeometry(QtCore.QRect(300, 500, 150, 40))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(viewstaffTablestaffDialouge.reject)

        self.retranslateUi(viewstaffTablestaffDialouge)
        QtCore.QMetaObject.connectSlotsByName(viewstaffTablestaffDialouge)
        self.tableheader = self.staffTable.horizontalHeader()
        self.tableheader.sectionClicked.connect(self.sortbyHeader)

    def retranslateUi(self, viewstaffTablestaffDialouge):
        _translate = QtCore.QCoreApplication.translate
        viewstaffTablestaffDialouge.setWindowTitle(_translate("viewstaffTablestaffDialouge", "Dialog"))
        self.atlantaZooLabel.setText(_translate("viewstaffTablestaffDialouge", "Atlanta Zoo"))
        self.viewstaffTablestaffLabel.setText(_translate("viewstaffTablestaffDialouge", "View staffTablestaff"))
        self.deletestaffButton.setText(_translate("viewstaffTablestaffDialouge", "Delete staff"))
        self.backButton.setText(_translate("viewstaffTablestaffDialouge", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewstaffTablestaffDialouge = QtWidgets.QDialog()
    ui = Ui_viewStaffDialouge()
    ui.setupUi(viewstaffTablestaffDialouge)
    viewstaffTablestaffDialouge.show()
    sys.exit(app.exec_())

