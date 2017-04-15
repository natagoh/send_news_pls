import requests
from bs4 import BeautifulSoup

# scrapes article given url
def scrape_article(str):
	url = str
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html, "html.parser")
	page = soup.find("div", class_="body-text").getText()
	print(page)
	return 

# run overlord function
def get_titles():
	url = 'http://abc7news.com/place/palo-alto/'
	response = requests.get(url)
	html = response.content

	# get top stories
	soup = BeautifulSoup(html, "html.parser")

	# parse top stores further to get headline titles
	links = []
	headlines = []
	for foo in soup.find_all("div", class_="top-stories-group"):
		headlines = foo.find_all("div", class_="headline")

	# get headline titles
	titles = []
	for x in headlines:
		title = str(x)
		title_1 = title.replace("<div class=\"headline\">", "")
		title_2 = title_1[:-6]
		titles.append(title_2)

	# urls
	#for link in links:
	#	print(link)

	# headlines
	#for title in titles:
	#	print(title)

	# scrapes the urls of main articles
	#for link in links:
	#	scrape_article(link)

	return titles

def get_urls():
	url = 'http://abc7news.com/place/palo-alto/'
	response = requests.get(url)
	html = response.content

	# get top stories
	soup = BeautifulSoup(html, "html.parser")

	# parse top stores further to get headline titles
	links = []
	headlines = []
	for foo in soup.find_all("div", class_="top-stories-group"):
		headlines = foo.find_all("div", class_="headline")
		# get urls
		for a in foo.find_all("a", href=True):
			prefix = "http://abc7news.com"
			links.append(prefix+str(a['href']))


	return links




