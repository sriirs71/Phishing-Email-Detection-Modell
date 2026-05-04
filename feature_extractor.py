import re
from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class EmailFeatureExtractor(BaseEstimator, TransformerMixin):
    """
    Custom Scikit-Learn transformer to extract specific features from email text.
    """
    def __init__(self):
        # Suspicious keywords commonly found in phishing emails
        self.suspicious_words = ['urgent', 'password', 'login', 'verify', 'account', 'update', 'click here', 'won', 'prize', 'compromised']
        
    def fit(self, X, y=None):
        return self # Nothing to fit
        
    def transform(self, X, y=None):
        """
        Extracts features from an array/Series of email strings.
        Returns a 2D numpy array of features.
        """
        features = []
        for email in X:
            email_lower = str(email).lower()
            
            # 1. Count URLs (HTTP/HTTPS)
            url_count = len(re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', email_lower))
            
            # 2. Count Suspicious Keywords
            keyword_count = sum(email_lower.count(word) for word in self.suspicious_words)
            
            # 3. Email Length
            length = len(email_lower)
            
            # 4. Contains HTML tags
            contains_html = int(bool(re.search(r'<[^>]+>', email_lower)))
            
            features.append([url_count, keyword_count, length, contains_html])
            
        return np.array(features)

def get_text_data(X):
    """
    Helper function to select text data for the Pipeline.
    Placed here so it can be safely pickled/unpickled by joblib.
    """
    return X

