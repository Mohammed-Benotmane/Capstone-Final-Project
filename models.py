from sqlalchemy import Column, String, create_engine,Integer,ForeignKey
from flask_sqlalchemy import SQLAlchemy
import json
import os
database_name="capstoneproject"
database_path = os.environ.get('DATABASE_URL',"postgres://{}:{}@{}/{}".format('postgres', '','localhost:5432', database_name))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Pharmacy
'''
class Pharmacy(db.Model):  
  __tablename__ = 'Pharmacy'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  location = Column(String)
  phoneNumber = Column(Integer)

  def __init__(self, name, location, phoneNumber):
    self.name = name
    self.location = location
    self.phoneNumber = phoneNumber
  
  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'location': self.location,
      'phoneNumber': self.phoneNumber
      }

class Medication(db.Model):  
  __tablename__ = 'Medication'

  id = Column(Integer, primary_key=True)
  medicationName = Column(String)
  price = Column(Integer)

  def __init__(self, medicationName, price):
    self.medicationName = medicationName
    self.price = price

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'medicationName': self.medicationName,
      'price': self.price
      }

class MedicationPharmacy(db.Model):  
  __tablename__ = 'MedicationPharmacy'

  id = Column(Integer, primary_key=True)
  pharmacyId = Column(Integer,ForeignKey('Pharmacy.id', ondelete='CASCADE'))
  medicationId = Column(Integer,ForeignKey('Medication.id',ondelete='CASCADE'))
  quantity = Column(Integer)

  def __init__(self, pharmacyId, medicationId, quantity):
    self.pharmacyId = pharmacyId
    self.medicationId = medicationId
    self.quantity = quantity

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id':self.id,
      'pharmacyId': self.pharmacyId,
      'medicationId': self.medicationId,
      'quantity': self.quantity
      }
