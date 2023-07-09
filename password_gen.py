import hashlib
import os
import time
import smtplib
from email.mime.text import MIMEText

def get_hash(file_path):
    hasher = hashlib.sha1()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def send_email(subject, body, to, email, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.send_message(msg)
    server.quit()

file_path = input("Enter the file path: ")
email = input("Enter the email address to send the alert: ")
password = input("Enter the email password: ")
email_to = input("Enter the email address to receive the alert: ")
previous_hash = get_hash(file_path)
while True:
    current_hash = get_hash(file_path)
    if current_hash != previous_hash:
        send_email("ALERT: File Hash Changed", f"The hash of the file at {file_path} has changed", email_to, email, password)
        previous_hash = current_hash
    time.sleep(60)
