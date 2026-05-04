Phishing Email Detection Model (Scikit-learn)

A Machine Learning project that detects whether an email is Phishing or Safe using text content and URL-based features. Built with Python and Scikit-learn, this tool helps identify malicious emails by analyzing keywords, links, and patterns commonly used in phishing attacks.

Features
Train model on phishing and legitimate email dataset
Extract email text features using TF-IDF
Detect suspicious URLs and phishing keywords
Classify emails as Phishing or Safe
Display Accuracy and Confusion Matrix
Save trained model as phishing_model.pkl
Technologies Used
Python
Scikit-learn
Pandas
NumPy
Matplotlib
Project Structure
phishing-email-detector/
│
├── dataset.csv
├── train_model.py
├── detector.py
├── phishing_model.pkl
├── vectorizer.pkl
└── README.md
Dataset Format

Your dataset (dataset.csv) should have:

email_text	label
Click here to verify account http://fake.com
	phishing
Meeting scheduled at 5 PM	safe
Installation
pip install pandas scikit-learn numpy matplotlib
How to Train the Model
python train_model.py

This will:

Train the model
Show accuracy and confusion matrix
Generate phishing_model.pkl and vectorizer.pkl
How to Test Emails
python detector.py

Enter an email message and the model will predict whether it is Phishing or Safe.

Example Output
Enter email text: Verify your bank account at http://secure-login.com

Prediction: Phishing
Learning Outcomes
Text feature extraction with TF-IDF
URL and keyword analysis
Machine learning classification
Model evaluation techniques
Future Improvements
Add GUI interface
Use advanced NLP models
Real-time email scanning
