# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorexhibitHistory.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from loadData import *
from Visitor.visitorexhibitDetail import Ui_exhibitDetail
class Ui_exhibitHistory(object):


    def __init__(self, username):
        self.username = username
        self.connection = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',password = 'Al5qCS2i', user = 'cs4400_group59', db='cs4400_group59')
        self.sqlheaderList = ["a.Exhibit", "a.datetime", "visitedNum"]
        self.orderdict = {0: "asc", 1: "asc", 2: "asc"}

    def exhibitDetail(self):
        exhibit = self.exhibitTable.selectedItems()
        exhibit = exhibit[0].text()
        self.detailDialog = QtWidgets.QDialog()
        self.ui = Ui_exhibitDetail(exhibit, self.username)
        self.ui.setupUi(self.detailDialog)
        self.detailDialog.show()
    def sortbyHeader(self):
        i = self.tableheader.sortIndicatorSection()
        query = ("select a.Exhibit, a.datetime, visitedNum from cs4400_group59.EXHIBIT_VISIT as a, (select EXHIBIT_VISIT.exhibit, EXHIBIT_VISIT.visitor, count(*) as visitedNum from cs4400_group59.EXHIBIT_VISIT where visitor='{}'"
                 " group by EXHIBIT_VISIT.exhibit) as b where a.exhibit = b.exhibit and a.visitor = b.visitor "
                 "order by {} {};").format(self.username, self.sqlheaderList[i], self.orderdict[i])
        if self.orderdict[i] == "asc":
            self.orderdict[i]="desc"
        else:
            self.orderdict[i] = "asc"

        cursor=self.connection.cursor()
        cursor.execute(query)
        result=cursor.fetchall()
        loadTable(self.exhibitTable, result, ['Name', 'Time', 'Number of Visits'], 3)
        cursor.close()

    def loadHistory(self):
        cursor = self.connection.cursor()
        query = ("select a.Exhibit, a.datetime, visitedNum from cs4400_group59.EXHIBIT_VISIT as a, (select EXHIBIT_VISIT.exhibit, EXHIBIT_VISIT.visitor, count(*) as visitedNum from cs4400_group59.EXHIBIT_VISIT where visitor='{}'"
                 " group by EXHIBIT_VISIT.exhibit) as b where a.exhibit = b.exhibit and a.visitor = b.visitor;").format(self.username)
        cursor.execute(query)
        result= cursor.fetchall()
        loadTable(self.exhibitTable, result, ["Name", "Time", 'Number of Visits'], 3)

    def searchHistory(self):
        exhibitName= self.nameEdit.text()
        visitMin = self.nminBox.value()
        visitMax = self.nmaxBox.value()
        year = self.timeEdit.date().year()
        month = self.timeEdit.date().month()
        day = self.timeEdit.date().day()
        date = "{}-{}-{}".format(year, month, day)
        nextdate = "{}-{}-{}".format(year, month, day + 1)
        query = ("select a.Exhibit, a.datetime, visitedNum from cs4400_group59.EXHIBIT_VISIT as a, (select EXHIBIT_VISIT.exhibit, EXHIBIT_VISIT.visitor, count(*) as visitedNum from cs4400_group59.EXHIBIT_VISIT where visitor='{}' group by EXHIBIT_VISIT.exhibit) "
                 "as b where a.exhibit = b.exhibit and a.visitor = b.visitor and a.exhibit like '%{}%' and datetime>= {{ts '{}'}} and datetime<= {{ts '{}'}} and visitedNum >={} and visitedNum <={};").format(self.username, exhibitName, date, nextdate, visitMin, visitMax)
        cursor=self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.exhibitTable, result, ["Name", "Time", 'Number of Visits'], 3)
        cursor.close()

    def setupUi(self, exhibitHistory):
        exhibitHistory.setObjectName("exhibitHistory")
        exhibitHistory.resize(611, 453)
        exhibitHistory.setStyleSheet("background:rgb(237, 212, 0)")
        self.gridLayout = QtWidgets.QGridLayout(exhibitHistory)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.zooLabel = QtWidgets.QLabel(exhibitHistory)
        self.zooLabel.setObjectName("zooLabel")
        self.gridLayout.addWidget(self.zooLabel, 2, 1, 1, 2)
        self.visitsLabel = QtWidgets.QLabel(exhibitHistory)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.visitsLabel.setFont(font)
        self.visitsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.visitsLabel.setObjectName("visitsLabel")
        self.gridLayout.addWidget(self.visitsLabel, 4, 4, 1, 1)
        self.exhibitLabel = QtWidgets.QLabel(exhibitHistory)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.exhibitLabel.setFont(font)
        self.exhibitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exhibitLabel.setObjectName("exhibitLabel")
        self.gridLayout.addWidget(self.exhibitLabel, 1, 1, 1, 6)
        self.searchButton = QtWidgets.QPushButton(exhibitHistory)
        self.searchButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.searchHistory)

        self.gridLayout.addWidget(self.searchButton, 6, 4, 1, 2)
        self.timeLabel = QtWidgets.QLabel(exhibitHistory)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.gridLayout.addWidget(self.timeLabel, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 7, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.nameLabel = QtWidgets.QLabel(exhibitHistory)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 4, 1, 1, 1)
        self.nmaxBox = QtWidgets.QSpinBox(exhibitHistory)
        self.nmaxBox.setStyleSheet("background:rgb(238, 238, 236)")
        self.nmaxBox.setMaximum(5000)
        self.nmaxBox.setObjectName("nmaxBox")
        self.gridLayout.addWidget(self.nmaxBox, 4, 6, 1, 1)
        self.timeEdit = QtWidgets.QDateEdit(exhibitHistory)
        self.timeEdit.setStyleSheet("background:rgb(238, 238, 236)")
        self.timeEdit.setCalendarPopup(True)
        self.timeEdit.setTimeSpec(QtCore.Qt.UTC)
        self.timeEdit.setDate(QtCore.QDate(2018, 1, 1))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 5, 2, 1, 1)
        self.nminLabel = QtWidgets.QLabel(exhibitHistory)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nminLabel.setFont(font)
        self.nminLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nminLabel.setObjectName("nminLabel")
        self.gridLayout.addWidget(self.nminLabel, 2, 5, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 10, 0, 1, 1)
        self.nminBox = QtWidgets.QSpinBox(exhibitHistory)
        self.nminBox.setStyleSheet("background:rgb(238, 238, 236)")
        self.nminBox.setMaximum(5000)
        self.nminBox.setObjectName("nminBox")
        self.gridLayout.addWidget(self.nminBox, 4, 5, 1, 1)
        self.nmaxLabel = QtWidgets.QLabel(exhibitHistory)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nmaxLabel.setFont(font)
        self.nmaxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nmaxLabel.setObjectName("nmaxLabel")
        self.gridLayout.addWidget(self.nmaxLabel, 2, 6, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(exhibitHistory)
        self.nameEdit.setStyleSheet("background:rgb(238, 238, 236)")
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 4, 2, 1, 1)
        self.exhibitTable = QtWidgets.QTableWidget(exhibitHistory)
        self.exhibitTable.setStyleSheet("background:rgb(238, 238, 236)")
        self.exhibitTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.exhibitTable.setObjectName("exhibitTable")
        self.exhibitTable.setColumnCount(3)
        self.exhibitTable.setRowCount(0)
        self.exhibitTable.doubleClicked.connect(self.exhibitDetail)

        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.exhibitTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.exhibitTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.exhibitTable.setHorizontalHeaderItem(2, item)
        self.exhibitTable.horizontalHeader().setCascadingSectionResizes(True)
        self.exhibitTable.horizontalHeader().setHighlightSections(False)
        self.exhibitTable.horizontalHeader().setSortIndicatorShown(True)
        self.exhibitTable.horizontalHeader().setStretchLastSection(True)
        self.exhibitTable.verticalHeader().setVisible(True)
        self.exhibitTable.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.exhibitTable, 8, 1, 1, 6)
        self.backButton = QtWidgets.QPushButton(exhibitHistory)
        self.backButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 9, 6, 1, 1)
        self.backButton.clicked.connect(exhibitHistory.reject)

        self.retranslateUi(exhibitHistory)
        QtCore.QMetaObject.connectSlotsByName(exhibitHistory)
        self.tableheader = self.exhibitTable.horizontalHeader()
        self.tableheader.sectionClicked.connect(self.sortbyHeader)
        self.loadHistory()

    def retranslateUi(self, exhibitHistory):
        _translate = QtCore.QCoreApplication.translate
        exhibitHistory.setWindowTitle(_translate("exhibitHistory", "Dialog"))
        self.zooLabel.setText(_translate("exhibitHistory", "Atlanta Zoo"))
        self.visitsLabel.setText(_translate("exhibitHistory", "Number of Visits"))
        self.exhibitLabel.setText(_translate("exhibitHistory", "Exhibit History"))
        self.searchButton.setText(_translate("exhibitHistory", "Search"))
        self.timeLabel.setText(_translate("exhibitHistory", "Time"))
        self.nameLabel.setText(_translate("exhibitHistory", "Name"))
        self.nminLabel.setText(_translate("exhibitHistory", "Min"))
        self.nmaxLabel.setText(_translate("exhibitHistory", "Max"))
        item = self.exhibitTable.horizontalHeaderItem(0)
        item.setText(_translate("exhibitHistory", "Name"))
        item = self.exhibitTable.horizontalHeaderItem(1)
        item.setText(_translate("exhibitHistory", "Time"))
        item = self.exhibitTable.horizontalHeaderItem(2)
        item.setText(_translate("exhibitHistory", "Number of Visits"))
        self.backButton.setText(_translate("exhibitHistory", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    exhibitHistory = QtWidgets.QDialog()
    ui = Ui_exhibitHistory('Junho')
    ui.setupUi(exhibitHistory)
    exhibitHistory.show()
    sys.exit(app.exec_())
