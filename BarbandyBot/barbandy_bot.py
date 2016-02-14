from twx.botapi import TelegramBot
token = '<>'
bot = TelegramBot(token)
while True:
	updates = bot.get_updates().wait()
	for update in updates:
		if update.message.text.startswith('/start'):
			bot.send_message(update.message.chat.id, 'test message body')
