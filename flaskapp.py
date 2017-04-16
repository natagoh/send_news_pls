from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
from scraper import get_titles
from scraper import get_urls
from scraper import scrape_article
import time

app = Flask(__name__)
#type your twilio function here
# Your Account SID from twilio.com/console
account_sid = "AC5997488c9e6295744ee09ef1f2c09f39"
# Your Auth Token from twilio.com/console
auth_token  = "99f4423365f738d8fd7a4ed4bb4bc973"
client = Client(account_sid, auth_token)
firstResponse = True
nHeadlines = len(get_titles())


def formatHeadlines(list):
	result = ""
	for x in range(0, len(list)-1):
		result = result + str(x+1) + ". " + list[x] + "\n"
	return result

def formatHeadlines(list):
	result = ""
	for x in range(0, len(list)-1):
		result = result + str(x+1) + ". " + list[x] + "\n"
	return result

headlines = formatHeadlines(get_titles())
urlList = get_urls()

def chunks(s,n):
	 return [s[i:i+n] for i in range(0, len(s), n)]

# SMS 
message = client.messages.create(
	to="+18048190626", 
	from_="+14159916397",
	body="Welcome to SendNewsPls: Would you like today's headlines? y/Y for Yes, n/N for No")

@app.route("/", methods=['GET', 'POST'])

def respond(): 
	user_response = request.form['Body']
	global firstResponse 
	if firstResponse:
		if user_response == 'y' or user_response == 'Y':
			resp = MessagingResponse().message(headlines)
			return str(resp)
		elif user_response == 'n' or user_response == 'N':
			resp = MessagingResponse().message("Have a nice day!")
		else:
			resp = MessagingResponse().message("invalid input")

	user_response2 = request.form['Body']
	resp1="blah"

	if user_response2 > 0 :
		user_response2 = request.form['Body']
		print str(user_response2)
		article = scrape_article(urlList[int(user_response2)-1])
		art_list = chunks(article,1500)
		for i in xrange(len(art_list)):
			x = art_list[i]
			resp1 = MessagingResponse().message(x)
			print resp1          
	return str(resp1)

if __name__ == "__main__":
    app.run()
