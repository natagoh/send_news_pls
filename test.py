from scraper import get_titles
from scraper import get_urls
from scraper import scrape_article

titles = get_titles()
links = get_urls()

# headlines
for x in titles:
	print(x)

# urls
for x in links:
	print(x)

# scrape articles
for x in links:
	scrape_article(x)