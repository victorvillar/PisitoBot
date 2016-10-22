import telebot
import os.path as path
import sys
from subprocess import call

# Create bot with its token
if not path.isfile("bot.token"):
    print("Error: \"bot.token\" not found!")
    sys.exit()

with open("./bot.token", "r") as TOKEN:
    bot = telebot.TeleBot(TOKEN.readline().strip())

# Ignorar mensajes antiguos
bot.skip_pending = True

# Handlers


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Soy el puto bot de idun")

@bot.message_handler(commands=['miautube'])
def send_video(message):
    call("ytb" + message.text)
    bot.send_message(message.chat.id, "MiauTube")

# Start the bot
print("Running...")
bot.polling()
