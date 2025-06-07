import telebot
import sqlite3

bot = telebot.TeleBot("7254662710:AAEWVqYJrmzmXYt7DfSXND1rvbGNB5gUaDM")
name = None


@bot.message_handler(commands=["start"])
def bot_start(message):
    conn = sqlite3.connect("users_data.sql")
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users ('
                'id int auto_increment primary key,'
                'name varchar(50),'
                'password varchar(50)'
                ')')

    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "привет, сейчас вас зарегестрируем, введите ваше имя")
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, "Теперь введите пароль")
    bot.register_next_step_handler(message, user_password)


def user_password(message):
    password = message.text.strip()

    conn = sqlite3.connect("users_data.sql")
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, password) VALUES ("%s", "%s")' % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton("Список пользователей", callback_data="users"))
    bot.send_message(message.chat.id, "Вы зарегистрированы", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback(callback):
    conn = sqlite3.connect("users_data.sql")
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ""
    for el in users:
        info += f'Имя: {el[1]}, паколь: {el[2]}\n'

    cur.close()
    conn.close()
    bot.send_message(callback.message.chat.id, info)


bot.polling(none_stop=True)
