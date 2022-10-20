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
    item_tomorrow = types.KeyboardButton("Завтра")
    item1 = types.KeyboardButton("На неделю")
    markdown.add(item_today, item_tomorrow, item1)
    bot.send_message(message.chat.id, 'Добро пожаловать!\n',  reply_markup=markdown)



@bot.message_handler(content_types = ['text'])
def add_message(message):
    if message.chat.type == 'private':
        if message.text == 'Сегодня':
            bot.send_message(message.chat.id, read_file('11А Понедельник.txt'))
        elif message.text == 'На неделю':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Понедельник", callback_data='day1')
            item2 = types.InlineKeyboardButton("Вторник", callback_data='day2')
            item3 = types.InlineKeyboardButton("Среда", callback_data='day3')
            item4 = types.InlineKeyboardButton("Четверг", callback_data='day4')
            item5 = types.InlineKeyboardButton("Пятница", callback_data='day5')
            item6 = types.InlineKeyboardButton("Суббота", callback_data='day6')
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Расписание на неделю', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'day1':
        bot.send_message(call.message.chat.id, 'круто' )
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Выдано расписание на понедельник ✅")
    elif call.data == 'day2':
        bot.send_message(call.message.chat.id, ' ')
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Выдано расписание на вторник ✅")
    elif call.data == 'day3':
        bot.send_message(call.message.chat.id, ' ')
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Выдано расписание на среду ✅")
    elif call.data == 'day4':
        bot.send_message(call.message.chat.id, ' ')
        bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Выдано расписание на четверг ✅")



bot.polling(none_stop=True)