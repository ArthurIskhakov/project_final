from database import *
import telebot
from telebot import types
from main_parsing import *

Token = '5653636541:AAEcL-OPzYeqFnDkrowOXAfnhfpVxA8GlyE'
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = types.KeyboardButton('Вчера')
    item_2 = types.KeyboardButton('Сегодня')
    item_3 = types.KeyboardButton('Завтра')
    markup.add(item_1, item_2, item_3)
    bot.send_message(message.chat.id, 'Здравствуйте '
                     + message.from_user.first_name + '\n'
                     + 'Выберите день за который хотите посмотреть '
                       'список матчей или результаты',
                     reply_markup=markup)
    add_in_data_base(message.from_user.id,
                     message.from_user.first_name,
                     message.from_user.last_name, message.text)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    match message.text:
        case 'Сегодня':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_1 = types.KeyboardButton('Английская премьер-лига')
            item_2 = types.KeyboardButton('Итальянская Серия А')
            item_3 = types.KeyboardButton('Немецкая Бундес лига')
            item_4 = types.KeyboardButton('Испанская Ла лига')
            item_5 = types.KeyboardButton('Французская Лига 1')
            back = types.KeyboardButton('Назад')
            markup.add(item_1, item_2, item_3, item_4, item_5, back)
            bot.send_message(message.chat.id,
                             'Список сегодняшних матчей️⬇',
                             reply_markup=markup)
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Завтра':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_6 = types.KeyboardButton('Английская премьер-лигa')
            item_7 = types.KeyboardButton('Итальянская Серия A')
            item_8 = types.KeyboardButton('Немецкая Бундес лигa')
            item_9 = types.KeyboardButton('Испанская Ла лигa')
            item_10 = types.KeyboardButton('Французская Лигa 1')
            back = types.KeyboardButton('Назад')
            markup.add(item_6, item_7, item_8, item_9, item_10, back)
            bot.send_message(message.chat.id, 'Список завтрашних матчей️⬇',
                             reply_markup=markup)
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Вчера':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_11 = types.KeyboardButton('Aнглийскaя премьер-лигa󠁢󠁥󠁧󠁢󠁥󠁮󠁧󠁿')
            item_12 = types.KeyboardButton('Итaльянская Серия А')
            item_13 = types.KeyboardButton('Немецкaя Бундес лига')
            item_14 = types.KeyboardButton('Испaнскaя Ла лига')
            item_15 = types.KeyboardButton('Фрaнцузская Лига')
            back = types.KeyboardButton('Назад')
            markup.add(item_11, item_12, item_13, item_14, item_15, back)
            bot.send_message(message.chat.id, 'Результаты вчерашних матчей️⬇',
                             reply_markup=markup)
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Английская премьер-лига':
            url = 'https://777score.ru/'
            bot.send_message(message.chat.id,
                             parsing(league_id['EPL'],
                                     league_country['EPL'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Итальянская Серия А':
            url = 'https://777score.ru/'
            bot.send_message(message.chat.id,
                             parsing(league_id['Seria_A'],
                                     league_country['Seria_A'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Испанская Ла лига':
            url = 'https://777score.ru/'
            bot.send_message(message.chat.id,
                             parsing(league_id['La_liga'],
                                     league_country['La_liga'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Немецкая Бундес лига':
            url = 'https://777score.ru/'
            bot.send_message(message.chat.id,
                             parsing(league_id['Bundes_Liga'],
                                     league_country['Bundes_Liga'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Французская Лига 1':
            url = 'https://777score.ru/'
            bot.send_message(message.chat.id,
                             parsing(league_id['League_One'],
                                     league_country['League_One'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)

        case 'Английская премьер-лигa':
            url = 'https://777score.ru/tomorrow'
            bot.send_message(message.chat.id,
                             parsing(league_id['EPL'],
                                     league_country['EPL'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Итальянская Серия A':
            url = 'https://777score.ru/tomorrow'
            bot.send_message(message.chat.id,
                             parsing(league_id['Seria_A'],
                                     league_country['Seria_A'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Испанская Ла лигa':
            url = 'https://777score.ru/tomorrow'
            bot.send_message(message.chat.id,
                             parsing(league_id['La_liga'],
                                     league_country['La_liga'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Немецкая Бундес лигa':
            url = 'https://777score.ru/tomorrow'
            bot.send_message(message.chat.id,
                             parsing(league_id['Bundes_Liga'],
                                     league_country['Bundes_Liga'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Французская Лигa 1':
            url = 'https://777score.ru/tomorrow'
            bot.send_message(message.chat.id,
                             parsing(league_id['League_One'],
                                     league_country['League_One'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)

        case 'Aнглийскaя премьер-лигa󠁢󠁥󠁧󠁢󠁥󠁮󠁧󠁿':
            url = 'https://777score.ru/yesterday'
            bot.send_message(message.chat.id,
                             parsing(league_id['EPL'],
                                     league_country['EPL'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Итaльянская Серия А':
            url = 'https://777score.ru/yesterday'
            bot.send_message(message.chat.id,
                             parsing(league_id['Seria_A'],
                                     league_country['Seria_A'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Испaнскaя Ла лига':
            url = 'https://777score.ru/yesterday'
            bot.send_message(message.chat.id,
                             parsing(league_id['La_liga'],
                                     league_country['La_liga'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Немецкaя Бундес лига':
            url = 'https://777score.ru/yesterday'
            bot.send_message(message.chat.id,
                             parsing(league_id['Bundes_Liga'],
                                     league_country['Bundes_Liga'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Фрaнцузская Лига':
            url = 'https://777score.ru/yesterday'
            bot.send_message(message.chat.id,
                             parsing(league_id['League_One'],
                                     league_country['League_One'], url))
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_16 = types.KeyboardButton('Вчера')
            item_17 = types.KeyboardButton('Сегодня')
            item_18 = types.KeyboardButton('Завтра')
            markup.add(item_16, item_17, item_18)
            bot.send_message(message.chat.id,
                             'Выберите день за который хотите посмотреть '
                             'список матчей или результаты',
                             reply_markup=markup)
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)
        case _:
            bot.send_message(message.chat.id, 'Нажмите на одну из кнопок')
            add_in_data_base(message.from_user.id,
                             message.from_user.first_name,
                             message.from_user.last_name, message.text)


bot.polling(none_stop=True)