import os
from ftplib import FTP
import sys
import getpass
from tkinter import *

class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''
    def __init__(self,text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self,msg):
        self.text_area.config(state=NORMAL)
        self.text_area.insert(END, msg)
        self.text_area.config(state=DISABLED)

class App:
    def __init__(self, master):
        self.CreateWidgets(master)
        sys.stdout = StdoutRedirector(self.output)
        self.ftp = None
        self.inputEntry.bind('<Return>', self.Command)
        print("Welcome to the Python FTP Client")
        print("Use 'help' to show commands\n")

    def ShowCommands(self):
        print("\nCommands:\n-------------")
        print("cd <dir>       : change current working directory")
        print("ls             : output the current working directory listing")
        print("rm <file>      : delete file")
        print("rmd <dir>      : delete directory")
        print("mkdir <dir>    : create new directory")
        print("dl <file>      : download file")
        print("ul <file>      : upload file")
        print("rn <old> <new> : rename old file to new file")
        print("clear          : clears screen")
        print("exit           : disconnect\n")

    def Echo(self, msg):
        self.output.config(state=NORMAL)
        self.output.insert(END, msg + "\n")
        self.output.config(state=DISABLED)

    def ClearScreen(self):
        self.output.config(state=NORMAL)
        self.output.delete(1.0, END)
        self.output.config(state=DISABLED)

    def Upload(self, file):
        try:
            ext = os.path.splitext(file)[1]
            if ext in (".txt", ".htm", ".html"):
                self.ftp.storlines("STOR " + file, open(file))
            else:
                self.ftp.storbinary("STOR " + file, open(file, 'rb'), 1024)
        except:
            print("Failed to upload file...")

    def Connect(self):
        host = self.hostEntry.get()
        user = self.usernameEntry.get()
        passwd = self.passwordEntry.get()
        try:
            self.ftp = FTP(host)
            self.ftp.login(user=user, passwd=passwd)
            print("Successfully connected to " + host + " as " + user + "...")
        except:
            print("Unable to connect...")

    def CreateWidgets(self, master):
        self.loginFrame = Frame(master)
        self.loginFrame.pack()

        Label(self.loginFrame, text="Host: ").pack()
        self.hostEntry = Entry(self.loginFrame)
        self.hostEntry.pack()
        Label(self.loginFrame, text="Username: ").pack()
        self.usernameEntry = Entry(self.loginFrame)
        self.usernameEntry.pack()
        Label(self.loginFrame, text="Password: ").pack()
        self.passwordEntry = Entry(self.loginFrame, show="*")
        self.passwordEntry.pack()
        self.connectButton = Button(self.loginFrame, text="Connect", command=self.Connect)
        self.connectButton.pack()

        self.outputFrame = Frame(master)
        self.outputFrame.pack()

        self.output = Text(self.outputFrame, state=DISABLED)
        self.output.pack()

        self.inputFrame = Frame(master)
        self.inputFrame.pack()

        Label(self.inputFrame, text="Command: ").pack()
        self.inputEntry = Entry(self.inputFrame)
        self.inputEntry.pack()

    def Command(self, event):
        if self.ftp == None:
            print("Not connected...")
        command = self.inputEntry.get()
        self.inputEntry.delete(0, END)
        if command == "help":
            self.ShowCommands()
            return
        try:
            if command[:2] == 'cd':
                # change dir
                d = command.split(' ')[1]
                self.ftp.cwd(d)
                print(">> cd " + d)
            elif command[:2] == 'rm' and len(command.split(' ')[0]) == 2:
                # remove file
                f = command.split(' ')[1]
                self.ftp.delete(f)
            elif command[:2] == 'dl':
                # download file
                f = command.split(' ')[1]
                self.ftp.retrbinary("RETR " + f, open("download_" + f, 'wb').write)
            elif command[:2] == 'ls':
                # show listing
                print(self.ftp.dir())
            elif command[:2] == 'rn':
                # rename file
                old = command.split(' ')[1]
                new = command.split(' ')[2]
                self.ftp.rename(old, new)
            elif command[:2] == 'ul':
                # upload new file
                f = command.split(' ')[1]
                self.Upload(f)
            elif command[:3] == 'rmd':
                # remove directory
                d = command.split(' ')[1]
                self.ftp.rmd(d)
            elif command[:5] == 'mkdir':
                # make new directory
                d = command.split(' ')[1]
                self.ftp.mkd(d)
            elif command == "clear":
                # clear screen
                self.ClearScreen()
            elif command == "exit":
                # exit app
                try:
                    self.ftp.quit()
                    sys.exit()
                except:
                    sys.exit()
            else:
                print("Invalid command. Try again...\n")
        except:
            print("Invalid command. Try again...\n")



def main():
    root = Tk()
    app = App(root)
    root.mainloop()
    sys.stdout = sys.__stdout__



if __name__ == "__main__":
    main()