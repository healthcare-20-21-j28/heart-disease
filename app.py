from flask import Flask, request, jsonify
from predict import predict_prob
from disease_description import disease_description

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to healthCare app backend !'


@app.route('/disease/heart/test', methods=['POST'])
def get_prob():
    print('method invoked')
    age = request.form['age']
    sex = request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    thalach = request.form['thalach']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']

    probability = predict_prob(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

    description = (disease_description(probability))

    return jsonify({'percentage': round(probability, 2),
                    'description': description['description'],
                    'symptoms': description['symptoms'],
                    'causes': description['causes'],
                    'treatement-1': description['treatement-1'],
                    'treatement-2': description['treatement-2']})


if __name__ == '__main__':
    app.run(debug=any)
