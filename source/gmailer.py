import smtplib
from Tkinter import *

def SendMail():
	toaddrs = toBox.get()
	fromaddrs = fromBox.get()
	username = fromBox.get()
	password = passBox.get()
	msg = msgBox.get(0.0, END)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(username, password)
	server.sendmail(toaddrs, fromaddrs, msg)
	server.quit()

root = Tk()
root.title("G-Mailer")
root.minsize(width=600, height=500)

fromBox = Entry(root, width=45)
passBox = Entry(root, width=40, show="*")
toBox = Entry(root, width=45)
msgBox = Text(root, wrap=WORD)
sendButton = Button(root, text="Send Mail", command=SendMail)


fromBox.insert(0, "from@gmail.com")
toBox.insert(0, "to@email.com")
msgBox.insert(0.0, "Message Here...")

fromBox.pack(fill=X, expand=1)
passBox.pack(fill=X, expand=1)
toBox.pack(fill=X, expand=1)

msgBox.pack(side=TOP, fill=BOTH, expand=1)
sendButton.pack(side=TOP, fill=X, expand=1)


root.mainloop()