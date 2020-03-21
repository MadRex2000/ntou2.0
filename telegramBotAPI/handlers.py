import globals, telegram
from postManager import cleanPost, editPost

def addme_handler(bot, update):
	ID = update.message.from_user.id
	if ID in globals.inspectors:
		update.message.reply_text('You were inspector already.')
	else:
		update.message.reply_text('Ok, you are inspector now.')
		globals.inspectors.append(ID)

def callback_handler(bot, update):
	answer = update.callback_query.data[0]
	post_id = update.callback_query.data.split()[1]
	from_id = update.callback_query.message.chat_id
	# Maybe it can speed up...
	for i in globals.posts[post_id].owners:
		if i[0] == from_id:
			if i[2] == True:
				return
			else:
				i[2] = True
				break
	if answer == 'Y':
		editPost(post_id, True, bot)
	elif answer == 'N':
		editPost(post_id, False, bot)