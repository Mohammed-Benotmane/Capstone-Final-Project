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

    @app.route('/disponibilities')
    def get_disponibilities():
        disponibilities = MedicationPharmacy.query.all()
        formatted_disponibilities = [disponibility.format() for disponibility in disponibilities]
        return jsonify({
            'success':True,
            'disponibilities':formatted_disponibilities,
            'total_disponibilities':len(disponibilities)
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

    @app.route('/disponibilities/<int:disponibility_id>',methods=['DELETE'])
    def delete_disponibility(disponibility_id):
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

    @app.route('/disponibilities',methods=['POST'])
    def create_disponibilities():
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

    @app.route("/medications/<medication_id>", methods=['PATCH'])
    def patch_medications(medication_id):
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

    return app


app = create_app()

if __name__ == '__main__':
    app.run()