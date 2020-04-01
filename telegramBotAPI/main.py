#pipenv run python3 main.py
import configparser
import logging
import telegram
from flask import Flask, request
from telegram.ext import *

from handlers import addme_handler, callback_handler
from postManager import newPost, cleanPost, editPost

import globals
globals.initialize()

# Load data from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
bot = telegram.Bot(token=str(config['TELEGRAM']['ACCESS_TOKEN']))

@app.route('/hook', methods=['POST'])
def webhook_handler():
	"""Set route /hook with POST method will trigger this method."""
	if request.method == "POST":
		#print(type(request.get_json(force=True)))
		update = telegram.Update.de_json(request.get_json(force=True), bot)
		# Update dispatcher process that handler to process this message
		dispatcher.process_update(update)
	return 'ok'

# New a dispatcher for bot
dispatcher = Dispatcher(bot, None)

# Add handler for handling message, there are many kinds of message. For this handler, it particular handle text
# message.

dispatcher.add_handler(CommandHandler('addme', addme_handler))
dispatcher.add_handler(CallbackQueryHandler(callback_handler))

@app.route('/operate', methods=['POST'])
def readPosts():
	if request.remote_addr != '127.0.0.1': return 'ok'
	if request.method == 'POST':
		if request.values['method'] == 'post':
			newPost(request, bot)
		else:
			if request.values['id'] in globals.posts:
				result = True if request.values['result'] == 'True' else False
				if request.values['method'] == 'vote':
					editPost(request.values['id'], result, bot)
				elif request.values['method'] == 'clean':
					cleanPost(request.values['id'], result, bot)
	return 'ok'

if __name__ == "__main__":
	app.run()
