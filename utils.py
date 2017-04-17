# -*- coding: utf-8 -*-
from telebot import types

# создаем кастомную клавиатуру для выбора шаблонной команды
def generate_markup(texts):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for t in texts:
        markup.add(t)
    return markup

def hide_markup():
    keyboard_hider = types.ReplyKeyboardRemove()
    return keyboard_hider