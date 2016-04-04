from bs4 import BeautifulSoup
from urllib2 import urlopen

url = "http://www.github.com/zach-king/CoolPython"
content = urlopen(url).read()
print(content)

soup = BeautifulSoup(content)

print(soup.prettify())
print(soup.title)
print(soup.title.string)
print(soup.p)
print(soup.a)
