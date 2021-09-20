import requests
import telebot
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
TOKEN = config["DEFAULT"]["token"]

bot = telebot.TeleBot(TOKEN)
user = bot.get_me()
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	cid = message.chat.id
	print(cid)
	bot.reply_to(message, "Serega have very little dick!")

bot.polling()

#
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
