# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visitorsearchExhibit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from loadData import *
from Visitor.visitorexhibitDetail import Ui_exhibitDetail


class Ui_searchExhibit(object):
    def __init__(self, username):
        object.__init__(self)
        self.connection = pymysql.connect(host = 'academic-mysql.cc.gatech.edu',password = 'Al5qCS2i', user = 'cs4400_group59', db='cs4400_group59')
        self.username = username

        self.nameOrder = True
        self.sizeOrder = True
        self.numAnimalOrder = True
        self.waterFeatureOrder = True
        self.orderdict = {0: "asc", 1: "asc", 2: "asc", 3: "asc"}
        self.sqlheaderList = ['Name', 'Size', 'NumAnimals', 'Water_Feature']

    def sortbyHeader(self):
        i = self.tableheader.sortIndicatorSection()
        query = ("select Name, Size, numAnimals, IF(Water_Feature, 'Yes', 'No')Water_Feature  from cs4400_group59.EXHIBIT join"
                 " (select count(*) as numAnimals, ANIMAL.EXHIBIT from cs4400_group59.ANIMAL group by ANIMAL.EXHIBIT) as a "
                 "on EXHIBIT.name = a.EXHIBIT order by {} {};").format(self.sqlheaderList[i], self.orderdict[i])
        if self.orderdict[i] == "asc":
            self.orderdict[i] = "desc"
        else:
            self.orderdict[i] = "asc"

        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.exhibitTable, result, ['Name', 'Size', 'NumAnimals', 'Water'], 4)
        cursor.close()

    def exhibitSearch(self):
        exhibitName = self.nameEdit.text()
        numMin = self.nminBox.value()
        numMax = self.nmaxBox.value()
        sizeMin = self.sminBox.value()
        sizeMax = self.smaxBox.value()
        water = self.waterBox.currentText()
        cursor = self.connection.cursor()
        cursor.execute("USE cs4400_group59;")
        query = ""

        if water == "No":
            query = (
                "select Name, Size, numAnimals, IF(Water_Feature, 'yes', 'no') Water_Feature  from cs4400_group59.EXHIBIT join (select count(*) as numAnimals, ANIMAL.EXHIBIT from cs4400_group59.ANIMAL group by ANIMAL.EXHIBIT) as a on EXHIBIT.name = a.exhibit where name like '%{}%' and size>={} and size<={} and numAnimals>={} and numAnimals<={} and water_feature = {};").format(
                exhibitName, sizeMin, sizeMax, numMin, numMax, 'False')
        elif water == "Yes":
            query = (
                "select Name, Size, numAnimals, IF(Water_Feature, 'yes', 'no') Water_Feature  from cs4400_group59.EXHIBIT join (select count(*) as numAnimals, ANIMAL.EXHIBIT from cs4400_group59.ANIMAL group by ANIMAL.EXHIBIT) as a on EXHIBIT.name = a.exhibit where name like '%{}%' and size>={} and size<={} and numAnimals>={} and numAnimals<={} and water_feature = {};").format(
                exhibitName, sizeMin, sizeMax, numMin, numMax, 'True')
        else:
            query = (
                        "select Name, Size, numAnimals, IF(Water_Feature, 'yes', 'no') Water_Feature  from cs4400_group59.EXHIBIT join" +
                        " (select count(*) as numAnimals, ANIMAL.EXHIBIT from cs4400_group59.ANIMAL group by ANIMAL.EXHIBIT) as a " +
                        "on EXHIBIT.name = a.EXHIBIT where name like '%{}%' and size>={} and size<={} and numAnimals>={} " +
                        "and numAnimals<={};").format(exhibitName, sizeMin, sizeMax, numMin, numMax)

        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.exhibitTable, result, ['Name', 'Size', 'NumAnimals', 'Water'], 4)
        cursor.close()

    def loadExhibit(self):
        cursor = self.connection.cursor()
        query = ("select Name, Size, numAnimals, IF(Water_Feature, 'yes', 'no') Water_Feature  from cs4400_group59.EXHIBIT join"
                 " (select count(*) as numAnimals, ANIMAL.EXHIBIT from cs4400_group59.ANIMAL group by ANIMAL.EXHIBIT) as a "
                 "on EXHIBIT.name = a.EXHIBIT;")
        cursor.execute(query)
        result = cursor.fetchall()
        loadTable(self.exhibitTable, result, ['Name', 'Size', 'NumAnimals', 'Water'], 4)
        cursor.close()

    def exhibitDetail(self):

        exhibit = self.exhibitTable.selectedItems()
        exhibit = exhibit[0].text()
        self.detailDialog = QtWidgets.QDialog()
        self.ui = Ui_exhibitDetail(exhibit, self.username)
        self.ui.setupUi(self.detailDialog)
        self.detailDialog.show()

    def setupUi(self, searchExhibit):
        searchExhibit.setObjectName("searchExhibit")
        searchExhibit.resize(606, 440)
        searchExhibit.setStyleSheet("background:rgb(237, 212, 0)")
        self.gridLayout_2 = QtWidgets.QGridLayout(searchExhibit)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.waterBox = QtWidgets.QComboBox(searchExhibit)
        self.waterBox.setStyleSheet("background:rgb(238, 238, 236)")
        self.waterBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.waterBox.setMinimumContentsLength(0)
        self.waterBox.setIconSize(QtCore.QSize(16, 16))
        self.waterBox.setObjectName("waterBox")
        self.waterBox.addItem("")
        self.waterBox.setItemText(0, "")
        self.waterBox.addItem("")
        self.waterBox.addItem("")
        self.gridLayout_2.addWidget(self.waterBox, 9, 8, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)
        self.nmaxBox = QtWidgets.QSpinBox(searchExhibit)
        self.nmaxBox.setStyleSheet("background:rgb(238, 238, 236)")
        self.nmaxBox.setMaximum(5000)
        self.nmaxBox.setObjectName("nmaxBox")
        self.gridLayout_2.addWidget(self.nmaxBox, 7, 9, 1, 1)
        self.zooLabel = QtWidgets.QLabel(searchExhibit)
        self.zooLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.zooLabel.setObjectName("zooLabel")
        self.gridLayout_2.addWidget(self.zooLabel, 6, 1, 1, 4)
        self.nminBox = QtWidgets.QSpinBox(searchExhibit)
        self.nminBox.setStyleSheet("background:rgb(238, 238, 236)")
        self.nminBox.setMaximum(5000)
        self.nminBox.setObjectName("nminBox")
        self.gridLayout_2.addWidget(self.nminBox, 7, 8, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 16, 6, 1, 1)
        self.exhibitLabel = QtWidgets.QLabel(searchExhibit)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.exhibitLabel.setFont(font)
        self.exhibitLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exhibitLabel.setIndent(-1)
        self.exhibitLabel.setObjectName("exhibitLabel")
        self.gridLayout_2.addWidget(self.exhibitLabel, 3, 1, 1, 9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 6, 1, 1)
        self.maxLabel = QtWidgets.QLabel(searchExhibit)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.maxLabel.setFont(font)
        self.maxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.maxLabel.setObjectName("maxLabel")
        self.gridLayout_2.addWidget(self.maxLabel, 8, 3, 1, 1)
        self.sizeLabel = QtWidgets.QLabel(searchExhibit)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sizeLabel.setFont(font)
        self.sizeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout_2.addWidget(self.sizeLabel, 9, 1, 1, 1)
        self.waterLabel = QtWidgets.QLabel(searchExhibit)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.waterLabel.setFont(font)
        self.waterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.waterLabel.setObjectName("waterLabel")
        self.gridLayout_2.addWidget(self.waterLabel, 9, 7, 1, 1)
        self.numLabel = QtWidgets.QLabel(searchExhibit)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.numLabel.setFont(font)
        self.numLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numLabel.setObjectName("numLabel")
        self.gridLayout_2.addWidget(self.numLabel, 7, 7, 1, 1)
        self.nmaxLabel = QtWidgets.QLabel(searchExhibit)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nmaxLabel.setFont(font)
        self.nmaxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nmaxLabel.setObjectName("nmaxLabel")
        self.gridLayout_2.addWidget(self.nmaxLabel, 6, 9, 1, 1)
        self.sminLabel = QtWidgets.QLabel(searchExhibit)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sminLabel.setFont(font)
        self.sminLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sminLabel.setObjectName("sminLabel")
        self.gridLayout_2.addWidget(self.sminLabel, 8, 2, 1, 1)
        self.nameLabel = QtWidgets.QLabel(searchExhibit)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.gridLayout_2.addWidget(self.nameLabel, 7, 1, 1, 1)
        self.sminBox = QtWidgets.QSpinBox(searchExhibit)
        self.sminBox.setStyleSheet("background:rgb(238, 238, 236)")
        self.sminBox.setMaximum(5000)
        self.sminBox.setSingleStep(50)
        self.sminBox.setObjectName("sminBox")
        self.gridLayout_2.addWidget(self.sminBox, 9, 2, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(searchExhibit)
        self.nameEdit.setEnabled(True)
        self.nameEdit.setAcceptDrops(False)
        self.nameEdit.setAutoFillBackground(False)
        self.nameEdit.setStyleSheet("background:rgb(238, 238, 236)")
        self.nameEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nameEdit.setClearButtonEnabled(False)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_2.addWidget(self.nameEdit, 7, 2, 1, 2)
        self.searchButton = QtWidgets.QPushButton(searchExhibit)
        self.searchButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.searchButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.exhibitSearch)
        self.gridLayout_2.addWidget(self.searchButton, 11, 7, 1, 1)
        self.nminLabel = QtWidgets.QLabel(searchExhibit)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nminLabel.setFont(font)
        self.nminLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nminLabel.setObjectName("nminLabel")
        self.gridLayout_2.addWidget(self.nminLabel, 6, 8, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 10, 1, 1)
        self.smaxBox = QtWidgets.QSpinBox(searchExhibit)
        self.smaxBox.setStyleSheet("background:rgb(238, 238, 236)")
        self.smaxBox.setMaximum(5000)
        self.smaxBox.setSingleStep(50)
        self.smaxBox.setObjectName("smaxBox")
        self.gridLayout_2.addWidget(self.smaxBox, 9, 3, 1, 1)
        self.exhibitTable = QtWidgets.QTableWidget(searchExhibit)
        self.exhibitTable.setStyleSheet("background:rgb(238, 238, 236)")
        self.exhibitTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.exhibitTable.setObjectName("exhibitTable")
        self.exhibitTable.setColumnCount(4)
        self.exhibitTable.setRowCount(0)
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
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.exhibitTable.setHorizontalHeaderItem(3, item)
        self.exhibitTable.horizontalHeader().setCascadingSectionResizes(False)
        self.exhibitTable.horizontalHeader().setSortIndicatorShown(False)
        self.exhibitTable.horizontalHeader().setStretchLastSection(True)
        self.exhibitTable.verticalHeader().setVisible(False)
        self.exhibitTable.verticalHeader().setCascadingSectionResizes(False)
        self.exhibitTable.verticalHeader().setSortIndicatorShown(False)
        self.exhibitTable.verticalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.exhibitTable, 14, 1, 1, 9)
        self.backButton = QtWidgets.QPushButton(searchExhibit)
        self.backButton.setStyleSheet("background:rgb(186, 189, 182)")
        self.backButton.setObjectName("backButton")
        self.gridLayout_2.addWidget(self.backButton, 15, 9, 1, 1)
        self.backButton.clicked.connect(searchExhibit.reject)

        self.retranslateUi(searchExhibit)
        QtCore.QMetaObject.connectSlotsByName(searchExhibit)
        self.tableheader = self.exhibitTable.horizontalHeader()
        self.tableheader.sectionClicked.connect(self.sortbyHeader)

        self.exhibitTable.doubleClicked.connect(self.exhibitDetail)

        self.loadExhibit()

    def retranslateUi(self, searchExhibit):
        _translate = QtCore.QCoreApplication.translate
        searchExhibit.setWindowTitle(_translate("searchExhibit", "Dialog"))
        self.waterBox.setItemText(1, _translate("searchExhibit", "Yes"))
        self.waterBox.setItemText(2, _translate("searchExhibit", "No"))
        self.zooLabel.setText(_translate("searchExhibit", "Atlanta Zoo"))
        self.exhibitLabel.setText(_translate("searchExhibit", "Exhibits"))
        self.maxLabel.setText(_translate("searchExhibit", "Max"))
        self.sizeLabel.setText(_translate("searchExhibit", "Size"))
        self.waterLabel.setText(_translate("searchExhibit", "Water Feature"))
        self.numLabel.setText(_translate("searchExhibit", "Num Animals"))
        self.nmaxLabel.setText(_translate("searchExhibit", "Max"))
        self.sminLabel.setText(_translate("searchExhibit", "Min"))
        self.nameLabel.setText(_translate("searchExhibit", "Name"))
        self.searchButton.setText(_translate("searchExhibit", "Search"))
        self.nminLabel.setText(_translate("searchExhibit", "Min"))
        self.exhibitTable.setSortingEnabled(False)
        item = self.exhibitTable.horizontalHeaderItem(0)
        item.setText(_translate("searchExhibit", "Name"))
        item = self.exhibitTable.horizontalHeaderItem(1)
        item.setText(_translate("searchExhibit", "Size"))
        item = self.exhibitTable.horizontalHeaderItem(2)
        item.setText(_translate("searchExhibit", "Num Animals"))
        item = self.exhibitTable.horizontalHeaderItem(3)
        item.setText(_translate("searchExhibit", "Water"))
        self.backButton.setText(_translate("searchExhibit", "Back"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    searchExhibit = QtWidgets.QDialog()
    ui = Ui_searchExhibit("Junho")
    ui.setupUi(searchExhibit)
    searchExhibit.show()
    sys.exit(app.exec_())

