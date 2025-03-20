from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

# Load the trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

app = Flask(__name__)
CORS(app)  # Allow frontend access

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        features = np.array([data['features']])
        prediction = model.predict(features)
        return jsonify({'price': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
