from bs4 import BeautifulSoup
from urllib import urlopen

url = "https://github.com/zach-king?tab=repositories"
content = urlopen(url).read()

soup = BeautifulSoup(content, "html.parser")

for repo in soup.find_all("h3", {"class":"repo-list-name"}):
	children = repo.children
	for child in children:
		print(child)
