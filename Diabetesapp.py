import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('picklediabetes.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('DiabetesIndex.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = int(prediction[0])
    if (output ==1):
        return render_template('DiabetesIndex.html', prediction_text='Person is Suffering with diabetes')
    else:
        return render_template('DiabetesIndex.html', prediction_text='Person is not Suffering from diabetes')




if __name__ == "__main__":
    app.run(debug = True)