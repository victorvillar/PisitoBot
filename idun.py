# - * - coding: UTF-8 - * -
import telebot
import os
import sys
import time
import string
import random

# Create bot with its token
if not os.path.isfile("bot.token"):
    print("Error: \"bot.token\" not found!")
    sys.exit()

with open("./bot.token", "r") as TOKEN:
    bot = telebot.TeleBot(TOKEN.readline().strip())

# Ignorar mensajes antiguos
bot.skip_pending = True

# Handlers


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Soy Idhún, dame gelatina")

@bot.message_handler(commands=['miautube'])
def send_video(message):
    bot.send_message(message.chat.id, "[MiauTube] *mordisco*")
    mordisco = open('./mordisco.mp4', 'rb')
    bot.send_document(message.chat.id, mordisco)
    time_before = time.time()
    os.system("youtubeplayer " + message.text.split()[1])
    time_after = time.time()
    if (time_after - time_before < 30):
        bot.send_message(message.chat.id, "[MiauTube] Trying hard mode")
	hardMode(message.text.split()[1])
        bot.send_message(message.chat.id, "[MiauTube] HardMode success")
    else:
        bot.send_message(message.chat.id, "[MiauTube] Over")

@bot.message_handler(commands=['miautwitch'])
def send_video(message):
    bot.send_message(message.chat.id, "[MiauTwitch] *arañazo*")
    os.system("twitchtv " + message.text.split()[1] + " " + message.text.split()[2])
    bot.send_message(message.chat.id, "[MiauTwitch] Over")

def hardMode(message):
    #TODO: Move to bin
	code = message.split("=")[1]
        random="&r=" + key_gen() + "&hd=1"
        r = os.system("wget --auth-no-challenge http://www.youtubeinmp4.com/redirect.php?video=" + code + random)
        video = "redirect.php?video=" + code
        if (r == 0):
            os.system("omxplayer "+ video)
            os.system("rm " + video)
        else:
            print("Meh")


KEY_LEN = 48

def base_str():
    return (string.letters+string.digits)
def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))


# Start the bot
print("Nya...")
bot.polling()
