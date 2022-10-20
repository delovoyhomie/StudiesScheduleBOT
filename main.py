import telebot
from token_bot import token
from telebot import types
bot = telebot.TeleBot(token)


def read_file(name):
    f = open(name, 'r', encoding="utf-8")
    a = f.read()
    f.close()
    return a
@bot.message_handler(commands=['start']) # команда /start
def welcome(message):
    markdown = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item_today = types.KeyboardButton("Сегодня")
    markdown.add(item_today)
    item_tomorrow = types.KeyboardButton("Завтра")
    markdown.add(item_tomorrow)
    item1 = types.KeyboardButton("На неделю")
    markdown.add(item1)
    bot.send_message(message.chat.id, 'Добро пожаловать!\n',  reply_markup=markdown)



@bot.message_handler(content_types = ['text'])
def add_message(message):
    if message.chat.type == 'private':
        if message.text == 'Сегодня':
            bot.send_message(message.chat.id, read_file('11А Понедельник.txt'))






bot.polling(none_stop=True)