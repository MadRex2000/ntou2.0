from globals import Posts
import globals, telegram

def newPost(request, bot):
	thisPost = Posts(request.values['text'], request.values['type'], [0, 0])
	text =  request.values['text'] + '\n\nAccept: {}, Reject:{}'.format(0,0)
	post_id = request.values['id']
	buttons = [[telegram.InlineKeyboardButton('Accept', callback_data = 'Y {}'.format(post_id)), telegram.InlineKeyboardButton('Reject', callback_data = 'N {}'.format(post_id))]]
	reply_markup = telegram.InlineKeyboardMarkup(buttons)
	owners = [] # Will add in the posts
	if thisPost.post_method == 'photo':
		address = request.values['address']
		address = 'testimg.jpg' # for debug
		for i in globals.inspectors:
			msg = bot.send_photo(chat_id = i, photo = open(address, 'rb'), caption = text, reply_markup = reply_markup)
			owners.append([msg.chat.id, msg.message_id, False])
	elif thisPost.post_method == 'text':
		for i in globals.inspectors:
			msg = bot.send_message(chat_id = i, text = text, reply_markup = reply_markup)
			owners.append([msg.chat.id, msg.message_id, False])
	thisPost.setOwners(owners)
	globals.posts[str(post_id)] = thisPost

def editPost(post_id, result, bot):
	if result is True:		globals.posts[str(post_id)].status[0]+=1
	elif result is False:	globals.posts[str(post_id)].status[1]+=1
	buttons = [[telegram.InlineKeyboardButton('Accept', callback_data = 'Y {}'.format(post_id)), telegram.InlineKeyboardButton('Reject', callback_data = 'N {}'.format(post_id))]]
	reply_markup = telegram.InlineKeyboardMarkup(buttons)
	thisPost = globals.posts[str(post_id)]
	text = thisPost.text+'\n\nAccept: {}, Reject: {}'.format(thisPost.status[0], thisPost.status[1])
	if thisPost.post_method == 'text':
		for i in thisPost.owners:
			if i[2] is True:
				bot.edit_message_text(chat_id = i[0], message_id = i[1], text = text)
			else:
				bot.edit_message_text(chat_id = i[0], message_id = i[1], text = text, reply_markup = reply_markup)
	elif thisPost.post_method == 'photo':
		for i in thisPost.owners:
			if i[2] is True:
				bot.edit_message_caption(chat_id = i[0], message_id = i[1], caption = text)
			else:
				bot.edit_message_caption(chat_id = i[0], message_id = i[1], caption = text, reply_markup = reply_markup)

def cleanPost(post_id, result, bot):
	if result is True:		text = 'The post has been accepted.'
	elif result is False: 	text = 'The post has been rejected.'
	thisPost = globals.posts[str(post_id)]
	text += '\n\nAccept: {}, Reject: {}'.format(thisPost.status[0], thisPost.status[1])
	if thisPost.post_method == 'text':
		for i in thisPost.owners:
			bot.edit_message_text(chat_id = i[0], message_id = i[1], text = text)
	elif thisPost.post_method == 'photo':
		media = telegram.InputMediaPhoto(open('ok.png' if result else 'no.png', 'rb'), caption = text)
		for i in thisPost.owners:
			bot.edit_message_media(chat_id = i[0], message_id = i[1], media = media)
	del globals.posts[str(post_id)]
