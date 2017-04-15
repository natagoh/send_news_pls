from scraper import get_titles
from scraper import get_urls
from scraper import scrape_article

def formatHeadlines(list):
	result = ""
	for x in range(0, len(list)-1):
		result = result + str(x+1) + ". " + list[x] + "\n"
	return result

titles = get_titles()
links = get_urls()

# headlines
#for x in titles:
#	print(x)
print(formatHeadlines(titles))

# urls
#for x in links:
#	print(x)

# scrape articles
#for x in links:
#	scrape_article(x)

#print(titles[0])

print(scrape_article(links[1]))