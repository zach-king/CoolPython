import requests
from bs4 import BeautifulSoup
import os
from urllib import request as req
from tkinter import *

url = "http://c.xkcd.com/random/comic/"
filename = ''
title = ''

def getRandomComic():
	global url, filename, title, photo, photo_label, caption
	try:
		r = requests.get(url)
		soup = BeautifulSoup(r.content)
		comic = soup.find_all("div", {"id": "comic"})

		opener = req.build_opener()
		req.install_opener(opener)

		img = comic[0].find_all("img")[0]
		link = 'http:' + img['src']
		title = img['alt']

		filename = "C:/Users/Zach/Pictures/comic.png"
		img_data = opener.open(link)
		f = open(filename, 'wb')
		f.write(img_data.read())
		f.close()

		photo = PhotoImage(file=filename)
		photo_label.config(image=photo)
		caption.config(text=title)
	except:
		caption.config(text="Sorry, try again")


def callback(event):
	getRandomComic()

# GUI Work
root = Tk()
root.title("xkcd Random Comic")

photo = PhotoImage(file=filename)
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