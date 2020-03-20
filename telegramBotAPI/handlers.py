import globals, telegram
from postManager import cleanPost

def addme_handler(self, update):
	ID = update.message.from_user.id
	if ID in globals.inspectors:
		update.message.reply_text('You were inspector already.')
	else:
		update.message.reply_text('Ok, you are inspector now.')
		globals.inspectors.append(ID)

def callback_handler(bot, update):
	answer = update.callback_query.data[0]
	message = update.callback_query.message
	post_id = update.callback_query.data.split()[1]
	if globals.unreviewedPosts[str(post_id)][1]=='text':
		if answer == 'Y':
			bot.edit_message_text(chat_id = message.chat_id, message_id = message.message_id, text = 'The post has been accepted by you.')
			cleanPost(from_id = message.chat_id, post_id = post_id, result = True, post_method = 'text', bot = bot)
		elif answer == 'N':
			bot.edit_message_text(chat_id = message.chat_id, message_id = message.message_id, text = 'The post has been rejected by you.')
			cleanPost(from_id = message.chat_id, post_id = post_id, result = False, post_method = 'text', bot = bot)
	else:
		if answer == 'Y':
			bot.edit_message_media(chat_id = message.chat_id, message_id = message.message_id, media = telegram.InputMediaPhoto(open('ok.png', 'rb'), caption='The post has been accepted by you.'))
			cleanPost(from_id = message.chat_id, post_id = post_id, result = True, post_method = 'photo', bot = bot)
		elif answer == 'N':
			bot.edit_message_media(chat_id = message.chat_id, message_id = message.message_id, media = telegram.InputMediaPhoto(open('no.png', 'rb'), caption='The post has been rejected by you.'))
			cleanPost(from_id = message.chat_id, post_id = post_id, result = False, post_method = 'photo', bot = bot)
