import os
from flask import Flask,jsonify,request,abort
from models import setup_db,Medication,MedicationPharmacy,Pharmacy
from flask_cors import CORS
from auth.auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/medications')
    @requires_auth('get:medications')
    def get_medication(token):
        medications = Medication.query.all()
        formatted_medications = [medication.format() for medication in medications]
        return jsonify({
            'success':True,
            'medications':formatted_medications,
            'total_medications':len(medications)
        })

    @app.route('/disponibilities')
    @requires_auth('get:disponibilities')
    def get_disponibilities(token):
        disponibilities = MedicationPharmacy.query.all()
        formatted_disponibilities = [disponibility.format() for disponibility in disponibilities]
        return jsonify({
            'success':True,
            'disponibilities':formatted_disponibilities,
            'total_disponibilities':len(disponibilities)
        })


    @app.route('/pharmacies')
    @requires_auth('get:pharmacies')
    def get_pharmacies(token):
        pharmacies = Pharmacy.query.all()
        formatted_pharmacies = [pharmacy.format() for pharmacy in pharmacies]
        return jsonify({
            'success':True,
            'pharmacies':formatted_pharmacies,
            'total_pharmacies':len(pharmacies)
        })

    @app.route('/pharmacies/<int:pharmacy_id>',methods=['DELETE'])
    @requires_auth('delete:pharmacies')
    def delete_pharmacy(token, pharmacy_id):
        pharmacy = Pharmacy.query.filter(Pharmacy.id == pharmacy_id).one_or_none()
        if pharmacy is None:
            abort(404)
        pharmacy.delete()
        pharmacies = Pharmacy.query.all()
        return jsonify({
            'success':True,
            'deleted':pharmacy_id,
            'pharmacies':[pharmacy.format() for pharmacy in pharmacies]
        })

    @app.route('/disponibilities/<int:disponibility_id>',methods=['DELETE'])
    @requires_auth('delete:disponibilities')
    def delete_disponibility(token, disponibility_id):
        disponibility = MedicationPharmacy.query.filter(MedicationPharmacy.id == disponibility_id).one_or_none()
        if disponibility is None:
            abort(404)
        disponibility.delete()
        disponibilities = MedicationPharmacy.query.all()
        return jsonify({
            'success':True,
            'deleted':disponibility_id,
            'disponibilities':[disponibility.format() for disponibility in disponibilities]
        })

    @app.route('/medications/<int:medication_id>',methods=['DELETE'])
    @requires_auth('delete:medications')
    def delete_medication(token,medication_id):
        medication = Medication.query.filter(Medication.id == medication_id).one_or_none()
        if medication is None:
            abort(404)
        medication.delete()
        medications = Medication.query.all()
        return jsonify({
            'success':True,
            'deleted':medication_id,
            'medications':[medication.format() for medication in medications]
        })

    @app.route('/pharmacies',methods=['POST'])
    @requires_auth('post:pharmacies')
    def create_pharmacies(token):
        body = request.get_json()
        new_name = body.get("name",None)
        new_location = body.get("location",None)
        new_phonenumber = body.get("phoneNumber",None)
        try:
            pharmacy = Pharmacy(name=new_name,location=new_location,phoneNumber=new_phonenumber)
            pharmacy.insert()
        except:
            abort(422)
        pharmacies=Pharmacy.query.all()
        formatted_pharmacies= [pharmacy.format() for pharmacy in pharmacies]
        return jsonify({
            'success':True,
            'pharmacies':formatted_pharmacies,
            'total_pharmacies':len(pharmacies)
        })

    @app.route('/disponibilities',methods=['POST'])
    @requires_auth('post:disponibilities')
    def create_disponibilities(token):
        body = request.get_json()
        new_pharmacyId = body.get("pharmacyId",None)
        new_medicationId = body.get("medicationId",None)
        new_quantity = body.get("quantity",None)
        try:
            disponibility = MedicationPharmacy(pharmacyId=new_pharmacyId,medicationId=new_medicationId,quantity=new_quantity)
            disponibility.insert()
        except:
            abort(422)
        disponibilities=MedicationPharmacy.query.all()
        formatted_disponibilities= [disponibility.format() for disponibility in disponibilities]
        return jsonify({
            'success':True,
            'disponibilities':formatted_disponibilities,
            'total_disponibilities':len(disponibilities)
        })

    @app.route('/medications',methods=['POST'])
    @requires_auth('post:medications')
    def create_medications(token):
        body = request.get_json()
        new_medicationName = body.get("medicationName",None)
        new_price = body.get("price",None)
        try:
            medication = Medication(medicationName=new_medicationName,price=new_price)
            medication.insert()
        except:
            abort(422)
        medications=Medication.query.all()
        formatted_medications= [medication.format() for medication in medications]
        return jsonify({
            'success':True,
            'medications':formatted_medications,
            'total_medications':len(medications)
        })

    @app.route("/pharmacies/<pharmacy_id>", methods=['PATCH'])
    @requires_auth('patch:pharmacies')
    def patch_pharmacies(token,pharmacy_id):
        body = request.get_json()
        pharmacy = Pharmacy.query.get(pharmacy_id)
        if body.get("name"):
            pharmacy.name = body.get("name")
        if body.get("location"):
            pharmacy.location = body.get("location")
        if body.get("phoneNumber"):
            pharmacy.phoneNumber = body.get("phoneNumber")
        pharmacy.update()
        return jsonify({
            "success": True,
            "pharmacy": pharmacy.format()
        })

    @app.route("/disponibilities/<disponibility_id>", methods=['PATCH'])
    @requires_auth('patch:disponibilities')
    def patch_disponibility(token,disponibility_id):
        body = request.get_json()
        disponibility = MedicationPharmacy.query.get(disponibility_id)
        if body.get("pharmacyId"):
            disponibility.pharmacyId = body.get("pharmacyId")
        if body.get("medicationId"):
            disponibility.medicationId = body.get("medicationId")
        if body.get("quantity"):
            disponibility.quantity = body.get("quantity")
        disponibility.update()
        return jsonify({
            "success": True,
            "disponibility": disponibility.format()
        })

    @app.route("/medications/<medication_id>", methods=['PATCH'])
    @requires_auth('patch:medications')
    def patch_medications(token, medication_id):
        body = request.get_json()
        medication = Medication.query.get(medication_id)
        if body.get("medicationName"):
            medication.medicationName = body.get("medicationName")
        if body.get("price"):
            medication.price = body.get("price")
        medication.update()
        return jsonify({
            "success": True,
            "medication": medication.format()
        })
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404
    
    @app.errorhandler(405)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422
    
    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "500 Internal Server Error” "
        }), 500
    


    return app


app = create_app()

if __name__ == '__main__':
    app.run()