import psycopg2
from peewee import *
from remi import gui
from app.gui import untitled
from remi import start, App

peewee = PostgresqlDatabase(
    'postgres',  
    user='postgres',  
    password='postgre',  
    host='localhost')  

peewee._connect();

class address(Model):
    id = IntegerField( unique = True )
    street = CharField()
    city = CharField(100)
    country = CharField(100)
    postcode = CharField(50)
    
    class Meta:
        database = peewee

class employee(Model):
    id = IntegerField( unique = True )
    firstName = CharField()
    lastName = CharField()
    salary = DecimalField(10,2)
    startDate = DateField()
    endDate = DateField()
    ##managerId = ForeignKeyField(employee, backref='id')
    addressId = ForeignKeyField(address, backref = 'address')
    
    class Meta:
        database = peewee 

class phone(Model):
    id = IntegerField( unique = True )
    type = CharField(20)
    phoneNumber = CharField()
    areaCode = CharField()
    ownerId = ForeignKeyField(employee, backref = 'owner')
    
    class Meta:
        database = peewee
        
class project(Model):
    id = IntegerField( unique = True )
    type = CharField(50)
    name = CharField()
    budget = DecimalField(16,2)
    liderId = ForeignKeyField(employee, backref = 'lider')
    
    class Meta:
        database = peewee

class projectEmployee(Model):
    projectId = ForeignKeyField(project, backref = 'project')
    employeeId = ForeignKeyField(employee, backref = 'employee_name')
    
    class Meta:
        database = peewee

peewee.create_tables([address, employee, phone, project, projectEmployee])


data_source = {'id': '1', 'firstName': 'Natalia', 'lastName': 'Cunillera', 'startDate': '12/7/2005', 'endDate': '7/7/2018'}
employee.insert_many(data_source)
GUI = untitled()

##peewee.drop_tables([employee])