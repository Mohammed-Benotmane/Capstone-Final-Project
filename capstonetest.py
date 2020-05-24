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
        environ['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qRkNRemt4TVRGQ1JUVTVOalk1TnpjNVJUQkRSa0ZGUXpVMU4wWkRPRVZFUkRaQ09VSXhNUSJ9.eyJpc3MiOiJodHRwczovL21vaGFtbWVkYmVub3RtYW5lLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWM4ZWJkM2VlNTZjNDBjNmQ4MDJlZTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MDM0MDkwOSwiZXhwIjoxNTkwNDI3MzA0LCJhenAiOiJUdmNjTWNINjZTUktkNW56aUw0QzkxVTdaN1ZlOXNhdSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRpc3BvbmliaWxpdGllcyIsImRlbGV0ZTptZWRpY2F0aW9ucyIsImRlbGV0ZTpwaGFybWFjaWVzIiwiZ2V0OmRpc3BvbmliaWxpdGllcyIsImdldDptZWRpY2F0aW9ucyIsImdldDpwaGFybWFjaWVzIiwicGF0Y2g6ZGlzcG9uaWJpbGl0aWVzIiwicGF0Y2g6bWVkaWNhdGlvbnMiLCJwYXRjaDpwaGFybWFjaWVzIiwicG9zdDpkaXNwb25pYmlsaXRpZXMiLCJwb3N0Om1lZGljYXRpb25zIiwicG9zdDpwaGFybWFjaWVzIl19.D-nvm_KdVofslGE140lod4_vsQqybBQcejJDPTtbjtNuca4rEX57ocr_f1-3ds5_miZtEQO817B61mnryApistjB2Wj8Hm5v_4zC6KwBbOhMzvZHp-S6CeDOQ0i32YAXXIwkkBrY9gIFL9WiAwjp1TYqc1h4uj4E8_WbNKXpPMnbUJsxqpVYIxVGBh_7MchYH20V3bzmmw2FM6QkY99fUG9OaccnGKh6jJVHXY423t4G2limnQl1VPT8R0cPaqF18xNrJp0JnsXPdsnimqdNYLQE29eEJvW__5MEl3ARe88pzfR0KY6B6AzQEuDSvySrXI-ybkoV4DFchtBGvYT3ig'
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
