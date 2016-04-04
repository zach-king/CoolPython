import smtplib
from Tkinter import *

# Function for retrieving the credentials,
# and sending the mail
def SendMail():
    # Retrieve data
    toaddrs = toBox.get()
    fromaddrs = fromBox.get()
    username = fromBox.get()
    subject = subjectBox.get()
    password = passBox.get()
    msg = msgBox.get(0.0, END)
    msg = "Subject: %s\n\n%s" % (subject, msg)

    # Create the SMTP object, login, and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddrs, toaddrs, msg)

    # Then quit (logout).
    server.quit()


# Create the GUI
root = Tk()
root.title("G-Mailer")
root.minsize(width=600, height=500)

fromBox = Entry(root, width=45)
passBox = Entry(root, width=40, show="*")
toBox = Entry(root, width=45)
subjectBox = Entry(root, width=45)
msgBox = Text(root, wrap=WORD, highlightbackground="black")
sendButton = Button(root, text="Send Mail", command=SendMail)


fromBox.insert(0, "from@gmail.com")
toBox.insert(0, "to@gmail.com")
msgBox.insert(0.0, "Message Here...")

Label(root, text="Username: ").grid(row=0, column=0, sticky=W)
fromBox.grid(row=0, column=1, sticky=W+E)

Label(root, text="Password: ").grid(row=1, column=0, sticky=W)
passBox.grid(row=1, column=1, sticky=W+E)

Label(root, text="To: ").grid(row=2, column=0, sticky=W)
toBox.grid(row=2, column=1, sticky=W+E)

Label(root, text="Subject: ").grid(row=3, column=0, sticky=W)
subjectBox.grid(row=3, column=1, sticky=W+E)

msgBox.grid(row=4, column=0, columnspan=2, rowspan=5,
    sticky=W+E+N+S)
sendButton.grid(row=9, column=0, columnspan=2, sticky=W+E)


root.mainloop()
