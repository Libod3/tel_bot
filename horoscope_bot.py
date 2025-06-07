import telebot
from tmp import get_supporter_b1

bot = telebot.TeleBot("7389746767:AAFk13WSXbrw8Nu9ce5Nac1X_15lj-IgYS8")
API = "99cb9e798fmsh417cc6381083be6p1014fcjsn847bb94bfa59"  # Не уверен в надобности API


# zodiac_signs = {
#     "Aries": "овен",
#     "Taurus": "телец",
#     "Gemini": "близнецы",
#     "Cancer": "рак",
#     "Leo": "лев",
#     "Virgo": "дева",
#     "Libra": "весы",
#     "Scorpio": "скорпион",
#     "Sagittarius": "стрелец",
#     "Capricorn": "козерог",
#     "Aquarius": "водолей",
#     "Pisces": "рыбы",
# }


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=3)

    btn_aries = telebot.types.InlineKeyboardButton("Овен", callback_data="aries")
    btn_taurus = telebot.types.InlineKeyboardButton("Телец", callback_data="taurus")
    btn_gemini = telebot.types.InlineKeyboardButton("Близнецы", callback_data="gemini")
    btn_cancer = telebot.types.InlineKeyboardButton("Рак", callback_data="cancer")
    btn_leo = telebot.types.InlineKeyboardButton("Лев", callback_data="leo")
    btn_virgo = telebot.types.InlineKeyboardButton("Дева", callback_data="virgo")
    btn_libra = telebot.types.InlineKeyboardButton("Весы", callback_data="libra")
    btn_scorpio = telebot.types.InlineKeyboardButton("Cкорпион", callback_data="scorpio")
    btn_sagittarius = telebot.types.InlineKeyboardButton("Cтрелец", callback_data="sagittarius")
    btn_capricorn = telebot.types.InlineKeyboardButton("Козерог", callback_data="capricorn")
    btn_aquarius = telebot.types.InlineKeyboardButton("Водолей", callback_data="aquarius")
    btn_pisces = telebot.types.InlineKeyboardButton("Рыбы", callback_data="pisces")

    markup.add(btn_aries, btn_taurus, btn_gemini, btn_cancer, btn_leo, btn_virgo, btn_libra, btn_scorpio,
               btn_sagittarius, btn_capricorn, btn_aquarius, btn_pisces)
    bot.send_message(message.chat.id,
                     "Привет, я Гороскоп \n"
                     "Подскажи, какой у тебя знак зодиака",
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    bot.send_message(callback.message.chat.id, f"Твоё предсказание: {get_supporter_b1(callback.message.text)}")


bot.polling(none_stop=True)
