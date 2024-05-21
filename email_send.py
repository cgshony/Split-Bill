"""
This script defines a function to send automated emails with PDF attachments of the monthly bill using the SMTP protocol.
It includes the setup for the SMTP server, creation of the email content, and attachment of the PDF file.
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

def send_email(from_email, to_email, subject, body, attachment_path):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'shony.alexandrova@gmail.com'  # Replace with your email
    smtp_password = 'jbhh sqpt uvmq psvq'  # Replace with your app-specific password

   # Create the email body
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body))

    # Attach the file
    with open(attachment_path, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='pdf')
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
        msg.attach(attachment)

    # Send the email
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.send_message(msg)

send_email('shony.alexandrova@gmail.com','shony.alexandrova@gmail.com', 'Email with attachment', 'Please find attached the monthly bill.', r'D:\Personal\Python-study\Split-Bill\january.pdf')
print('Email sent succesfully!')





#Code contribution: https://keentolearn.medium.com/automating-emails-with-python-a-comprehensive-guide-ba00fa98b92