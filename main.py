# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Manue\Desktop\ormTest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot
from playhouse.migrate import *

from peewee import *

peewee = PostgresqlDatabase(
    'postgres',
    user='postgres',
    password='postgre',
    host='localhost')

peewee._connect();
migrator = PostgresqlMigrator(peewee)

class address(Model):
    street = CharField()
    city = CharField(100)
    province = CharField(100)
    country = CharField(100)
    postcode = CharField(50)

    class Meta:
        database = peewee


class employee(Model):
    firstName = CharField()
    lastName = CharField()
    salary = DecimalField(10, 2)
    startDate = DateField()
    endDate = DateField()
    managerId = IntegerField(unique=True)
    addressId = ForeignKeyField(address, backref='address')

    class Meta:
        database = peewee


class phone(Model):
    type = CharField(20)
    phoneNumber = CharField()
    areaCode = CharField()
    ownerId = ForeignKeyField(employee, backref='owner')

    class Meta:
        database = peewee


class project(Model):
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
#migrator.add_column(ForeignKeyField(employee, backref="manager"))
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
        Dialog.setObjectName("Address")
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
        self.tableWidget.setGeometry(QtCore.QRect(80, 360, 602, 283))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Street", "City", "Province", "Country", "Postcode"])
        self.tableWidget.verticalHeader().hide()
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.modifyButton = QtWidgets.QPushButton(Dialog)
        self.modifyButton.setGeometry(QtCore.QRect(380, 290, 101, 41))
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
        self.show_table()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Address", "Address"))
        self.streetLabel.setText(_translate("Address", "Street:"))
        self.cityLabel.setText(_translate("Address", "City:"))
        self.provinceLabel.setText(_translate("Address", "Province:"))
        self.countryLabel.setText(_translate("Address", "Country:"))
        self.postcodeLabel.setText(_translate("Address", "Postcode:"))
        self.addButton.setText(_translate("Address", "Add"))
        self.cancelButton.setText(_translate("Address", "Cancel"))
        self.modifyButton.setText(_translate("Address", "Modify"))
        self.deleteButton.setText(_translate("Address", "Delete"))

    def addRow(self):
        street_input = self.streetText.toPlainText()
        city_input = self.cityText.toPlainText()
        country_input = self.countryText.toPlainText()
        province_input = self.provinceText.toPlainText()
        postcode_input = self.postcodeText.toPlainText()

        if not street_input or not city_input or not country_input or not postcode_input:
            msgBox = QMessageBox();
            msgBox.setText("Please add all fields")
            msgBox.exec()
        else:
            address_record = address(street=street_input, city=city_input, province=province_input, country=country_input, postcode=postcode_input)
            address_record.save()
            msgBox = QMessageBox()
            msgBox.setText("Address added")
            msgBox.exec()
            self.tableWidget.clear()
            self.tableWidget.setRowCount(0)
            self.show_table()

        self.streetText.clear()
        self.cityText.clear()
        self.countryText.clear()
        self.provinceText.clear()
        self.postcodeText.clear()

    def edit(self):
        id_input = self.idText.toPlainText()

        if id_input:
            street_input = self.streetText.toPlainText()
            city_input = self.cityText.toPlainText()
            country_input = self.countryText.toPlainText()
            postcode_input = self.postcodeText.toPlainText()

            if street_input:
                update = address.update(street=street_input).where(address.id == id_input)
                update.execute()
                self.streetText.clear()

            if city_input:
                update = address.update(city=city_input).where(address.id == id_input)
                update.execute()
                self.cityText.clear()

            if country_input:
                update = address.update(country=country_input).where(address.id == id_input)
                update.execute()
                self.countryText.clear()

            if postcode_input:
                update = address.update(postcode=postcode_input).where(address.id == id_input)
                update.execute()
                self.postcodeText.clear()

            self.streetText.clear()
            self.cityText.clear()
            self.countryText.clear()
            self.provinceText.clear()
            self.postcodeText.clear()
            self.tableWidget.clear()
            self.tableWidget.setRowCount(0)
            self.show_table()
            self.idText.clear()

    def cancel(self):
        self.streetText.clear()
        self.cityText.clear()
        self.countryText.clear()
        self.provinceText.clear()
        self.postcodeText.clear()

    def delete(self):
        id_input = self.idText.toPlainText()
        if id_input:
            query = address.delete().where(address.id == id_input)
            query.execute()
            msgBox = QMessageBox()
            msgBox.setText("Address erased")
            msgBox.exec()
            self.idText.clear()
            self.tableWidget.clear()
            self.tableWidget.setRowCount(0)
            self.show_table()

    def show_table(self):
        query = address.select()
        query.execute()

        self.tableWidget.setHorizontalHeaderLabels(["ID", "Street", "City", "Province", "Country", "Postcode"])
        for address_input in address.select():
            row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_count)
            new_id = QTableWidgetItem()
            new_street = QTableWidgetItem()
            new_city = QTableWidgetItem()
            new_province = QTableWidgetItem()
            new_country = QTableWidgetItem()
            new_postcode = QTableWidgetItem()

            new_id.setText(str(address_input.id))
            new_street.setText(address_input.street)
            new_city.setText(address_input.city)
            new_province.setText(address_input.province)
            new_country.setText(address_input.country)
            new_postcode.setText(str(address_input.postcode))

            self.tableWidget.setItem(row_count, 0, new_id)
            self.tableWidget.setItem(row_count, 1, new_street)
            self.tableWidget.setItem(row_count, 2, new_city)
            self.tableWidget.setItem(row_count, 3, new_province)
            self.tableWidget.setItem(row_count, 4, new_country)
            self.tableWidget.setItem(row_count, 5, new_postcode)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
