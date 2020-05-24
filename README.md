# Capstone MediPharm

## capstone project for the udacity full stack nanodegree program.

**Heroku link:** (https://capstonemedipharm.herokuapp.com/)

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies
Navigate to the directory of the project and run:

```
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server

To run the server, execute:

```
export FLASK_APP=app.py
export FLASK_ENV=debug
flask run --reload
```

## MediPharm Specifications

Medipharm models a website that is responsible for creating pharmacies and managing and assigning medications to those pharmacies, and we can found the availability of all medications in all pharmacies. There is two roles, the admin and the client, each one has his own permissions.

## Models

Pharmacy with attributes: name, location and phoneNumber.
Medication with attributes: medicationName, price.
MedicationPharmacy with attributes: pharmacyId, medicationId and quantity.

## Roles and Permissions

Client

- GET:pharmacies
- GET:medications
- GET:disponibilities

Admin

- GET:pharmacies
- GET:medications
- GET:disponibilities
- POST:pharmacies
- POST:medications
- POST:disponibilities
- PATCH:pharmacies
- PATCH:medications
- PATCH:disponibilities
- DELETE:pharmacies
- DELETE:medications
- DELETE:disponibilities

## Authorization

To execute the endpoints you need authorization, here is two bearer token for the two roles:

Client Token:

'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qRkNRemt4TVRGQ1JUVTVOalk1TnpjNVJUQkRSa0ZGUXpVMU4wWkRPRVZFUkRaQ09VSXhNUSJ9.eyJpc3MiOiJodHRwczovL21vaGFtbWVkYmVub3RtYW5lLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWM4ZWZiMTkyZGNlODBjNmYxMmZiMzIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MDIyNjk1OSwiZXhwIjoxNTkwMjM0MTU5LCJhenAiOiJUdmNjTWNINjZTUktkNW56aUw0QzkxVTdaN1ZlOXNhdSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRpc3BvbmliaWxpdGllcyIsImdldDptZWRpY2F0aW9ucyIsImdldDpwaGFybWFjaWVzIl19.fNPyx-mFW6kKS_tD3dkkHpwSrm_pvSX7UvpyWFv8nnsQyRxEnsiCI9X4QmLzbKP3JbRZbI1uaOVcgyxuPhpoTnGrwLh0xzPac27_8TO_X8ekQKu_LESRltGstsdTjv_0ka3ywR8o7kiDrNpJlK4jWd5efbztfET3BaSAU1-cNaUYmNW0KwzW_unsUuS5FRBLL2OB9QV4ZlwbS3gzAmwGr56ON9yNlp4vuseJp21tJRFkXjfHdKJYV7xXoDpdw6QX8KtnrLGEI5Nk80VSTQVrFzxtlnmBXBHaWagSn2nxPqmIF7YUoJeyP1jqhfvdLo5naOZ3O48h7S36IA7zdclk7A'

Admin Token:

'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qRkNRemt4TVRGQ1JUVTVOalk1TnpjNVJUQkRSa0ZGUXpVMU4wWkRPRVZFUkRaQ09VSXhNUSJ9.eyJpc3MiOiJodHRwczovL21vaGFtbWVkYmVub3RtYW5lLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWM4ZWJkM2VlNTZjNDBjNmQ4MDJlZTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MDI1ODk4NCwiZXhwIjoxNTkwMzQ1Mzc5LCJhenAiOiJUdmNjTWNINjZTUktkNW56aUw0QzkxVTdaN1ZlOXNhdSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRpc3BvbmliaWxpdGllcyIsImRlbGV0ZTptZWRpY2F0aW9ucyIsImRlbGV0ZTpwaGFybWFjaWVzIiwiZ2V0OmRpc3BvbmliaWxpdGllcyIsImdldDptZWRpY2F0aW9ucyIsImdldDpwaGFybWFjaWVzIiwicGF0Y2g6ZGlzcG9uaWJpbGl0aWVzIiwicGF0Y2g6bWVkaWNhdGlvbnMiLCJwYXRjaDpwaGFybWFjaWVzIiwicG9zdDpkaXNwb25pYmlsaXRpZXMiLCJwb3N0Om1lZGljYXRpb25zIiwicG9zdDpwaGFybWFjaWVzIl19.NGt49NwR1IX8BR5kyK_e3yCrXfIBItNwJ7vlJHcqA_sX41wiQLtQ5riBu1AgDyQYi62eca_HklVESYy20qDPOr83bltC4khTBGccH3Q2iPrMTyjC4DtwG04HXiKj4D7Oe_XPyl6QgIu3zhak1j1c9aSrWjceJE3ZmfdgsFcbFYOuWGE3K1PKY6QT44iJU3KT4B1XbNW3SMlz0UWnVBavIHZMHT_s1hr3IApImEERPYm3KL6Dm56Vrwvsq234C3_BcxI_YiWdLQkdPblEPdA36fM4pdXFLyqpK3e6v4Oyep9CEnGlW1KVOMgOZy4eMErS8ue7Zc08KZJbSuciPlW_Xg'

## Endpoints

### Pharmacies:

GET '/pharmacies'

reponse = {
    "pharmacies": [
        {
            "id": 4,
            "location": "algeria Oran",
            "name": "pharmacie mohammed",
            "phoneNumber": 213213
        },
        {
            "id": 5,
            "location": "algeria gdyel",
            "name": "pharmacie abir",
            "phoneNumber": 55555
        }
    ],
    "success": true,
    "total_pharmacies": 2
}

POST '/pharmacies'

body = {
    "name": "pharmacie abir",
    "location": "algeria gdyel",
    "phoneNumber": 55555
}

response = {
    "pharmacies": [
        {
            "id": 4,
            "location": "algeria Oran",
            "name": "pharmacie mohammed",
            "phoneNumber": 213213
        },
        {
            "id": 5,
            "location": "algeria gdyel",
            "name": "pharmacie abir",
            "phoneNumber": 55555
        }
    ],
    "success": true,
    "total_pharmacies": 2
}


PATCH '/pharmacies/<int:pharmacy_id>'

params = <int:pharmacy_id>

for example we change the name of the pharmacy with id:5.

body = {
    "name": "pharmacie test"
}

response = {
    "pharmacy": {
        "id": 5,
        "location": "algeria gdyel",
        "name": "pharmacie test",
        "phoneNumber": 55555
    },
    "success": true
}

DELETE '/pharmacies/<int:pharmacy_id>'

params = <int:pharmacy_id>

for example we delete the pharmacy with id:5

response = {
    "deleted": 5,
    "pharmacies": [
        {
            "id": 4,
            "location": "algeria Oran",
            "name": "pharmacie mohammed",
            "phoneNumber": 213213
        }
    ],
    "success": true
}


### Medications:

GET '/medications'

reponse = {
    "medications": [
        {
            "id": 6,
            "medicationName": "Doliprane",
            "price": 120
        },
        {
            "id": 7,
            "medicationName": "Clamoxyl",
            "price": 250
        }
    ],
    "success": true,
    "total_medications": 2
}

POST '/medications'

body = {
    "medicationName": "Clamoxyl",
    "price": 250
}

response = {
    "medications": [
        {
            "id": 6,
            "medicationName": "Doliprane",
            "price": 120
        },
        {
            "id": 7,
            "medicationName": "Clamoxyl",
            "price": 250
        }
    ],
    "success": true,
    "total_medications": 2
}


PATCH '/medications/<int:medication_id>'

params = <int:medication_id>

for example we change the price of the pharmacy with id:6.

body = {
    "price": 1000
}

response = {
    "medication": {
        "id": 6,
        "medicationName": "Doliprane",
        "price": 1000
    },
    "success": true
}

DELETE '/medications/<int:medication_id>'

params = <int:medication_id>

for example we delete the medication with id:6

response = {
    "deleted": 6,
    "medications": [
        {
            "id": 7,
            "medicationName": "Clamoxyl",
            "price": 250
        }
    ],
    "success": true
}

### Disponibilities:

GET '/disponibilities'

reponse = {
    "disponibilities": [
        {
            "id": 4,
            "medicationId": 7,
            "pharmacyId": 4,
            "quantity": 158
        }
    ],
    "success": true,
    "total_disponibilities": 1
}

POST '/disponibilities'

body = {
    "pharmacyId": 4,
    "medicationId": 7,
    "quantity": 158
}

response = {
    "disponibilities": [
        {
            "id": 4,
            "medicationId": 7,
            "pharmacyId": 4,
            "quantity": 158
        }
    ],
    "success": true,
    "total_disponibilities": 1
}


PATCH '/disponibilities/<int:disponibility_id>'

params = <int:disponibility_id>

for example we change the quantity of the disponibility with id:4.

body = {
    "quantity": 800
}

response = {
    "disponibility": {
        "id": 4,
        "medicationId": 7,
        "pharmacyId": 4,
        "quantity": 800
    },
    "success": true
}

DELETE '/disponibilities/<int:disponibility_id>'

params = <int:disponibility_id>

for example we delete the disponibility with id:4

response = {
    "deleted": 4,
    "disponibilities": [],
    "success": true
}

## Testing

To run the tests run in your terminal

```bash

python capstonetest.py
`````