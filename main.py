import telebot
from telebot import types

import random

import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot('_')


@bot.message_handler(commands=['start'])         #command_start
def start_message(message):

  mess = f'Привет, {message.from_user.first_name}, я твой личный библиотекарь.'

  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button1 = types.KeyboardButton(f'Главное меню')
  button2 = types.KeyboardButton(f'Помощь')
  markup.add(button1, button2)

  bot.send_message(message.chat.id, mess, reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Главное меню' or message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(f'Онлайн библиотека')
        btn2 = types.KeyboardButton(f'Книги на английском')
        btn3 = types.KeyboardButton(f'Что почитать?')
        btn4 = types.KeyboardButton(f'Мемы для интеллектуалов')
        btn5 = types.KeyboardButton(f'Последние новости')
        markup.add(btn1, btn2, btn3, btn4,btn5)
        bot.send_message(message.chat.id, text=f'Посмотрим-ка, что я могу', reply_markup=markup)


    elif message.text == 'Мемы для интеллектуалов':
        img_list = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png', '11.png', '12.png']
        img_path = random.choice(img_list)
        bot.send_photo(message.chat.id, photo=open(img_path, 'rb'))

    elif message.text == 'Что почитать?':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(f'Фантастика')
        btn2 = types.KeyboardButton(f'Фэнтези')
        btn3 = types.KeyboardButton(f'Детективы и триллеры')
        btn4 = types.KeyboardButton(f'Любовные романы')
        btn5 = types.KeyboardButton(f'Приключения')
        btn6 = types.KeyboardButton(f'Проза')
        back = types.KeyboardButton(f'Вернуться в главное меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, back)
        bot.send_message(message.chat.id, text=f'Какой жанр предпочитаете?', reply_markup=markup)

    elif message.text == 'Последние новости':
        temp = parser()
        bot.send_message(message.chat.id, text=temp)

    elif message.text == 'Онлайн библиотека':
        markup1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text=f'Онлайн Библиотека "Альдебаран"', url='https://aldebaran.ru')
        markup1.add(btn1)
        bot.send_message(message.chat.id, text=f'Прошу: ', reply_markup=markup1)


    elif message.text == 'Книги на английском':
        markup1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text=f'Онлайн Библиотека "Gutenberg"', url='https://www.gutenberg.org')
        markup1.add(btn1)
        bot.send_message(message.chat.id, text=f'Прошу: ', reply_markup=markup1)

    elif message.text == 'Любовные романы':
        img = open('roman.png', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == 'Фантастика':
        img = open('фантастика.png', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == 'Фэнтези':
        img = open('фэнтези.png', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == 'Приключения':
        img = open('приключения.png', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == 'Проза':
        img = open('проза.png', 'rb')
        bot.send_photo(message.chat.id, img)

    elif message.text == 'Детективы и триллеры':
        img = open('детективы.png', 'rb')
        bot.send_photo(message.chat.id, img)


    elif message.text == 'Помощь':
        bot.send_message(message.chat.id, f'Мой создатель:')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text=f'Только будьте с ней помягче, прошу', url='https://t.me/Viki_or_Wiki')
        markup.add(button1)
        img = open('ava.jpg', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=markup)

    elif message.text == 'Привет':  # обработка текстовых сообщений
     bot.send_message(message.chat.id, f'И снова здравствуй, {message.from_user.first_name}.')

    elif message.text == 'привет':
        bot.send_message(message.chat.id, f'И снова здравствуй, {message.from_user.first_name}.')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Держи свой ID: {message.from_user.id}.')
    elif message.text == 'ID':
        bot.send_message(message.chat.id, f'Держи свой ID: {message.from_user.id}.')
    elif message.text == 'Id':
        bot.send_message(message.chat.id, f'Держи свой ID: {message.from_user.id}.')


    else:
        bot.send_message(message.chat.id, text=f'Моя твоя не понимать! Если потерялся, введи "Главное меню"')





@bot.message_handler(content_types=['photo'])    #обработка изображений
def user_photo(message):
  bot.send_message(message.chat.id, f'Not bad.')


@bot.message_handler(content_types=['audio'])    #обработка аудио
def user_audio(message):
  bot.send_message(message.chat.id, f'Позже послушаю, {message.from_user.first_name}.')


@bot.message_handler(content_types=['voice'])    #обработка голоса
def user_voice(message):
  bot.send_message(message.chat.id, f'Может твой голосок и прекрасен, {message.from_user.first_name}, но сейчас я явно не хочу его слышать.')


@bot.message_handler(content_types=['video'])    #обработка видео
def user_video(message):
  bot.send_message(message.chat.id, f'Хмм...что это тут у нас? Посмотрим-ка.')


@bot.message_handler(content_types=['sticker'])  #обработка стикера
def user_sticker(message):
  bot.send_message(message.chat.id, f'Какой милый стикер^^')


@bot.message_handler(content_types=['document'])  #обработка документа
def user_document(message):
  bot.send_message(message.chat.id, f'О, будет что изучить на вечер, спасибо.')


def parser(): #back_post_id):
    url = 'https://readrate.com/rus/news'

    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    post = soup.find('div', class_='container news-post')
    # post_id = post['id']

    # if post_id != back_post_id:
    title = post.find('a', class_='title-link d-block my-sm-2').text.strip()
    describe = post.find('div', class_='subtitle d-none d-sm-block').text.strip()
    img = post.find('r', class_="image-link", url="	https://readrate.com/img/pictures/basic/260/260360/2603605/w240h180-crop-stretch-9c7ef3c7.jpg"  )
    url = post.find('a', class_='title-link d-block my-sm-2', href=True)['href'].strip()

    return f'{title}\n\n{describe}\n\n{url}\n\n{img}'

    # else:
    #     return None, post_id


bot.polling(none_stop=True)
