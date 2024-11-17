from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model and label encoder
model = pickle.load(open('classifier.pkl', 'rb'))
ferti_encoder = pickle.load(open('fertilizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.htm')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        features = [
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['moisture']),
            int(request.form['soil_type']),
            int(request.form['crop_type']),
            float(request.form['nitrogen']),
            float(request.form['potassium']),
            float(request.form['phosphorous'])
        ]
        
        # Make prediction
        prediction = model.predict([features])[0]
        fertilizer_name = ferti_encoder.classes_[prediction]
        
        return render_template('index.htm', prediction_text=f'Recommended Fertilizer: {fertilizer_name}')
    except Exception as e:
        return render_template('index.htm', error_text=f'Error: {e}')

if __name__ == '__main__':
    app.run(debug=True)
