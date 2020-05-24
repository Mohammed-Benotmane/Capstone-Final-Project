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

'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qRkNRemt4TVRGQ1JUVTVOalk1TnpjNVJUQkRSa0ZGUXpVMU4wWkRPRVZFUkRaQ09VSXhNUSJ9.eyJpc3MiOiJodHRwczovL21vaGFtbWVkYmVub3RtYW5lLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWM4ZWZiMTkyZGNlODBjNmYxMmZiMzIiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MDM0MDc5NSwiZXhwIjoxNTkwNDI3MTkwLCJhenAiOiJUdmNjTWNINjZTUktkNW56aUw0QzkxVTdaN1ZlOXNhdSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRpc3BvbmliaWxpdGllcyIsImdldDptZWRpY2F0aW9ucyIsImdldDpwaGFybWFjaWVzIl19.YUwySravFS4_IRZdKrxBinRG6Pq_O5LDoaOKVG5MxpTO41YeVzht2cuSQu9mrMW_VhzrtPdATDsCXkslmncv9ZcqVauhbNvBCpHhS-KzUB0zzH_WYN7DeDqEh5bVIgt42icMKKUvtPQFTEOvvRZIfz4YKPkxAH1n-N2kXpZR7BagX-SP0KdaQzqJilIFuQG6MsVobZ6zAqZmQ5lWl2q0IJPr2-KGr9WYsVqjn_8tsoYcndYFdnVJkarJ_XKJRFRTfSNaZr5UZSd1qR2Bn7OQZrp6_vOUnyWAyKlUC39qvB556Ayge9C_yyaD1QV5TgeJ8V8ebSOtWNQ3ZhjAZ-o7cg'

Admin Token:

'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5qRkNRemt4TVRGQ1JUVTVOalk1TnpjNVJUQkRSa0ZGUXpVMU4wWkRPRVZFUkRaQ09VSXhNUSJ9.eyJpc3MiOiJodHRwczovL21vaGFtbWVkYmVub3RtYW5lLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWM4ZWJkM2VlNTZjNDBjNmQ4MDJlZTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTU5MDM0MDkwOSwiZXhwIjoxNTkwNDI3MzA0LCJhenAiOiJUdmNjTWNINjZTUktkNW56aUw0QzkxVTdaN1ZlOXNhdSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRpc3BvbmliaWxpdGllcyIsImRlbGV0ZTptZWRpY2F0aW9ucyIsImRlbGV0ZTpwaGFybWFjaWVzIiwiZ2V0OmRpc3BvbmliaWxpdGllcyIsImdldDptZWRpY2F0aW9ucyIsImdldDpwaGFybWFjaWVzIiwicGF0Y2g6ZGlzcG9uaWJpbGl0aWVzIiwicGF0Y2g6bWVkaWNhdGlvbnMiLCJwYXRjaDpwaGFybWFjaWVzIiwicG9zdDpkaXNwb25pYmlsaXRpZXMiLCJwb3N0Om1lZGljYXRpb25zIiwicG9zdDpwaGFybWFjaWVzIl19.D-nvm_KdVofslGE140lod4_vsQqybBQcejJDPTtbjtNuca4rEX57ocr_f1-3ds5_miZtEQO817B61mnryApistjB2Wj8Hm5v_4zC6KwBbOhMzvZHp-S6CeDOQ0i32YAXXIwkkBrY9gIFL9WiAwjp1TYqc1h4uj4E8_WbNKXpPMnbUJsxqpVYIxVGBh_7MchYH20V3bzmmw2FM6QkY99fUG9OaccnGKh6jJVHXY423t4G2limnQl1VPT8R0cPaqF18xNrJp0JnsXPdsnimqdNYLQE29eEJvW__5MEl3ARe88pzfR0KY6B6AzQEuDSvySrXI-ybkoV4DFchtBGvYT3ig'

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