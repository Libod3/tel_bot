import telebot
import webbrowser


bot = telebot.TeleBot("7254662710:AAEWVqYJrmzmXYt7DfSXND1rvbGNB5gUaDM")


@bot.message_handler(commands=["start"])
def start_bot(message):
    markup = telebot.types.ReplyKeyboardMarkup()

    button1 = telebot.types.KeyboardButton("Перейти на сайт")
    button2 = telebot.types.KeyboardButton("Удалить фото")
    button3 = telebot.types.KeyboardButton("Изменить текст")

    markup.row(button1)
    markup.row(button2, button3)

    bot.send_message(message.chat.id, "Привет", reply_markup=markup)

    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "Перейти на сайт":
        webbrowser.open(url="https://www.youtube.com/watch?v=RpiWnPNTeww&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=3")
        bot.send_message(message.chat.id, "Готово")
    elif message.text == "Удалить фото":
        bot.delete_message(message.chat.id, message.message_id - 1)
        bot.delete_message(message.chat.id, message.message_id)
    elif message.text == "Изменить текст":
        bot.edit_message_text("Текст изменен", message.chat.id, message.message_id - 1)


@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = telebot.types.InlineKeyboardMarkup()

    button1 = telebot.types.InlineKeyboardButton("Перейти на сайт", url="https://www.youtube.com/watch?v=RpiWnPNTeww&list=PL0lO_mIqDDFUev1gp9yEwmwcy8SicqKbt&index=3")
    button2 = telebot.types.InlineKeyboardButton("Удалить фото", callback_data="delete")
    button3 = telebot.types.InlineKeyboardButton("Изменить текст", callback_data="edit")

    markup.row(button1)
    markup.row(button2, button3)

    bot.reply_to(message, "Какое красивое фото", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "delete":
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == "edit":
        bot.edit_message_text("Edit message", callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)