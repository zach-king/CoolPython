"""
File: gov-bills-scraper.py
Author: Zachary King
Description: A web scraper that retrieves the top 10
	viewed bills in Congress currently. Simply prints
	out their title and bill number.
"""

import requests
from bs4 import BeautifulSoup

url = "https://www.congress.gov/resources/display/content/Most-Viewed+Bills"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
for i, bill in enumerate(soup.find_all("td", {"class":"confluenceTd"})[:30]):
	try:
		print(bill.text)
	except:
		pass
	if (i+1) % 3 == 0:
		print("\n")
