import os
from flask import Flask,jsonify,request,abort
from models import setup_db,Medication,MedicationPharmacy,Pharmacy
from flask_cors import CORS

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/medications')
    def get_medication():
        medications = Medication.query.all()
        formatted_medications = [medication.format() for medication in medications]
        return jsonify({
            'success':True,
            'medications':formatted_medications,
            'total_medications':len(medications)
        })


    @app.route('/pharmacies')
    def get_pharmacies():
        pharmacies = Pharmacy.query.all()
        formatted_pharmacies = [pharmacy.format() for pharmacy in pharmacies]
        return jsonify({
            'success':True,
            'pharmacies':formatted_pharmacies,
            'total_pharmacies':len(pharmacies)
        })

    @app.route('/pharmacies/<int:pharmacy_id>',methods=['DELETE'])
    def delete_pharmacy(pharmacy_id):
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

    @app.route('/medications/<int:medication_id>',methods=['DELETE'])
    def delete_medication(medication_id):
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
    def create_pharmacies():
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

    @app.route('/medications',methods=['POST'])
    def create_medications():
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
    def patch_pharmacies(pharmacy_id):
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

    return app


app = create_app()

if __name__ == '__main__':
    app.run()