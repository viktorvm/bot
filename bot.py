#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from time import sleep

import telebot

import config
import utils
from SQLighter import SQLighter

bot = telebot.TeleBot(config.token)

# Обработка команды старт
@bot.message_handler(commands=['start'])
def start(message):
    db_worker = SQLighter(config.database_name)
    if db_worker.select_single(message.chat.id):
        markup = utils.generate_markup(['Забудь про меня'])
        bot.send_message(message.chat.id, 'Не волнуйся, я тебя не забыл. Ты у меня уже на заметке, '
                                          'напоминаю каждый день про отчет:)', reply_markup=markup)
    else:
        markup = utils.generate_markup(['Да. То, что нужно!'])
        bot.send_message(message.chat.id, 'Привет! Я бот, который поможет тебе не забыть писать ежедневный отчет! '
                                          'Напоминать тебе об этом?', reply_markup=markup)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def message_handle(message):
    db_worker = SQLighter(config.database_name)

    #убрать после того, как имена всех существующих обновятся
    x = db_worker.select_single(message.chat.id)
    if x:
        username = '"' + message.chat.username.encode('utf-8') + '"' if message.chat.username else 'null'
        if username:
            db_worker.upd_col('chat_username', username, message.chat.id)
        first_name = '"' + message.chat.first_name.encode('utf-8') + '"' if message.chat.first_name else 'null'
        if first_name:
            db_worker.upd_col('chat_first_name', first_name, message.chat.id)
    #---------------------------------------------------------

    if message.text == u'Да. То, что нужно!':
        username = '"' + message.chat.username.encode('utf-8') + '"' if message.chat.username else 'null'
        first_name = '"' + message.chat.first_name.encode('utf-8') + '"' if message.chat.first_name else 'null'
        db_worker.add_row(message.chat.id, username, first_name)
        bot.send_message(message.chat.id, 'Больше тебе приседать не придется:) Я буду ежедневно напоминать тебе '
                                          'об отчете каждый час, начиная с 20:00. '
                                          'До связи!', reply_markup=utils.hide_markup())
    elif message.text == u'+':
        db_worker.upd_col('done', 1, message.chat.id)
        bot.send_message(message.chat.id, 'Отлично! встретимся завтра:)')
    elif message.text == u'Спроси в другой раз':
        bot.send_message(message.chat.id, 'Окей, напомню через час.')
    elif message.text == u'Забудь про меня':
        db_worker.delete_row(message.chat.id)
        bot.send_message(message.chat.id, 'Хорошо, больше не буду тебе надоедать. '
                                          'Если передумаешь подай команду /start')
    elif message.text == u'Беру на себя всю ответственность':
        bot.send_message(message.chat.id, 'Смотри, так до приседаний недалеко))')
    else:
        bot.send_message(message.chat.id, 'Извини, такой команды я не знаю. '
                                          'Я пока примитивный глуповатый бот:( Но я учусь')

def cyclic():
    print 'its me'
    sleep(3)
    cyclic()

if __name__ == '__main__':
    bot.polling(none_stop=True)