import telebot
from token_bot import token
from telebot import types
bot = telebot.TeleBot(token)
import datetime

def send(da):
    def day_week(d):
        if da == 0:
            d = 'пн'
        elif da == 1:
            d = 'вт'
        elif da == 2:
            d = 'ср'
        elif da == 3:
            d = 'чт'
        elif da == 4:
            d = 'пт'
        elif da == 5:
            d = 'сб'
        return d

    global d
    d = day_week(da)
    print(d)
    check(id, d)
    bot.send_message(id_int, print_file(a_print, b_print, c_print))
def send_day(time):
    da = datetime.datetime.today().weekday()
    da+=time
    def day_week(d):
        if da == 0:
            d = 'пн'
        elif da == 1:
            d = 'вт'
        elif da == 2:
            d = 'ср'
        elif da == 3:
            d = 'чт'
        elif da == 4:
            d = 'пт'
        elif da == 5:
            d = 'сб'
        return d

    global d
    d = day_week(da)
    print(d)
    check(id, d)
    bot.send_message(id_int, print_file(a_print, b_print, c_print))

def print_file(number, letter, len):
    global b_print
    b_print = letter
    print('len:', len)
    f = open('Расписание/' + str(number) + letter + ' ' + len + '.txt', 'r', encoding="utf-8")
    a = f.read()
    f.close()
    return a

def write_the_class_id(id, number, letter):
    f = open('Классы/' + 'Регистрация' + '.txt', 'a', encoding="utf-8")
    f.write(id + ' ' + number + letter + '\n')
    f.close()


def check(id, len):
    global a_print
    global c_print
    f = open('Классы/' + 'Регистрация' + '.txt', 'r', encoding="utf-8")
    mass = f.readlines()
    mass.reverse()
    print(mass)
    number = mass[0][10:-2]
    for i in mass:
        if i == id + ' ' + str(number) + 'A' or i == id + ' ' + str(number) + 'A' + '\n':
            print('number:', str(number), 'A')
            print_file(str(number), 'А', len)
            f.close()
            a_print = number
            c_print = len
            return 0

        elif i == id + ' ' + str(number) + 'B' or i == id + ' ' + str(number) + 'B' + '\n':
            print('good')
            print_file(str(number), 'Б', len)
            f.close()
            a_print = number
            c_print = len
            return 0
        elif i == id + ' ' + str(number) + 'V' or i == id + ' ' + str(number) + 'V' + '\n':
            print('good')
            print_file(str(number), 'В', len)
            f.close()
            a_print = number
            c_print = len
            return 0
        elif i == id + ' ' + str(number) + 'G' or i == id + ' ' + str(number) + 'G' + '\n':
            print('good')
            print_file(str(number), 'Г', len)
            f.close()
            a_print = number
            c_print = len
            return 0
@bot.message_handler(commands=['start']) # команда /start
def welcome(message):
    markdown = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    item_today = types.KeyboardButton("Сегодня")
    item_tomorrow = types.KeyboardButton("Завтра")
    item1 = types.KeyboardButton("На неделю")
    markdown.add(item_today, item_tomorrow, item1)
    bot.send_message(message.chat.id, 'Добро пожаловать!\n \nЗарегистрируйтесь',  reply_markup=markdown)

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("7", callback_data='class7')
    item2 = types.InlineKeyboardButton("8", callback_data='class8')
    item3 = types.InlineKeyboardButton("9", callback_data='class9')
    item4 = types.InlineKeyboardButton("10", callback_data='class10')
    item5 = types.InlineKeyboardButton("11", callback_data='class11')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Выбери свой класс', reply_markup=markup)
    global id
    id = str(message.chat.id)
    print('id:', message.chat.id)
    global id_int
    id_int = message.chat.id

    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("А", callback_data='classA')
    item2 = types.InlineKeyboardButton("Б", callback_data='classB')
    item3 = types.InlineKeyboardButton("В", callback_data='classV')
    item4 = types.InlineKeyboardButton("Г", callback_data='classG')
    markup.add(item1, item2, item3, item4)
    bot.send_message(id, 'Выбери свою букву', reply_markup=markup)

@bot.message_handler(content_types = ['text'])
def add_message(message):
    if message.chat.type == 'private':
        if message.text == 'Сегодня':
            print('сегодня')
            send_day(0) # + 0 дней, потому что сегодня
        elif message.text == 'Завтра':
            print('завтра')
            send_day(1) # + 1 день, потому что завтра
        elif message.text == 'На неделю':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item = types.InlineKeyboardButton("На всю неделю", callback_data='all')
            item1 = types.InlineKeyboardButton("Понедельник", callback_data='day1')
            item2 = types.InlineKeyboardButton("Вторник", callback_data='day2')
            item3 = types.InlineKeyboardButton("Среда", callback_data='day3')
            item4 = types.InlineKeyboardButton("Четверг", callback_data='day4')
            item5 = types.InlineKeyboardButton("Пятница", callback_data='day5')
            item6 = types.InlineKeyboardButton("Суббота", callback_data='day6')
            markup.add(item)
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Расписание на неделю', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global class_number
    global class_letter

    if call.data == 'class7':
        print(id)
        class_number = 7
    elif call.data == 'class8':
        print(id)
        class_number = 8
    elif call.data == 'class9':
        print(id)
        class_number = 9
    elif call.data == 'class10':
        print(id)
        class_number = 10
    elif call.data == 'class11':
        print(id)
        class_number = 11

    elif call.data == 'classA':
        class_letter = 'A'
        write_the_class_id(str(id), str(class_number), class_letter)
        bot.send_message(call.message.chat.id, 'Вы успешно зарегистрировались ✅')
    elif call.data == 'classB':
        class_letter = 'Б'
        write_the_class_id(str(id), str(class_number), class_letter)
        bot.send_message(call.message.chat.id, 'Вы успешно зарегистрировались ✅')
    elif call.data == 'classV':
        class_letter = 'В'
        write_the_class_id(str(id), str(class_number), class_letter)
        bot.send_message(call.message.chat.id, 'Вы успешно зарегистрировались ✅')
    elif call.data == 'classG':
        class_letter = 'Г'
        write_the_class_id(str(id), str(class_number), class_letter)
        bot.send_message(call.message.chat.id, 'Вы успешно зарегистрировались ✅')

    elif call.data == 'all':
        send(0) # понедельник
        send(1)# вторник
        send(2)# среда
        send(3)# четверг
        send(4)# пятница
        send(5)# суббота
    elif call.data == 'day1': send(0)
    elif call.data == 'day2': send(1)
    elif call.data == 'day3': send(2)
    elif call.data == 'day4': send(3)
    elif call.data == 'day5': send(4)
    elif call.data == 'day6': send(5)


bot.polling(none_stop=True)