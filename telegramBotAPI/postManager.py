import globals
import telegram
def newPost(content, bot):
	post_id = content[2]
	post_method = content[1]
	text = input()
	buttons = [[telegram.InlineKeyboardButton('Accept', callback_data = 'Y {}'.format(post_id)), telegram.InlineKeyboardButton('Reject', callback_data = 'N {}'.format(post_id))]]
	reply_markup = telegram.InlineKeyboardMarkup(buttons)

	lst = [] # Will add in the unreviewedPosts dict
	if post_method == 'photo':
		address = input()
		address = 'testimg.jpg' # for debug
		for i in globals.inspectors:
			msg = bot.send_photo(chat_id = i, photo = open(address, 'rb'), caption = text, reply_markup = reply_markup)
			lst.append((msg.chat.id, msg.message_id))
	elif post_method == 'text':
		for i in globals.inspectors:
			msg = bot.send_message(chat_id = i, text = text, reply_markup = reply_markup)
			lst.append((msg.chat.id, msg.message_id))
	globals.unreviewedPosts[str(post_id)] = (lst, post_method)

def cleanPost(from_id, post_id, result, post_method, bot):
	if result is True:		text = 'The post has been accepted by others.'
	elif result is False: 	text = 'The post has been rejected by others.'
	for i in globals.unreviewedPosts[str(post_id)][0]:
			if i[0] != from_id:
				if post_method == 'text':
					bot.edit_message_text(chat_id = i[0], message_id  = i[1], text = text)
				elif post_method == 'photo':
					bot.edit_message_media(chat_id = i[0], message_id = i[1], media = telegram.InputMediaPhoto(open('ok.png' if result else 'no.png', 'rb'), caption = text))
	del globals.unreviewedPosts[str(post_id)]
