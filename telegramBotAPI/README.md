# telegramBotAPI

This program controls the telegramBot to send message to users for reviewing the post .

## Getting Started

### Requirements

- Python 3
    + pipenv
    + python-telegram-bot
    + flask
- ngrok

### Virtual Environment Building

Create the virtual environment:

	cd $menu
	pipenv install --three python-telegram-bot flask gunicorn requests

Now your project menu would add two files:

	Project Directory
	├── Pipfile.lock
	└── Pipfile

Create `config.ini` in the same menu:

	vim config.ini

Add your telegram bot access token in config file:

	[TELEGRAM]
	ACCESS_TOKEN = YOUR_TOKEN

Add `no.png` and `ok.png` for reply message.

### Apply a domain for develpoment and test

Using `ngrok` apply for a temporary domain:

	ngrok http 5000

And copy the **https** url.

Going here to set webhook for your telegramBot:
http://api.telegram.org/botYOUR_TOKEN_HERE/setWebhook?url=WEBHOOK_URL

## Finally, run the bot server

Confrim your menu like this:

	Project Directory
	├── config.ini
	├── main.py
	├── no.png
	├── ok.png
	├── Pipfile
	└── Pipfile.lock

And run the bot:

	pipenv run python3 main.py

## How to use

### User Commands

+ /addme: Add the user who send this command to the inspectors list, you can add a verification function for this.

### Server Operations

Since the bot is in development stage, it use `input()` function for simulating the database's operations.

#### input() Format

+ post_text:

		post text post_id
		Content...

+ post_photo:

		post photo (post_id)
		Content...
		photoAddress

+ vote_post:
	
	vote post_id Y/N
	

+ accept_post:

		accept post_id

+ reject_post:

		reject post_id
