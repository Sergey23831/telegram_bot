import requests
import telebot
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
TOKEN = config["DEFAULT"]["token"]

bot = telebot.TeleBot(TOKEN)
user = bot.get_me()

# # setWebhook
# bot.set_webhook(url="http://example.com", certificate=open('mycert.pem'))
# # unset webhook
# bot.remove_webhook()

# getUpdates
updates = bot.get_updates()
updates = bot.get_updates(1234,100,20) #get_Updates(offset, limit, timeout):

#sendMessage
bot.send_message(chat_id=817923363, text="ok")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	cid = message.chat.id
	name = message.from_user.first_name
	print(cid)
	bot.reply_to(message, f"{name} have very little dick!")
	bot.send_message(817923363, text=cid)

bot.polling()

#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
