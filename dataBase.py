import sqlite3
import telebot
from telebot import types
bot = telebot.TeleBot('6364860659:AAE6ZY3vaulobWUx2g7pj3sPTVNSmUxlcBU')

print('Введите нужную команду цифрой\n')
commands = ['Вывести все записи', 'Добавить', 'Удалить'];
flag1 = False
for i in range(len(commands)):
    print(i ,'-' ,commands[i])
command = int(input())

while flag1 == False:
    if command < len(commands):
        flag1 = True
    if(flag1 == False):
        print('Вы ввели неверную команду, попробуйте ввести снова')
        command = int(input())


try:
    connect = sqlite3.connect('mydatabase.db')

    cursor = connect.cursor()

    cursor.execute('''CREATE TABLE if not exists "users" (
        "id"	INTEGER NOT NULL,
        "login"	INTEGER NOT NULL UNIQUE,
        "password"	INTEGER NOT NULL UNIQUE,
        PRIMARY KEY("id" AUTOINCREMENT)
    ); ''')
    connect.commit()

    cursor.execute('''CREATE TABLE if not exists "categories" (
        "id"	INTEGER NOT NULL,
        "name"	INTEGER NOT NULL UNIQUE,
        PRIMARY KEY("id" AUTOINCREMENT)
    ); ''')
    connect.commit()

    cursor.execute('''CREATE TABLE if not exists "subsribes" (
        "id_users"	INTEGER NOT NULL,
        "id_categories"	INTEGER NOT NULL UNIQUE,
        PRIMARY KEY("id_users" AUTOINCREMENT)
    ); ''')
    connect.commit()
    categories =[]
    categories = cursor.execute('SELECT name FROM categories').fetchall()
    connect.commit()



    if commands[command] == 'Вывести все записи':
        print('Список всех записей в базе данных:')
        for i in range(len(categories)):
            print(i, categories[i])
    elif commands[command] == 'Добавить':
        print('Введите название категории')
        categ = input()
        likes = cursor.execute('''SELECT name FROM categories WHERE name=?''',(categ, )).fetchall()
        while len(likes) > 0:
            print('Такая запись уже есть в базе, введите другое название')
            categ = input()
            likes = cursor.execute('''SELECT name FROM categories WHERE name=?''', (categ,)).fetchall()
        cursor.execute('''INSERT INTO categories (name) VALUES(?)''',(categ, ))
        connect.commit()
        print('Запись успешно добавлена в базу данных')
    elif commands[command] == 'Удалить':
        print('Введите номер категории, которую желаете удалить')
        for i in range(len(categories)):
            print(i, categories[i])
        id = int(input())
        flag = False
        while flag == False:
            for i in range(len(categories)):
                if i == id:
                    flag = True
            if flag == False:
                print('Вы ввели неверный id, попробуйте ввести снова')
                id = input()
        cat = list(categories[id])
        cursor.execute('''DELETE FROM categories WHERE name=?''', (cat[0],))
        connect.commit()
        print('Запись успешно удалена')

    cursor.close()





    # def fetch(message):
    #     return cursor.execute('SELECT * FROM categories').fetchall()
    #
    # def add(message):
    #     bot.reply_to(message.chat.id, 'Выберите действие, которое вы хотите выполнить')
    #     # cursor.execute('''INSERT INTO users (name) VALUES(?)'''(message,))
    #     connect.commit()
    #
    # def delete(message):
    #     login = message.text.strip()
    #     password = message.text.strip()
    #     cursor.execute('''Delete categories (login, password) VALUES(?, ?)''',(login))
    #     connect.commit()
    #
    # cursor.close()


    bot.polling(none_stop=True, interval=0)


except sqlite3.Error as error:
    print('Ошибка при подключении к sqlite', error)







#
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Вывести все записи')
#     btn2 = types.KeyboardButton('Добавить')
#     btn3 = types.KeyboardButton('Удалить')
#     markup.row(btn2, btn3)
#     markup.row(btn1)
#     print('Нажата кнопка')
#     bot.send_message(message.chat.id, 'Выберите нужную кнопку', reply_markup=markup)
#     bot.register_message_handler(message, on_click)
#     print('Нажата кнопка')
#
#     bot.polling(none_stop=True)
#
# def on_click(message):
#     if message.text == 'Вывести все записи':
#         print('Нажата кнопка вывести')
#         bot.send_message(message.chat.id, 'Все записи: ')
#         bot.register_message_handler(message, fetch)
#     elif message.text == 'Добавить':
#         bot.send_message(message.chat.id, 'Все записи: ')
#         bot.register_message_handler(message, add)
#     elif message.text == 'Удалить':
#         bot.send_message(message.chat.id, 'Все записи: ')
#         bot.register_message_handler(message, delete)
#
# try:
#     connect = sqlite3.connect('mydatabase.db')
#
#     cursor = connect.cursor()
#
#     cursor.execute('''CREATE TABLE if not exists "users" (
#         "id"	INTEGER NOT NULL,
#         "login"	INTEGER NOT NULL UNIQUE,
#         "password"	INTEGER NOT NULL UNIQUE,
#         PRIMARY KEY("id" AUTOINCREMENT)
#     ); ''')
#     connect.commit()
#
#     cursor.execute('''CREATE TABLE if not exists "categories" (
#         "id"	INTEGER NOT NULL,
#         "name"	INTEGER NOT NULL UNIQUE,
#         PRIMARY KEY("id" AUTOINCREMENT)
#     ); ''')
#     connect.commit()
#
#     cursor.execute('''CREATE TABLE if not exists "subsribes" (
#         "id_users"	INTEGER NOT NULL,
#         "id_categories"	INTEGER NOT NULL UNIQUE,
#         PRIMARY KEY("id_users" AUTOINCREMENT)
#     ); ''')
#     connect.commit()
#
#     def fetch(message):
#         return cursor.execute('SELECT * FROM categories').fetchall()
#
#     def add(message):
#         bot.reply_to(message.chat.id, 'Выберите действие, которое вы хотите выполнить')
#         # cursor.execute('''INSERT INTO users (name) VALUES(?)'''(message,))
#         connect.commit()
#
#     def delete(message):
#         login = message.text.strip()
#         password = message.text.strip()
#         cursor.execute('''INSERT INTO users (login, password) VALUES(?, ?)''',
#                                 (login))
#         connect.commit()
#
#     cursor.close()
#
#
#     bot.polling(none_stop=True, interval=0)
#
#
# except sqlite3.Error as error:
#     print('Ошибка при подключении к sqlite', error)
