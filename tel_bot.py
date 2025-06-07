import telebot
from random import randint

bot = telebot.TeleBot("7254662710:AAEWVqYJrmzmXYt7DfSXND1rvbGNB5gUaDM")


@bot.message_handler(commands=["start"])
def start_bot(message):
    bot.send_message(message.chat.id, "привет")


@bot.message_handler(commands=["help"])
def help_bot(message):
    bot.send_message(message.chat.id, "/start - команда которая <u>запустит бота</u> \n"
                                      "/info - команда, которая выдаёт <u>информацию о сообщении</u> \n"
                                      "/gift - прикольчик для Сони \n",
                     parse_mode="html")


@bot.message_handler(commands=["info"])
def info_bot(message):
    bot.send_message(message.chat.id, f"{message.from_user.id} - ваше ID в системе телеграма")


@bot.message_handler(commands=["gift"])
def gift_bot(message):
    num = randint(0, 3)
    with open(f"img{num}.png", 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, f"ты Солнышко")


@bot.message_handler()
def often_text(message):
    if message.text.lower() == "что ты умеешь":
        bot.send_message(message.chat.id, "пока что совсем ничего")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
