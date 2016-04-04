from bs4 import BeautifulSoup
import os
from Tkinter import *
from urllib2 import urlopen
import base64

url = "http://c.xkcd.com/random/comic/"
title = ""
img_data = ""

def getRandomComic():
	global url, img_data, title, photo, photo_label, caption
#	try:
	r = urlopen(url).read()
	soup = BeautifulSoup(r)
	comic = soup.find_all("div", {"id": "comic"})

	img = comic[0].find_all("img")[0]
	link = 'http:' + img['src']
	title = img['alt']

	img_data = urlopen(link).read()
	img_data = base64.encodestring(img_data)

	photo = PhotoImage(data=img_data)
	photo_label.config(image=photo)
	caption.config(text=title)
#	except:
#		caption.config(text="Sorry, try again")


def callback(event):
	getRandomComic()

# GUI Work
root = Tk()
root.title("xkcd Random Comic")

photo = PhotoImage(data=img_data)
photo_label = Label(image=photo)
photo_label.grid()
photo_label.image = photo

caption = Label(text=title)
caption.grid()

getComicButton = Button(root, text="Random Comic", command=getRandomComic)
getComicButton.grid()

getRandomComic()

root.bind("<Button-1>", callback)

root.mainloop()
