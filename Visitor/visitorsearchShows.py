# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorsearchShowS.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from loadData import *
from Visitor.visitorexhibitDetail import Ui_exhibitDetail
from datetime import datetime

class Ui_searchShows(object):
    def __init__(self,username):
        object.__init__(self)
        self.connection = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',password = 'Al5qCS2i', user = 'cs4400_group59', db='cs4400_group59')
        self.username= username
        self.orderdict = {0: "asc", 1: "asc", 2: "asc"}
        self.sqlheaderList = ['Name', 'Location', 'datetime']
    def loadShow(self):


        query = "SELECT name, location, datetime from cs4400_group59.SHOW;"

        # print(query)

        cursor = self.connection.cursor()
        cursor.execute("USE cs4400_group59;")
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.showTable, result, ['Name', 'location', 'datetime'], 3)
        cursor.close()


    def logVisit(self):
        cursor = self.connection.cursor()
        show = self.showTable.selectedItems()
        if len(show) ==0:
            self.failedMessage("error", "Please select a show")
            return


        showname = show[0].text()
        showExhibit =  show[1].text()
        showtime = show[2].text()
        showtimeStrip = datetime.strptime(showtime, '%Y-%m-%d %H:%M:%S')
        curTime = datetime.now()

        query = "select * from cs4400_group59.SHOW where name = '{}';".format(showname)

        cursor.execute(query)
        foreignCheck = cursor.fetchall()
        query = "select * from cs4400_group59.SHOW_VISIT where SHOW_VISIT='{}' and visitor='{}' and datetime={{ts '{}'}};".format(showname, self.username, showtime)
        cursor.execute(query)
        primaryCheck = cursor.fetchall()

        if len(foreignCheck)==0:
            # warning! there is no such show
            self.failedMessage("error", "The show does not exist")
        elif len(primaryCheck)>0 :
            #warning! the visit is already in the list!
            self.failedMessage("error", "You have already been to the show")
        elif (showtimeStrip>curTime):
            self.failedMessage("error", "You can't log show visit of a show in the future")
        else:
            query = "insert into cs4400_group59.SHOW_VISIT values ('{}', '{}', {{ts '{}'}});".format(self.username, showname, showtime)
            #print(query)
            cursor.execute(query)
            self.connection.commit()

            query = "select * from cs4400_group59.EXHIBIT_VISIT where visitor ='{}' and exhibit = '{}' and datetime = {{ts '{}'}};".format(self.username, showExhibit, showtime)
            cursor.execute(query)
            result = cursor.fetchall()
            if len(result)==0:
                query = "insert into cs4400_group59.EXHIBIT_VISIT values ('{}', '{}', {{ts '{}'}});".format(self.username, showExhibit, showtime)
                cursor.execute(query)
                self.connection.commit()

    def sortbyHeader(self):
        i = self.tableheader.sortIndicatorSection()
        query = ("SELECT name, location, datetime from cs4400_group59.SHOW order by {} {};").format(self.sqlheaderList[i], self.orderdict[i])
        if self.orderdict[i] == "asc":
            self.orderdict[i]="desc"
        else:
            self.orderdict[i] = "asc"

        cursor=self.connection.cursor()
        cursor.execute(query)
        result=cursor.fetchall()
        loadTable(self.showTable, result, ['Name', 'locaiton', 'datetime'], 3)
        cursor.close()

    def showsSearch(self):
        showName = self.nameEdit.text()
        year = self.dateEdit.date().year()
        month = self.dateEdit.date().month()
        day = self.dateEdit.date().day()
        date = "{}-{}-{}".format(year, month, day)
        exhibit = self.exhibitBox.currentText()
        nextdate = "{}-{}-{}".format(year, month, day + 1)

        query = "SELECT name, location, datetime from cs4400_group59.SHOW where name like '%{}%' AND location like '%{}%' AND datetime>={{ts '{} 00:00'}} AND datetime<{{ts '{} 00:00'}}; ".format(
            showName, exhibit, date, nextdate)
        # query = "SELECT * from cs4400_group59.SHOW where name = '{}' AND location = '{}' AND datetime>={{ts '{} 00:00'}} AND datetime<{{ts '{} 00:00'}}; ".format(name, exhibit, date, nextdate)



    def loadBox(self):
        cursor = self.connection.cursor()
        cursor.execute("USE cs4400_group59;")
        query = "SELECT Name from EXHIBIT; "
        cursor.execute(query)
        result = cursor.fetchall()
        loadExhibit(self.exhibitBox, result)


    def showsSearch(self):
        showName= self.nameEdit.text()
        year = self.dateEdit.date().year()
        month = self.dateEdit.date().month()
        day = self.dateEdit.date().day()
        date = "{}-{}-{}".format(year, month, day)
        exhibit = self.exhibitBox.currentText()
        nextdate = "{}-{}-{}".format(year, month, day + 1)

        query = "SELECT name, location, datetime from cs4400_group59.SHOW where name like '%{}%' AND location like '%{}%' AND datetime>={{ts '{} 00:00'}} AND datetime<{{ts '{} 00:00'}}; ".format(
            showName, exhibit, date, nextdate)
        # query = "SELECT * from cs4400_group59.SHOW where name = '{}' AND location = '{}' AND datetime>={{ts '{} 00:00'}} AND datetime<{{ts '{} 00:00'}}; ".format(name, exhibit, date, nextdate)

        # print(query)

        cursor = self.connection.cursor()
        cursor.execute("USE cs4400_group59;")
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.showTable, result, ['Name', 'location', 'datetime'], 3)
        cursor.close()

    def exhibitDetail(self):
        exhibit = self.showTable.selectedItems()
        exhibit = exhibit[1].text()
        self.detailDialog = QtWidgets.QDialog()
        self.ui = Ui_exhibitDetail(exhibit, self.username)
        self.ui.setupUi(self.detailDialog)
        self.detailDialog.show()
    def failedMessage(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def setupUi(self, searchShows):
        searchShows.setObjectName("searchShows")
        searchShows.resize(611, 428)
        searchShows.setStyleSheet("background:rgb(237, 212, 0)")
        self.gridLayout = QtWidgets.QGridLayout(searchShows)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 0, 1, 1)
        self.exhibitLabel = QtWidgets.QLabel(searchShows)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exhibitLabel.setFont(font)
        self.exhibitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exhibitLabel.setObjectName("exhibitLabel")
        self.gridLayout.addWidget(self.exhibitLabel, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.searchButton = QtWidgets.QPushButton(searchShows)
        self.searchButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.showsSearch)
        self.gridLayout.addWidget(self.searchButton, 6, 4, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 7, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.dateLabel = QtWidgets.QLabel(searchShows)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel.setFont(font)
        self.dateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dateLabel.setObjectName("dateLabel")
        self.gridLayout.addWidget(self.dateLabel, 4, 4, 1, 1)
        self.showLabel = QtWidgets.QLabel(searchShows)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.showLabel.setFont(font)
        self.showLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showLabel.setObjectName("showLabel")
        self.gridLayout.addWidget(self.showLabel, 1, 1, 1, 6)
        self.zooLabel = QtWidgets.QLabel(searchShows)
        self.zooLabel.setObjectName("zooLabel")
        self.gridLayout.addWidget(self.zooLabel, 2, 1, 1, 2)
        self.exhibitBox = QtWidgets.QComboBox(searchShows)
        self.exhibitBox.setStyleSheet("background:rgb(238, 238, 236)")
        self.exhibitBox.setObjectName("exhibitBox")
        self.exhibitBox.addItem("")
        self.exhibitBox.setItemText(0, "")
        self.gridLayout.addWidget(self.exhibitBox, 5, 2, 1, 1)
        self.nameLabel = QtWidgets.QLabel(searchShows)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout.addWidget(self.nameLabel, 4, 1, 1, 1)
        self.showTable = QtWidgets.QTableWidget(searchShows)
        self.showTable.setStyleSheet("background:rgb(238, 238, 236)")
        self.showTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.showTable.setObjectName("showTable")
        self.showTable.setColumnCount(3)
        self.showTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.showTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.showTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.showTable.setHorizontalHeaderItem(2, item)
        self.showTable.horizontalHeader().setCascadingSectionResizes(True)
        self.showTable.horizontalHeader().setHighlightSections(False)
        self.showTable.horizontalHeader().setSortIndicatorShown(True)
        self.showTable.horizontalHeader().setStretchLastSection(True)
        self.showTable.verticalHeader().setVisible(True)
        self.showTable.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout.addWidget(self.showTable, 8, 1, 1, 6)
        self.nameEdit = QtWidgets.QLineEdit(searchShows)
        self.nameEdit.setStyleSheet("background:rgb(238, 238, 236)")
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 4, 2, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(searchShows)
        self.dateEdit.setStyleSheet("background:rgb(238, 238, 236)")
        self.dateEdit.setProperty("showGroupSeparator", False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setTimeSpec(QtCore.Qt.UTC)
        self.dateEdit.setDate(QtCore.QDate(2018, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 4, 5, 1, 2)
        self.logvisitButton = QtWidgets.QPushButton(searchShows)
        self.logvisitButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.logvisitButton.setObjectName("logvisitButton")
        self.logvisitButton.clicked.connect(self.logVisit)
        self.gridLayout.addWidget(self.logvisitButton, 9, 4, 1, 2)
        self.backButton = QtWidgets.QPushButton(searchShows)
        self.backButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.backButton.setObjectName("backButton")
        self.gridLayout.addWidget(self.backButton, 9, 6, 1, 1)
        self.backButton.clicked.connect(searchShows.reject)
        self.tableheader = self.showTable.horizontalHeader()
        self.tableheader.sectionClicked.connect(self.sortbyHeader)
        self.retranslateUi(searchShows)

        QtCore.QMetaObject.connectSlotsByName(searchShows)
        self.loadBox()
        self.loadShow()

        self.showTable.doubleClicked.connect(self.exhibitDetail)
    def retranslateUi(self, searchShows):
        _translate = QtCore.QCoreApplication.translate
        searchShows.setWindowTitle(_translate("searchShows", "Dialog"))
        self.exhibitLabel.setText(_translate("searchShows", "Exhibit"))
        self.searchButton.setText(_translate("searchShows", "Search"))
        self.dateLabel.setText(_translate("searchShows", "Date"))
        self.showLabel.setText(_translate("searchShows", "Shows"))
        self.zooLabel.setText(_translate("searchShows", "Atlanta Zoo"))
        self.nameLabel.setText(_translate("searchShows", "Name"))
        item = self.showTable.horizontalHeaderItem(0)
        item.setText(_translate("searchShows", "Name"))
        item = self.showTable.horizontalHeaderItem(1)
        item.setText(_translate("searchShows", "Exhibit"))
        item = self.showTable.horizontalHeaderItem(2)
        item.setText(_translate("searchShows", "Data"))
        self.logvisitButton.setText(_translate("searchShows", "Log Visit"))
        self.backButton.setText(_translate("searchShows", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searchShows = QtWidgets.QDialog()
    ui = Ui_searchShows('hello')
    ui.setupUi(searchShows)
    searchShows.show()
    sys.exit(app.exec_())

