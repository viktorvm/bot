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
        bot.send_message(message.chat.id, 'Не волнуйся, я тебя не забыл. Ты у меня уже на заметке, напоминаю каждый день про отчет:)')
    else:
        markup = utils.generate_markup('Да. То, что нужно!')
        bot.send_message(message.chat.id, 'Привет! Я бот, который поможет тебе не забыть писать ежедневный отчет! Напоминать тебе об этом?', reply_markup=markup)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    db_worker = SQLighter(config.database_name)

    if message.text == u'Да. То, что нужно!':
        with db_worker.connection:
            db_worker.add_row(message.chat.id)
            bot.send_message(message.chat.id, 'Больше тебе приседать не придется:) Я буду ежедневно напоминать тебе об отчете каждый час, начиная с 20:00. До связи!',
                             reply_markup=utils.hide_markup())

    else:
        bot.send_message(message.chat.id, message.text)

def cyclic():
    print 'its me'
    sleep(3)
    cyclic()

if __name__ == '__main__':
    bot.polling(none_stop=True)
    cyclic()