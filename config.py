# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

token = '302262847:AAEgKj9TuBHsbeDfFfcScq_DEQGkGtDLIfU'

database_name = os.path.join(BASE_DIR, 'pomnibot.db') # Файл с базой данных
botlog_name = os.path.join(BASE_DIR, 'bot.log') # Файл с логом работы основного обработчика команд
resetlog_name = os.path.join(BASE_DIR, 'reset.log') # Файл с логом ежедневного сброса
napomnilog_name = os.path.join(BASE_DIR, 'napomni.log') # Файл с логом напоминаний