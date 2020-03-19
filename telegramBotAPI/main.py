#pipenv run python3 main.py
import configparser
import logging

import threading

import telegram
from flask import Flask, request
from telegram.ext import *

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

inspectors = []
# Todo: Add a token to check if somebody can be inspector
def addme_handler(bot, update):
	ID = update.message.from_user.id
	if ID in inspectors:
		update.message.reply_text('You were inspector already.')
	else:
		update.message.reply_text('Ok, you are inspector now.')
		inspectors.append(ID)

unreviewedPosts = {}

def cleanPost(from_id, post_id, result, post_method):
	if result is True:		text = 'The post has been accepted by others.'
	elif result is False: 	text = 'The post has been rejected by others.'
	for i in unreviewedPosts[str(post_id)][0]:
			if i[0] != from_id:
				if post_method == 'text':
					bot.edit_message_text(chat_id = i[0], message_id  = i[1], text = text)
				elif post_method == 'photo':
					bot.edit_message_media(chat_id = i[0], message_id = i[1], media = telegram.InputMediaPhoto(open('ok.png' if result else 'no.png', 'rb'), caption = text))
	del unreviewedPosts[str(post_id)]

def callback_handler(bot, update):
	answer = update.callback_query.data[0]
	message = update.callback_query.message
	post_id = update.callback_query.data.split()[1]
	if unreviewedPosts[str(post_id)][1]=='text':
		if answer == 'Y':
			bot.edit_message_text(chat_id = message.chat_id, message_id = message.message_id, text = 'The post has been accepted by you.')
			cleanPost(from_id = message.chat_id, post_id = post_id, result = True, post_method = 'text')
		elif answer == 'N':
			bot.edit_message_text(chat_id = message.chat_id, message_id = message.message_id, text = 'The post has been rejected by you.')
			cleanPost(from_id = message.chat_id, post_id = post_id, result = False, post_method = 'text')
	else:
		if answer == 'Y':
			bot.edit_message_media(chat_id = message.chat_id, message_id = message.message_id, media = telegram.InputMediaPhoto(open('ok.png', 'rb'), caption='The post has been accepted by you.'))
			cleanPost(from_id = message.chat_id, post_id = post_id, result = True, post_method = 'photo')
		elif answer == 'N':
			bot.edit_message_media(chat_id = message.chat_id, message_id = message.message_id, media = telegram.InputMediaPhoto(open('no.png', 'rb'), caption='The post has been rejected by you.'))
			cleanPost(from_id = message.chat_id, post_id = post_id, result = False, post_method = 'photo')

def newPost(content):
	post_id = content[2]
	post_method = content[1]
	text = input()
	buttons = [[telegram.InlineKeyboardButton('Accept', callback_data = 'Y {}'.format(post_id)), telegram.InlineKeyboardButton('Reject', callback_data = 'N {}'.format(post_id))]]
	reply_markup = telegram.InlineKeyboardMarkup(buttons)

	lst = [] # Will add in the unreviewedPosts dict
	if post_method == 'photo':
		address = input()
		address = 'testimg.jpg' # for debug
		for i in inspectors:
			msg = bot.send_photo(chat_id = i, photo = open(address, 'rb'), caption = text, reply_markup = reply_markup)
			lst.append((msg.chat.id, msg.message_id))
	elif post_method == 'text':
		for i in inspectors:
			msg = bot.send_message(chat_id = i, text = text, reply_markup = reply_markup)
			lst.append((msg.chat.id, msg.message_id))
	unreviewedPosts[str(post_id)] = (lst, post_method)

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
		if s[0] == 'post': newPost(content = s)
		# Reply post format: accept/reject from_id post_id
		elif s[0] == 'accept':
			if s[1] in unreviewedPosts:
				cleanPost(0, int(s[1]), True, unreviewedPosts[s[1]][1])
		elif s[0] == 'reject':
			if s[1] in unreviewedPosts:
				cleanPost(0, int(s[1]), False, unreviewedPosts[s[1]][1])
readPostsThread = threading.Thread(target=readPosts)

if __name__ == "__main__":
	readPostsThread.start()
	app.run()
