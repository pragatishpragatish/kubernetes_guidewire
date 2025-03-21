from flask import Flask, request, jsonify
import numpy as np
import joblib
app = Flask(__name__)

# Load the trained model
model = joblib.load("deployment/k8s_failure_model.pkl")
scaler = joblib.load("deployment/scaler.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    """API endpoint for predicting Kubernetes failures"""
    data = request.json  # Expecting JSON input
    features = np.array(data["features"]).reshape(1, -1)
    
    # Preprocess input
    features_scaled = scaler.transform(features)
    
    # Make prediction
    prediction = model.predict(features_scaled)[0]
    
    return jsonify({"prediction": int(prediction)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
