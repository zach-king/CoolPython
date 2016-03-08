import smtplib
from getpass import getpass
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
username = input("Enter your email address: ")
password = getpass(prompt="Enter your password: ")
server.login(username, password)

recipient = input("\nEnter Recipient Email Address: ")
subject = input("Enter Subject: ")
msg = input("\nEnter message: ")

mail = MIMEText(msg)
mail['Subject'] = subject
mail['From'] = username
mail['To'] = recipient

# Send mail
server.send_message(mail)
server.quit()
