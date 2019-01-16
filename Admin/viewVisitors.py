# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewVisitors.ui'
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



class Ui_viewVisitorsDialouge(object):

    def __init__(self):
        object.__init__(self)

        self.connection = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',password = 'Al5qCS2i', user = 'cs4400_group59', db='cs4400_group59')

        self.sqlheaderList = ['username', 'email']
        self.orderdict = ['asc', 'asc']
    def sortbyHeader(self):
        i = self.tableheader.sortIndicatorSection()
        query =  "SELECT username, email from USER NATURAL JOIN VISITOR order by {} {}; ".format(self.sqlheaderList[i], self.orderdict[i])
        if self.orderdict[i] == "asc":
            self.orderdict[i] = "desc"
        else:
            self.orderdict[i] = "asc"

        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.visitorsTable, result, ['Username', 'Email'], 2)
        cursor.close()
    def loaddata(self):
        cursor = self.connection.cursor()
        cursor.execute("USE cs4400_group59;")
        query = "SELECT username, email from USER NATURAL JOIN VISITOR; "
        cursor.execute(query)
        result = cursor.fetchall()
        # self.visitorsTable.setRowCount(0)
        # self.visitorsTable.setColumnCount(2)
        # self.visitorsTable.sethorizontalHeaderLabels(['Username', 'Email'])
        # for row_number, row_data in enumerate(result):
        #     #first we insert a row then the data is inserted
        #     self.visitorsTable.insertRow(row_number)
        #     for column_number, data in enumerate(row_data):
        #         self.visitorsTable.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(data)))
        loadTable(self.visitorsTable, result, ['Username', 'Email'], 2)





        # self.db.close()
    def deleteVisitor(self):
        cursor = self.connection.cursor()
        cursor.execute("USE cs4400_group59;")
        deletedVisitors = self.visitorsTable.selectedItems()
        visitorsToText = []

        for i in range(0,len(deletedVisitors),2):
            visitorsToText.append(deletedVisitors[i].text())
        for visitor in visitorsToText:
            query = "DELETE FROM USER WHERE username = "+"'"+visitor+"'"
            cursor.execute(query)
            result=cursor.fetchall()
        self.connection.commit()
        self.loaddata()

        #type of deleted visitors is QTableWidgetItem. So no I am going to change this to a list of strings.

        # requires a function to delete a visitor


    def back(self):
        print("back")
        # requires a function to go back to the previous screen

    def setupUi(self, viewVisitorsDialouge):
        viewVisitorsDialouge.setObjectName("viewVisitorsDialouge")
        viewVisitorsDialouge.resize(800, 600)

        self.atlantaZooLabel = QtWidgets.QLabel(viewVisitorsDialouge)
        self.atlantaZooLabel.setGeometry(QtCore.QRect(50, 30, 150, 30))
        self.atlantaZooLabel.setObjectName("Atlanta Zoo")

        self.viewVisitorsLabel = QtWidgets.QLabel(viewVisitorsDialouge)
        self.viewVisitorsLabel.setGeometry(QtCore.QRect(300, 30, 150, 30))
        self.viewVisitorsLabel.setObjectName("View Visitors")

        self.visitorsTable = QtWidgets.QTableWidget(viewVisitorsDialouge)
        self.visitorsTable.setGeometry(QtCore.QRect(50, 80, 700, 400 ))
        self.visitorsTable.setObjectName("visitorsTable")
        self.visitorsTable.setAlternatingRowColors(True)
        self.visitorsTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)


        self.visitorsTable.setColumnCount(2)
        self.visitorsTable.setRowCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.visitorsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.visitorsTable.setHorizontalHeaderItem(1, item)
        self.visitorsTable.horizontalHeader().setVisible(True)
        self.visitorsTable.verticalHeader().setVisible(False)
        self.loaddata()







        self.deleteVisitorButton = QtWidgets.QPushButton(viewVisitorsDialouge)
        self.deleteVisitorButton.setGeometry(QtCore.QRect(100, 500, 90, 30))
        self.deleteVisitorButton.setObjectName("deleteVisitorButton")
        self.deleteVisitorButton.clicked.connect(self.deleteVisitor)


        self.backButton = QtWidgets.QPushButton(viewVisitorsDialouge)
        self.backButton.setGeometry(QtCore.QRect(500, 500, 90, 30))
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(viewVisitorsDialouge.reject)

        self.retranslateUi(viewVisitorsDialouge)
        QtCore.QMetaObject.connectSlotsByName(viewVisitorsDialouge)
        self.tableheader = self.visitorsTable.horizontalHeader()
        self.tableheader.sectionClicked.connect(self.sortbyHeader)

    def retranslateUi(self, viewVisitorsDialouge):
        _translate = QtCore.QCoreApplication.translate
        viewVisitorsDialouge.setWindowTitle(_translate("viewVisitorsDialouge", "Dialog"))
        self.atlantaZooLabel.setText(_translate("viewVisitorsDialouge", "Atlanta Zoo"))
        self.viewVisitorsLabel.setText(_translate("viewVisitorsDialouge", "View Visitors"))
        self.deleteVisitorButton.setText(_translate("viewVisitorsDialouge", "Delete Visitor"))
        self.backButton.setText(_translate("viewVisitorsDialouge", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewVisitorsDialouge = QtWidgets.QDialog()
    ui = Ui_viewVisitorsDialouge()
    ui.setupUi(viewVisitorsDialouge)
    viewVisitorsDialouge.show()
    sys.exit(app.exec_())

