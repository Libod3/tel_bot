import json

import telebot
import requests

bot = telebot.TeleBot("7254662710:AAEWVqYJrmzmXYt7DfSXND1rvbGNB5gUaDM")
API = "0db20a58a243ab7ebc078d73daaf2480"


@bot.message_handler(commands=["start"])
def start_bot(message):
    bot.send_message(message.chat.id, "Привет, напиши название города")


@bot.message_handler(content_types=["text"])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']

        if temp >= 18.0:
            image = "sun.jpg"
        else:
            image = "sun_with_wind.jpg"

        with open(image, 'rb') as img:
            bot.send_photo(message.chat.id, img)
        bot.send_message(message.chat.id, f"Температура в городе {message.text}: {temp} °С")

    else:
        bot.send_message(message.chat.id, f"Такого города не существует")


bot.polling(none_stop=True)