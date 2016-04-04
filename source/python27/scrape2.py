from bs4 import BeautifulSoup
from urllib2 import urlopen

url = "http://www.github.com/zach-king/CoolPython"
content = urlopen(url).read()

soup = BeautifulSoup(content)

for link in soup.find_all('a'):
	print(link.get('href'))
