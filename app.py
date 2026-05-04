from flask import Flask, render_template, request, jsonify
import joblib
import os
from feature_extractor import EmailFeatureExtractor, get_text_data

app = Flask(__name__)
MODEL_PATH = "phishing_model.pkl"

# Load the model globally
model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    print(f"Warning: Model not found at {MODEL_PATH}. Predictions will fail.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return jsonify({'error': 'Model is not loaded.'}), 500

    data = request.get_json()
    email_text = data.get('text', '')

    if not email_text.strip():
        return jsonify({'error': 'Empty text provided.'}), 400

    try:
        prediction = model.predict([email_text])[0]
        probabilities = model.predict_proba([email_text])[0]
        
        classes = model.classes_
        prob_dict = {cls: float(prob) for cls, prob in zip(classes, probabilities)}
        
        return jsonify({
            'prediction': prediction,
            'probabilities': prob_dict
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
