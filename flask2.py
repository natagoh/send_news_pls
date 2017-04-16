from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio import twiml
from scraper import get_titles
from scraper import get_urls
from scraper import scrape_article

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

headlines = formatHeadlines(get_titles())
urlList = get_urls()

def formatHeadlines(list):
	result = ""
	for x in range(0, len(list)-1):
		result = result + str(x+1) + ". " + list[x] + "\n"
	return result

message = client.messages.create(
	to="+18048190626", 
	from_="+14159916397",
	#from_="+"
	body="Welcome to SendNewsPls: Would you like today's headlines? 1 for Yes, 2 for No")


@app.route("/", methods=['GET', 'POST'])

def respond(): 
	user_response = request.form['Body']
	global firstResponse 
	if firstResponse:
		if user_response == '1a':
			resp = MessagingResponse().message(headlines)
			return str(resp)
		else:
			resp = MessagingResponse().message("Have a nice day!")
		#firstResponse = False

	user_response2 = request.form['Body']
	resp1="blah"

	if user_response2 > 0 :
		user_response2 = request.form['Body']
		print str(user_response2)
		article = scrape_article(urlList[int(user_response2)-1])
		resp1 = MessagingResponse().message(article)
		print(article)
		print(resp1)
	return str(resp1)

if __name__ == "__main__":
    app.run()
