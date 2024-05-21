import smtplib

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'shony.alexandrova@gmail.com'  # Replace with your email
smtp_password = '****'  # Replace with your app-specific password

from_email = 'shony.alexandrova@gmail.com'
to_email = 'shony.alexandrova@gmail.com'
subject = 'Hello, world!'
body = 'This is a test email.'

message = f'Subject: {subject}\n\n{body}'

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(from_email, to_email, message)




