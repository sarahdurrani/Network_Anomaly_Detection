import os
import pickle
import json
import numpy as np
import xgboost as xgb

# Load model when the container starts
MODEL_PATH = "/opt/ml/model/model.xgb"

def model_fn(model_dir):
    """Load the trained model"""
    model = xgb.Booster()
    model.load_model(os.path.join(model_dir, "model.xgb"))
    return model

def input_fn(request_body, request_content_type):
    """Parse input data from JSON"""
    if request_content_type == "application/json":
        data = json.loads(request_body)["instances"]
        return np.array(data)
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    """Make predictions"""
    dmatrix = xgb.DMatrix(input_data)
    predictions = model.predict(dmatrix)
    return predictions.tolist()

def output_fn(predictions, response_content_type):
    """Format output"""
    return json.dumps({"predictions": predictions})
