import os
import telebot

BOT_TOKEN = '6776280637:AAEVk4zdCUuE9TeCPsrxVrf4c-Jeu5uXGvM'
os.environ['BOT_TOKEN'] = BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

bot.polling()