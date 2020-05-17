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
        environ['HTTP_AUTHORIZATION'] = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qRkNRemt4TVRGQ1JUVTVOalk1TnpjNVJUQkRSa0ZGUXpVMU4wWkRPRVZFUkRaQ09VSXhNUSJ9.eyJpc3MiOiJodHRwczovL21vaGFtbWVkYmVub3RtYW5lLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMTkxMjgwNjg0MjY5NDExNTE0NyIsImF1ZCI6WyJjYXBzdG9uZSIsImh0dHBzOi8vbW9oYW1tZWRiZW5vdG1hbmUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU4OTY5NjM3NCwiZXhwIjoxNTg5NzAzNTc0LCJhenAiOiJUdmNjTWNINjZTUktkNW56aUw0QzkxVTdaN1ZlOXNhdSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6ZGlzcG9uaWJpbGl0aWVzIiwiZGVsZXRlOm1lZGljYXRpb25zIiwiZGVsZXRlOnBoYXJtYWNpZXMiLCJnZXQ6ZGlzcG9uaWJpbGl0aWVzIiwiZ2V0Om1lZGljYXRpb25zIiwiZ2V0OnBoYXJtYWNpZXMiLCJwYXRjaDpkaXNwb25pYmlsaXRpZXMiLCJwYXRjaDptZWRpY2F0aW9ucyIsInBhdGNoOnBoYXJtYWNpZXMiLCJwb3N0OmRpc3BvbmliaWxpdGllcyIsInBvc3Q6bWVkaWNhdGlvbnMiLCJwb3N0OnBoYXJtYWNpZXMiXX0.bgWOt9e9IY2Q4NL5cThti6M1p-EXQCKIbxsq-7MvVtFHVUhinkCz7t06vWm-gaXIreoHPQnH-AEIyhMmB85ROLAL3PnW-FgqzvyniGxrxsRsizawxfQScLmeogWA9FhfJF4-sX82VsD-AvhHUKL3_6IMjUUTugk58nWOE2fvgJA2Y--sa5Oj9teV8WAe3niHz6bXWRgKgVW-I85lNfBTW8bmudBhNJu3I_SNtyKn88Qm7HoNxMQrj6IAKKrcPI7murzzoFgT0b5eFxOc5F6ZNpd8cyilpIN9Gy3e6I-JGlYIcjOge-dcNIC2FUIE2gWy74n0ZH7cZfqaSkUJaoggJA'
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
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

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

    def test_create_pharmacies(self):
        res = self.client().post('/pharmacies',json=self.new_pharmacy)
        data = json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['pharmacies'])
        self.assertTrue(data['total_pharmacies'])

    

    




        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

