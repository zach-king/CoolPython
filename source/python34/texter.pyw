# TEXTER.py
# Created By Zachary King
# Aug 28, 2014
# open-source
# www.binarybyron.com
import smtplib
from tkinter import *

def sendText():
	email = emailBox.get()
	password = passBox.get()
	to = recBox.get()
	subject = subBox.get()
	carrier = carrierBox.get()
	if (carrier == "AT&T"):
		to += "@txt.att.net"
	elif (carrier == "Verizon"):
		to += "@vtext.com"
	elif (carrier == "Sprint"):
		to += "@messaging.sprintpcs.com"
	elif (carrier == "T-Mobile"):
		to += "@tmomail.net"
	elif (carrier == "Virgin Mobile"):
		to += "@vmobl.com"
	else:
		return None
	msg = msgBox.get(0.0, END)
	msg = 'Subject: %s\n\n%s' % (subject, msg)
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, to, msg)
	server.quit()
	msgBox.delete(0.0, END)



root = Tk()
root.title("Texter")


emailBox = Entry(root)
passBox = Entry(root, show="*")
recBox = Entry(root)
subBox = Entry(root)
carrierBox = Spinbox(root, wrap=True, values=("AT&T", "Verizon", "Sprint", "T-Mobile", "Virgin Mobile"), state="readonly")
msgBox = Text(root, wrap=WORD)
sendButton = Button(root, text="Send", command=sendText)

emailBox.pack(fill=X, expand=1)
passBox.pack(fill=X, expand=1)
recBox.pack(fill=X, expand=1)
carrierBox.pack(fill=X, expand=1)
subBox.pack(fill=X, expand=1)
msgBox.pack(fill=BOTH, expand=1)
sendButton.pack(fill=X, expand=1)

emailBox.insert(0, "yourgmailhere@gmail.com")
recBox.insert(0, "##########")
subBox.insert(0, "subject here")

root.mainloop()
