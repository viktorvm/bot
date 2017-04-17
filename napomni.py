#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import telebot

import config
import utils

from time import sleep
from SQLighter import SQLighter


bot = telebot.TeleBot(config.token)

db_worker = SQLighter(config.database_name)
db_entries = db_worker.select_all()

now = datetime.datetime.now()

time8pm = now.replace(hour=20, minute=0, second=0, microsecond=0)
checked8pm = False

time9pm = now.replace(hour=21, minute=0, second=0, microsecond=0)
checked9pm = False

time10pm = now.replace(hour=22, minute=0, second=0, microsecond=0)
checked10pm = False

time11pm = now.replace(hour=22, minute=0, second=0, microsecond=0)
checked11pm = False

def cyclicCheck():
    now = datetime.datetime.now()
    global checked8pm
    global checked9pm
    global checked10pm
    global checked11pm

    markup = utils.generate_markup(['+', 'Спроси в другой раз'])

    if (now > now.replace(hour=23, minute=59, second=50, microsecond=0) and now < now.replace(hour=23, minute=59, second=54, microsecond=0)):
        checked8pm = False
        checked9pm = False
        checked10pm = False
        checked11pm = False
        for x in db_entries:
            db_worker.upd_col('done', 0, x[1])

    if now > time8pm and not checked8pm:
        for x in db_entries:
            print x
            if (not x[2]):
                bot.send_message(x[1], 'Отчет готов?',
                                 reply_markup=markup)
        checked8pm = True
    if now > time9pm and not checked9pm:
        for x in db_entries:
            print x
            if (not x[2]):
                bot.send_message(x[1], 'Отчет готов?',
                                 reply_markup=markup)
        checked9pm = True
    if now > time10pm and not checked10pm:
        for x in db_entries:
            print x
            if (not x[2]):
                bot.send_message(x[1], 'Отчет готов?',
                                 reply_markup=markup)
        checked10pm = True
    if now > time11pm and not checked11pm:
        for x in db_entries:
            print x
            if (not x[2]):
                bot.send_message(x[1], 'Отчет готов?',
                                 reply_markup=markup)
        checked11pm = True
    sleep(5)
    cyclicCheck()

cyclicCheck()