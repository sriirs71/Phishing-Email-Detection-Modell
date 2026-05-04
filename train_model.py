import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import FunctionTransformer

from feature_extractor import EmailFeatureExtractor, get_text_data

def load_data(filepath="emails.csv"):
    if not os.path.exists(filepath):
        print(f"Dataset {filepath} not found. Please run generate_dataset.py first.")
        exit(1)
    df = pd.read_csv(filepath)
    return df['text'], df['label']

def build_pipeline():
    """
    Combines custom features (URL count, keywords, length) with TF-IDF features.
    """
    # FeatureUnion combines multiple feature extraction mechanisms
    features = FeatureUnion([
        ('text_tfidf', Pipeline([
            ('selector', FunctionTransformer(get_text_data, validate=False)),
            ('tfidf', TfidfVectorizer(max_features=5000, stop_words='english'))
        ])),
        ('custom_features', EmailFeatureExtractor())
    ])

    # The main pipeline combines features with a classifier
    pipeline = Pipeline([
        ('features', features),
        ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
    ])
    
    return pipeline

def main():
    print("Loading dataset...")
    X, y = load_data()
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Building model pipeline...")
    model = build_pipeline()
    
    print("Training model (this might take a moment)...")
    model.fit(X_train, y_train)
    
    print("Evaluating model...")
    y_pred = model.predict(X_test)
    
    # Calculate accuracy
    acc = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {acc * 100:.2f}%")
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Plot Confusion Matrix
    cm = confusion_matrix(y_test, y_pred, labels=["Phishing", "Safe"])
    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["Phishing", "Safe"], yticklabels=["Phishing", "Safe"])
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Phishing Detection Confusion Matrix')
    
    cm_path = "confusion_matrix.png"
    plt.savefig(cm_path)
    print(f"\nConfusion matrix saved to {cm_path}")
    
    # Save the model
    model_path = "phishing_model.pkl"
    joblib.dump(model, model_path)
    print(f"Model saved successfully to {model_path}")

if __name__ == "__main__":
    main()
