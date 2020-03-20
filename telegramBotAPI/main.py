#pipenv run python3 main.py
import configparser
import logging
import threading
import telegram
from flask import Flask, request
from telegram.ext import *

from handlers import addme_handler, callback_handler
from postManager import newPost, cleanPost
import globals


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

@app.route('/', methods=['POST'])
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

# Simulating the database operation
def readPosts():
	while True:
		try:	s = input().split()
		except:	continue
		# New post format: post text/photo post_id
		if s[0] == 'post': newPost(s, bot)
		# Reply post format: accept/reject post_id
		elif s[0] == 'accept':
			if s[1] in globals.unreviewedPosts:
				cleanPost(0, int(s[1]), True, globals.unreviewedPosts[s[1]][1], bot)
		elif s[0] == 'reject':
			if s[1] in globals.unreviewedPosts:
				cleanPost(0, int(s[1]), False, globals.unreviewedPosts[s[1]][1], bot)
readPostsThread = threading.Thread(target=readPosts)

if __name__ == "__main__":
	globals.initialize()
	readPostsThread.start()
	app.run()
