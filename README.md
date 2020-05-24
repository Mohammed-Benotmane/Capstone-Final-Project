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

