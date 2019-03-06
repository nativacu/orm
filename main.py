# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Manue\Desktop\ormTest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem
from PyQt5.QtCore import pyqtSlot

from peewee import *

peewee = PostgresqlDatabase(
    'postgres',
    user='postgres',
    password='postgre',
    host='localhost')

peewee._connect();


class address(Model):
    #id = AutoField()
    street = CharField()
    city = CharField(100)
    province = CharField(100)
    country = CharField(100)
    postcode = CharField(50)

    class Meta:
        database = peewee


class employee(Model):
    id = AutoField()
    firstName = CharField()
    lastName = CharField()
    salary = DecimalField(10, 2)
    startDate = DateField()
    endDate = DateField()
    # managerId = ForeignKeyField(employee, backref='id')
    addressId = ForeignKeyField(address, backref='address')

    class Meta:
        database = peewee


class phone(Model):
    id = AutoField()
    type = CharField(20)
    phoneNumber = CharField()
    areaCode = CharField()
    ownerId = ForeignKeyField(employee, backref='owner')

    class Meta:
        database = peewee


class project(Model):
    id = AutoField()
    type = CharField(50)
    name = CharField()
    budget = DecimalField(16, 2)
    liderId = ForeignKeyField(employee, backref='lider')

    class Meta:
        database = peewee


class projectEmployee(Model):
    projectId = ForeignKeyField(project, backref='project')
    employeeId = ForeignKeyField(employee, backref='employee_name')

    class Meta:
        database = peewee


peewee.create_tables([address, employee, phone, project, projectEmployee])
#peewee.drop_tables([address, employee, phone, project, projectEmployee])

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Manue\Desktop\gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(722, 682)
        self.streetLabel = QtWidgets.QLabel(Dialog)
        self.streetLabel.setGeometry(QtCore.QRect(40, 40, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.streetLabel.setFont(font)
        self.streetLabel.setObjectName("streetLabel")
        self.streetText = QtWidgets.QPlainTextEdit(Dialog)
        self.streetText.setGeometry(QtCore.QRect(140, 40, 541, 31))
        self.streetText.setObjectName("streetText")
        self.cityLabel = QtWidgets.QLabel(Dialog)
        self.cityLabel.setGeometry(QtCore.QRect(40, 90, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cityLabel.setFont(font)
        self.cityLabel.setObjectName("cityLabel")
        self.cityText = QtWidgets.QPlainTextEdit(Dialog)
        self.cityText.setGeometry(QtCore.QRect(140, 90, 541, 31))
        self.cityText.setObjectName("cityText")
        self.provinceLabel = QtWidgets.QLabel(Dialog)
        self.provinceLabel.setGeometry(QtCore.QRect(40, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.provinceLabel.setFont(font)
        self.provinceLabel.setObjectName("provinceLabel")
        self.provinceText = QtWidgets.QPlainTextEdit(Dialog)
        self.provinceText.setGeometry(QtCore.QRect(140, 140, 541, 31))
        self.provinceText.setObjectName("provinceText")
        self.countryLabel = QtWidgets.QLabel(Dialog)
        self.countryLabel.setGeometry(QtCore.QRect(40, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.countryLabel.setFont(font)
        self.countryLabel.setObjectName("countryLabel")
        self.countryText = QtWidgets.QPlainTextEdit(Dialog)
        self.countryText.setGeometry(QtCore.QRect(140, 190, 541, 31))
        self.countryText.setObjectName("countryText")
        self.postcodeLabel = QtWidgets.QLabel(Dialog)
        self.postcodeLabel.setGeometry(QtCore.QRect(40, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.postcodeLabel.setFont(font)
        self.postcodeLabel.setObjectName("postcodeLabel")
        self.postcodeText = QtWidgets.QPlainTextEdit(Dialog)
        self.postcodeText.setGeometry(QtCore.QRect(140, 240, 541, 31))
        self.postcodeText.setObjectName("postcodeText")
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(140, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(250, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 360, 641, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Street", "City", "Province", "Country", "Postcode"])
        self.modifyButton = QtWidgets.QPushButton(Dialog)
        self.modifyButton.setGeometry(QtCore.QRect(390, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.modifyButton.setFont(font)
        self.modifyButton.setObjectName("modifyButton")
        self.deleteButton = QtWidgets.QPushButton(Dialog)
        self.deleteButton.setGeometry(QtCore.QRect(500, 290, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.idText = QtWidgets.QPlainTextEdit(Dialog)
        self.idText.setGeometry(QtCore.QRect(620, 290, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.idText.setFont(font)
        self.idText.setPlainText("")
        self.idText.setCenterOnScroll(True)
        self.idText.setObjectName("idText")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(380, 270, 301, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(380, 340, 301, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.addButton.clicked.connect(self.addRow)
        self.cancelButton.clicked.connect(self.cancel)
        self.deleteButton.clicked.connect(self.delete)
        self.modifyButton.clicked.connect(self.edit)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.streetLabel.setText(_translate("Dialog", "Street:"))
        self.cityLabel.setText(_translate("Dialog", "City:"))
        self.provinceLabel.setText(_translate("Dialog", "Province:"))
        self.countryLabel.setText(_translate("Dialog", "Country:"))
        self.postcodeLabel.setText(_translate("Dialog", "Postcode:"))
        self.addButton.setText(_translate("Dialog", "Add"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.modifyButton.setText(_translate("Dialog", "Modify"))
        self.deleteButton.setText(_translate("Dialog", "Delete"))

    def addRow(self):
        self.update_table()
        street_input = self.streetText.toPlainText()
        city_input = self.cityText.toPlainText()
        country_input = self.countryText.toPlainText()
        province_input = self.provinceText.toPlainText()
        postcode_input = self.postcodeText.toPlainText()

        if not street_input or not city_input or not country_input or not postcode_input:
            print("You suck")


        else:
            address_record = address(street=street_input, city=city_input, province=province_input, country=country_input, postcode=postcode_input)
            address_record.save()

        self.streetText.clear()
        self.cityText.clear()
        self.countryText.clear()
        self.provinceText.clear()
        self.postcodeText.clear()

    def edit(self):
        id_input = self.idText.toPlainText()
        street_input = self.streetText.toPlainText()
        city_input = self.cityText.toPlainText()
        country_input = self.countryText.toPlainText()
        postcode_input = self.postcodeText.toPlainText()

        if street_input:
            update = address.update(street=street_input).where(address.id == id_input)
            update.execute()

        if city_input:
            update = address.update(city=city_input).where(address.id == id_input)
            update.execute()

        if country_input:
            update = address.update(country=country_input).where(address.id == id_input)
            update.execute()

        if postcode_input:
            update = address.update(postcode=postcode_input).where(address.id == id_input)
            update.execute()

        self.streetText.clear()
        self.cityText.clear()
        self.countryText.clear()
        self.provinceText.clear()
        self.postcodeText.clear()

    def cancel(self):
        self.streetText.clear()
        self.cityText.clear()
        self.countryText.clear()
        self.provinceText.clear()
        self.postcodeText.clear()

    def delete(self):
        id_input = self.idText.toPlainText()
        query = address.delete().where(address.id == id_input)
        query.execute()
        #try:
        #except self.address.DoesNotExist:
         #   return print({'error': 'that set does not exist'})
        #if not query.exists():
            #self.streetText.setPlainText("you suck")
        #self.streetText.setPlainText(query.street)



    def exit_program(self):
        sys.exit()

    def update_table(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        query = address.select()
        self.tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem("text1"))
        self.tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem("text2"))
        self.tableWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem("text3"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
