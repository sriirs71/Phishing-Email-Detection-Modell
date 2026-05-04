import pandas as pd
import random

# A script to generate a synthetic dataset of emails for training

phishing_templates = [
    "URGENT: Your account has been compromised. Please click here to login and verify your identity: http://secure-login-update.com",
    "Dear customer, your invoice is attached. Please review the payment details urgently. http://billing-update-now.com",
    "You have won a $1000 gift card! Click here to claim your prize now: http://claim-your-prize.net/win",
    "Security Alert: We detected unusual activity on your account. Verify your password immediately at http://verify-account-security.info",
    "Action Required: Your password expires in 24 hours. Update it now or lose access: http://password-reset-portal.org"
]

safe_templates = [
    "Hi team, just a reminder that our weekly meeting is at 10 AM tomorrow. Please review the attached agenda.",
    "Hey John, thanks for the update on the project. Let's catch up later this week.",
    "Your recent order #12345 has been shipped. You can track your package using the tracking link on our website.",
    "Please find attached the Q3 financial report for your review. Let me know if you have any questions.",
    "Happy Birthday! Hope you have a wonderful day. Best wishes from all of us."
]

def generate_emails(num_samples=200):
    data = []
    
    # Generate Phishing Emails
    for _ in range(num_samples // 2):
        base_email = random.choice(phishing_templates)
        # Add some random variations
        if random.random() > 0.5:
            base_email = "ATTENTION! " + base_email
        data.append({"text": base_email, "label": "Phishing"})
        
    # Generate Safe Emails
    for _ in range(num_samples // 2):
        base_email = random.choice(safe_templates)
        if random.random() > 0.5:
            base_email = "FYI: " + base_email
        data.append({"text": base_email, "label": "Safe"})
        
    # Shuffle dataset
    random.shuffle(data)
    
    df = pd.DataFrame(data)
    df.to_csv("emails.csv", index=False)
    print(f"Generated synthetic dataset with {len(df)} samples and saved to emails.csv.")

if __name__ == "__main__":
    generate_emails(500)
