#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

import config

bot = telebot.TeleBot(config.token)

bot.delete_webhook()