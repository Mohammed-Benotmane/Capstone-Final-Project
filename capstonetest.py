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
        environ['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qRkNRemt4TVRGQ1JUVTVOalk1TnpjNVJUQkRSa0ZGUXpVMU4wWkRPRVZFUkRaQ09VSXhNUSJ9.eyJpc3MiOiJodHRwczovL21vaGFtbWVkYmVub3RtYW5lLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMTkxMjgwNjg0MjY5NDExNTE0NyIsImF1ZCI6WyJjYXBzdG9uZSIsImh0dHBzOi8vbW9oYW1tZWRiZW5vdG1hbmUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5MDEyOTY2MCwiZXhwIjoxNTkwMTM2ODYwLCJhenAiOiJUdmNjTWNINjZTUktkNW56aUw0QzkxVTdaN1ZlOXNhdSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZGlzcG9uaWJpbGl0aWVzIiwiZGVsZXRlOm1lZGljYXRpb25zIiwiZGVsZXRlOnBoYXJtYWNpZXMiLCJnZXQ6ZGlzcG9uaWJpbGl0aWVzIiwiZ2V0Om1lZGljYXRpb25zIiwiZ2V0OnBoYXJtYWNpZXMiLCJwYXRjaDpkaXNwb25pYmlsaXRpZXMiLCJwYXRjaDptZWRpY2F0aW9ucyIsInBhdGNoOnBoYXJtYWNpZXMiLCJwb3N0OmRpc3BvbmliaWxpdGllcyIsInBvc3Q6bWVkaWNhdGlvbnMiLCJwb3N0OnBoYXJtYWNpZXMiXX0.MY2XlxtMH0wEqnIsmn44YnQl-oY-sVcCZR5M-hiCsx58wJMzAEy5xbuHpVIiP4oPC5g35t3Cho0DLbpUE7qRfWbuV4-OJmzUWzIE4ghDq65nuR9QiR0tWEZMKuB_r-k3DEnBlDCGkWhRoEH8DGJOFaOnr3OXYLvR5OZyd31eom9xfJPGs68TQ7AsQcpc1tMx4Xlv3NqZpV7Rv7Q8r2C9lpEyPpQ7Z-dTjNiSjTKBDuSCOFTGxZAptPjHWthpDcXhgO9VW3MAw_d-F0DDJ0CNigkJu7QvB8BhesXWfozIEUiFD3QuHzoqn0QeJ1rnJm3lXQjSzXnj4IoyqYOjFLj2DQ'
        return self.app(environ, start_response)


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.wsgi_app = TestAppWrapper(self.app.wsgi_app)
        self.client = self.app.test_client
        self.database_name = "capstone_test"
        self.database_path = os.environ.get(
            'DATABASE_URL', "postgres://{}:{}@{}/{}".format('postgres', '', 'localhost:5432', self.database_name))
        setup_db(self.app, self.database_path)

        self.new_pharmacy = {
            'name': 'pharmacie hai',
            'location': 'North Africa',
            'phoneNumber': 5454
        }

        self.new_medication = {
            'medicationName': 'Doliprane',
            'price': 120
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def testA_create_pharmacies(self):
        res = self.client().post('/pharmacies', json=self.new_pharmacy)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['pharmacies'])
        self.assertTrue(data['total_pharmacies'])

    def testB_create_medications(self):
        res = self.client().post('/medications', json=self.new_medication)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['medications'])
        self.assertTrue(data['total_medications'])

    def testC_create_disponibilities(self):
        res = self.client().post('/disponibilities', json={
            'pharmacyId': Pharmacy.query.first().id,
            'medicationId': Medication.query.first().id,
            'quantity': 15
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['disponibilities'])
        self.assertTrue(data['total_disponibilities'])

    def testD_get_pharmacies(self):
        res = self.client().get('/pharmacies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['pharmacies'])
        self.assertTrue(data['total_pharmacies'])

    def testE_get_medications(self):
        res = self.client().get('/medications')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['medications'])
        self.assertTrue(data['total_medications'])

    def testF_get_disponibilities(self):
        res = self.client().get('/disponibilities')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['disponibilities'])
        self.assertTrue(data['total_disponibilities'])

    def testG_update_pharmacies(self):
        id = Pharmacy.query.first().id
        res = self.client().patch('/pharmacies/'+str(id), json={
            'name': 'test'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['pharmacy'])

    def testH_update_medication(self):
        id = Medication.query.first().id
        res = self.client().patch('/medications/'+str(id), json={
            'price': 100
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['medication'])

    def testI_update_disponibility(self):
        id = MedicationPharmacy.query.first().id
        res = self.client().patch('/disponibilities/'+str(id), json={
            'quantity': 100
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['disponibility'])

    def testJ_delete_disponibility(self):
        disponibility = MedicationPharmacy.query.first()
        res = self.client().delete('/disponibilities/'+str(disponibility.id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], disponibility.id)

    def testK_delete_pharmacy(self):
        pharmacy = Pharmacy.query.first()
        res = self.client().delete('/pharmacies/'+str(pharmacy.id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], pharmacy.id)

    def testL_delete_medication(self):
        medication = Medication.query.first()
        res = self.client().delete('/medications/'+str(medication.id))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], medication.id)

    def testM_error_create_pharmacy(self):
        res = self.client().post('/pharmacies', json={
            'name': 3,
            'location': 10,
            'phoneNumber': 'test'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def testN_error_create_medication(self):
        res = self.client().post('/medications', json={
            'medicationName': 3,
            'price': 'test'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def testO_error_create_disponibility(self):
        res = self.client().post('/disponibilities', json={
            'pharmacyId': 'test',
            'medicationId': 'test',
            'quantity':'test'
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def testE1_error_get_pharmacies(self):
        res = self.client().get('/pharmacies/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method Not Allowed")

    def testF1_error_get_medications(self):
        res = self.client().get('/medications/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method Not Allowed")

    def testG1_error_get_disponibilities(self):
        res = self.client().get('/disponibilities/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Method Not Allowed")

    def testH1_error_update_pharmacy(self):
        id = Pharmacy.query.first().id
        res = self.client().patch('/pharmacies/'+ str(id), json={
            'phoneNumber': True
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "500 Internal Server Error” ")

    def testI1_error_update_medication(self):
        id = Medication.query.first().id
        res = self.client().patch('/medications/'+ str(id), json={
            'price': True
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "500 Internal Server Error” ")

    def testJ1_error_update_disponibility(self):
        id = MedicationPharmacy.query.first().id
        res = self.client().patch('/disponibilities/'+ str(id), json={
            'quantity': True
        })
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 500)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "500 Internal Server Error” ")

    def testL1_error_delete_pharmacy(self):
        res = self.client().delete('/pharmacies/100000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def testM1_error_delete_medication(self):
        res = self.client().delete('/medications/100000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def testN1_error_delete_disponibility(self):
        res = self.client().delete('/disponibilities/100000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
