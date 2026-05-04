import joblib
import sys
import os
from feature_extractor import EmailFeatureExtractor, get_text_data

MODEL_PATH = "phishing_model.pkl"

def predict_email(text):
    if not os.path.exists(MODEL_PATH):
        print(f"Error: Model file '{MODEL_PATH}' not found. Please run train_model.py first.")
        return

    # Load the trained model
    model = joblib.load(MODEL_PATH)
    
    # Predict
    # The pipeline expects a list or array-like of strings
    prediction = model.predict([text])
    probabilities = model.predict_proba([text])[0]
    
    print("\n" + "="*40)
    print("EMAIL ANALYSIS REPORT")
    print("="*40)
    print(f"Text snippet: {text[:100]}...")
    print(f"Prediction:   {prediction[0].upper()}")
    
    # Probabilities order depends on classes (model.classes_)
    classes = model.classes_
    for cls, prob in zip(classes, probabilities):
        print(f"Probability ({cls}): {prob*100:.2f}%")
    print("="*40 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If user passed text via command line argument
        sample_text = " ".join(sys.argv[1:])
    else:
        # Default test cases
        print("No input provided. Running default test cases...")
        sample_text = "URGENT: We noticed a login from an unknown device. Please click http://verify-account.com to secure your account."
        predict_email(sample_text)
        
        sample_text_2 = "Hi Alice, could you please send me the report by 5 PM today? Thanks!"
        predict_email(sample_text_2)
        sys.exit(0)
        
    predict_email(sample_text)
