import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Pharmacy, Medication, MedicationPharmacy
from app import create_app

class TestAppWrapper(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        environ['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qRkNRemt4TVRGQ1JUVTVOalk1TnpjNVJUQkRSa0ZGUXpVMU4wWkRPRVZFUkRaQ09VSXhNUSJ9.eyJpc3MiOiJodHRwczovL21vaGFtbWVkYmVub3RtYW5lLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMTkxMjgwNjg0MjY5NDExNTE0NyIsImF1ZCI6WyJjYXBzdG9uZSIsImh0dHBzOi8vbW9oYW1tZWRiZW5vdG1hbmUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTk4NjY0MiwiZXhwIjoxNTg5OTkzODQyLCJhenAiOiJUdmNjTWNINjZTUktkNW56aUw0QzkxVTdaN1ZlOXNhdSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZGlzcG9uaWJpbGl0aWVzIiwiZGVsZXRlOm1lZGljYXRpb25zIiwiZGVsZXRlOnBoYXJtYWNpZXMiLCJnZXQ6ZGlzcG9uaWJpbGl0aWVzIiwiZ2V0Om1lZGljYXRpb25zIiwiZ2V0OnBoYXJtYWNpZXMiLCJwYXRjaDpkaXNwb25pYmlsaXRpZXMiLCJwYXRjaDptZWRpY2F0aW9ucyIsInBhdGNoOnBoYXJtYWNpZXMiLCJwb3N0OmRpc3BvbmliaWxpdGllcyIsInBvc3Q6bWVkaWNhdGlvbnMiLCJwb3N0OnBoYXJtYWNpZXMiXX0.tgtPWbnuxxaAb6IgO0rcDJ-eYQhMBdJkNQVqEW1DMxQ3CrF6VGC4Ms9tRbB0LYTG_sDn_TykNMI44KGouQ3eZ2FlSLIuYN052--APkF23rquD3bt49Nj53Vyxe_BmaA5IIHz4154cpjMtP54ouRm6WEwX28nMAXNknnu_ZLhg3fSjjsEFgF-vgwfBSmeB0enQRh89FM2hXsa9BQwvEuTR02XuaSwpjDqo9hAkz6sykGGk1oDJtSVAC70GlX6Lb63TgnXN5RtN9ZgO8R7QxO6duJO5AYwkUz-AIXMdJc4swz2w-MGPv4TiS1-1c0sqg6WL2mStMEI4p5vVi1Vk8AccQ'
        return self.app(environ, start_response)


class CapstoneTestCase(unittest.TestCase):
   
    def setUp(self):
        self.app = create_app()
        self.app.wsgi_app = TestAppWrapper(self.app.wsgi_app)
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = os.environ.get('DATABASE_URL',"postgres://{}:{}@{}/{}".format('postgres', '','localhost:5432', self.database_name))
        setup_db(self.app, self.database_path)

        self.new_pharmacy = {
            'name':'pharmacie hai',
            'location':'North Africa',
            'phoneNumber':'5454'
        }

        self.new_medication = {
            'medicationName':'Doliprane',
            'price':'120'
        }
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_create_pharmacies(self):
        res = self.client().post('/pharmacies',json=self.new_pharmacy)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['pharmacies'])
        self.assertTrue(data['total_pharmacies'])

    def test_create_medications(self):
        res = self.client().post('/medications',json=self.new_medication)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['medications'])
        self.assertTrue(data['total_medications'])
    
    def test_create_disponibilities(self):
        res = self.client().post('/disponibilities',json={
            'pharmacyId':Pharmacy.query.first().id,
            'medicationId':Medication.query.first().id,
            'quantity':15
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['disponibilities'])
        self.assertTrue(data['total_disponibilities'])
    
    def test_get_pharmacies(self):
        res = self.client().get('/pharmacies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['pharmacies'])
        self.assertTrue(data['total_pharmacies'])

    def test_get_medications(self):
        res = self.client().get('/medications')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['medications'])
        self.assertTrue(data['total_medications'])

    def test_get_disponibilities(self):
        res = self.client().get('/disponibilities')
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['disponibilities'])
        self.assertTrue(data['total_disponibilities'])

    def test_update_pharmacies(self):
        id=Pharmacy.query.first().id
        res = self.client().patch('/pharmacies/'+str(id),json={
            'name':'test'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['pharmacy'])

    def test_update_medication(self):
        id=Medication.query.first().id
        res = self.client().patch('/medications/'+str(id),json={
            'price':100
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['medication'])

    def test_update_disponibility(self):
        id=MedicationPharmacy.query.first().id
        res = self.client().patch('/disponibilities/'+str(id),json={
            'quantity':100
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['disponibility'])

    def test_delete_disponibility(self):
        disponibility = MedicationPharmacy.query.first()
        res = self.client().delete('/disponibilities/'+str(disponibility.id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],disponibility.id)
        self.assertTrue(data['disponibilities'])

    def test_delete_pharmacy(self):
        pharmacy = Pharmacy.query.first()
        res = self.client().delete('/pharmacies/'+str(pharmacy.id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],pharmacy.id)
        self.assertTrue(data['pharmacies'])

    def test_delete_medication(self):
        medication = Medication.query.first()
        res = self.client().delete('/medications/'+str(medication.id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],medication.id)
        self.assertTrue(data['medications'])

'''
    def test_delete_disponibility(self):
        disponibility = MedicationPharmacy.query.first()
        res = self.client().delete('/disponibilities/'+str(disponibility.id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],disponibility.id)
        self.assertTrue(data['disponibilities'])

    def test_update_pharmacies(self):
        res = self.client().patch('/pharmacies/1',json={
            'name':'test'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['pharmacy'])

    def test_delete_pharmacy(self):
        pharmacy = Pharmacy.query.first()
        disponibilities = MedicationPharmacy.query.filter(MedicationPharmacy.pharmacyId == pharmacy.id)
        for d in disponibilities:
            self.test_delete_disponibility
        res = self.client().delete('/pharmacies/'+str(pharmacy.id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],pharmacy.id)
        self.assertTrue(data['pharmacies'])
        self.assertEqual(pharmacy,None)
    
'''
    

    




        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

