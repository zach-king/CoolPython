import smtplib
from getpass import getpass
from email.mime.text import MIMEText

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
username = raw_input("Enter your email address: ")
password = getpass(prompt="Enter your password: ")
server.login(username, password)

recipient = raw_input("\nEnter Recipient Email Address: ")
subject = raw_input("Enter Subject: ")
msg = raw_input("\nEnter message: ")
msg = 'Subject: %s\n\n%s' % (subject, msg)

mail = MIMEText(msg)
mail['Subject'] = subject
mail['From'] = username
mail['To'] = recipient

# Send mail
server.sendmail(username, recipient, msg)
server.quit()
