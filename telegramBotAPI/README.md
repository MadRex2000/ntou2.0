# telegramBotAPI

This program controls the telegramBot to send message to users for reviewing the post .

## Getting Started

### Requirements

- Python 3
    + python-telegram-bot
    + flask

### Virtual Environment Building

Create the virtual environment:

	$python3 -m venv venv
	$source /venv/bin/activate
	(venv) $pip install falsk
	(venv) $pip install python-telegram-bot

Create `config.ini` in the same menu:

	(venv) $vim config.ini

Add your telegram bot access token in config file:
Add your public ip address in config file:

	[TELEGRAM]
	ACCESS_TOKEN = YOUR_TOKEN
	[HOST]
	IP = YOUR_IPADDRESS


Add `no.png` and `ok.png` for reply message.
*Add `testimg.jpg` for image post test.*

### Deployed your app

We use nginx + uwsgi.
*For the test, you can use `ngrok`, and copy the `https` link.*

Going here to set webhook for your telegramBot:
http://api.telegram.org/botYOUR_TOKEN_HERE/setWebhook?url=WEBHOOK_URL/**hook**

## Finally, run the bot server

Confirm your menu like this:

	Project Directory
	├── config.ini
	├── main.py
	├── no.png
	└── ok.png

And run the bot:

	(venv) $ python3 main.py


## How to use

### User Commands

+ /addme: Add the user who send this command to the inspectors list, you can add a verification function for this.

### Database Operations

+ Send the information to http://localhost:5000/operate, by JSON.
+ Format:
  - PostNewText: { 'method':'post', 'type':'text', 'id':'POST_ID', 'text':'CONTENT'}
  - PostNewPhoto: { 'method':'post', 'type':'photo', 'id':'POST_ID', 'text':'CONTENT', 'address':'PHOTO'S_ADDRESS'}
  - Vote, Accept or Reject Post: { 'method':'vote/clean', 'id':'POST_ID', 'result':'True/False'}
