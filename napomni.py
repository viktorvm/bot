#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import telebot

import config
import utils

from SQLighter import SQLighter

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level = logging.DEBUG, filename = u'napomnilog.log')
logging.info(u'Napomni module started')

bot = telebot.TeleBot(config.token)

db_worker = SQLighter(config.database_name)
db_entries = db_worker.select_all()

def remind():
    for x in db_entries:
        try:
            if (x['need_remind'] and not x['done']):
                markup = utils.generate_markup(['+', 'Спроси в другой раз']) if x['reminds_today'] < 3 \
                    else utils.generate_markup(['+', 'Беру на себя всю ответственность'])

                name = ', ' + x['chat_first_name'].encode('utf-8') if x['chat_first_name'] else ''

                mes_text = 'Привет' + name + '! Отчет уже написан?' if x['reminds_today'] == 0 \
                    else 'Это снова я. Как твой отчет, готов?' if x['reminds_today'] == 1 \
                    else 'Время уже позднее, про отчет не забудь. Или уже написан?' if x['reminds_today'] == 2 \
                    else 'Не забудь про отчет. На сегодня беспокою тебя в последний раз. ' \
                         'Напиши мне + когда будет готово. Спокойной ночи)' if x['reminds_today'] == 3 \
                    else 'Отчет готов?'

                db_worker.upd_col('reminds_today', int(x['reminds_today']) + 1, x['chat_id'])
                bot.send_message(x['chat_id'], mes_text, reply_markup=markup)
        except Exception as e:
            db_worker.upd_col('errors', int(x['errors'])+1, x['chat_id'])
            logging.error(e)

    logging.info(u'Napomni module ended')

remind()