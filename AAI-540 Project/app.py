from flask import Flask, request, jsonify
import xgboost as xgb
import numpy as np
import pickle

# Load the trained model
model_path = "xgboost_model.pkl"  # Ensure this file exists in the directory
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Network Anomaly Detection API is running!"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse input JSON
        data = request.get_json()

        # Extract feature values (ensure they match the model input size)
        features = np.array(data["features"]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Convert to standard response format
        response = {
            "prediction": int(prediction[0]),  # Convert NumPy int to standard int
            "message": "Prediction successful!"
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e), "message": "Invalid request!"}), 400

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True)
