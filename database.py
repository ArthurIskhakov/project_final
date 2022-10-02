import sqlite3
import datetime


def add_in_data_base(id, first_name, last_name, message_text):
    date = datetime.date.today()
    current_date_time = datetime.datetime.now()
    time = current_date_time.time()
    bot_data_base = sqlite3.connect('bot.db')
    cursor = bot_data_base.cursor()
    cursor.execute(f"INSERT INTO main_data_base VALUES('{id}', "
                   f"'{first_name}', '{last_name}', '{date}', '{time}'"
                   f", '{message_text}')")
    bot_data_base.commit()
    bot_data_base.close()


def today_users(date):   #дата в формате гггг-мм-дд
    bot_data_base = sqlite3.connect('bot.db')
    cursor = bot_data_base.cursor()
    cursor.execute(f"SELECT id, "
                   f"first_name FROM main_data_base WHERE date = '{date}'")
    users = cursor.fetchall()
    if len(users) == 0:
        return 'Нет данных за этот день'
    else:
        return users


def number_of_users_today(day):
    all_list = today_users(day)
    if all_list == 'Нет данных за этот день':
        return 'Количество уникальных пользователей не доступно'
    else:
        unique_users = set(all_list)
        return len(unique_users)
print('dsfg')




