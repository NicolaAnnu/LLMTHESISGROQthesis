from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ptsd_symptoms.db'
db = SQLAlchemy(app)

class SymptomReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(50), nullable=False)
    symptom_description = db.Column(db.String(200), nullable=False)
    report_date = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/report_symptom', methods=['POST'])
def report_symptom():
    data = request.get_json()
    new_report = SymptomReport(
        employee_id=data['employee_id'],
        symptom_description=data['symptom_description']
    )
    db.session.add(new_report)
    db.session.commit()
    return jsonify({'message': 'Symptom report received'}), 201

@app.route('/aggregate_symptoms', methods=['GET'])
def aggregate_symptoms():
    symptoms = SymptomReport.query.all()
    symptom_counts = {}
    for symptom in symptoms:
        if symptom.symptom_description in symptom_counts:
            symptom_counts[symptom.symptom_description] += 1
        else:
            symptom_counts[symptom.symptom_description] = 1
    return jsonify(symptom_counts)

@app.route('/generate_report', methods=['GET'])
def generate_report():
    symptoms = SymptomReport.query.all()
    report = []
    for symptom in symptoms:
        report.append({
            'employee_id': symptom.employee_id,
            'symptom_description': symptom.symptom_description,
            'report_date': symptom.report_date
        })
    return jsonify(report)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)