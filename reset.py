#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import config

from SQLighter import SQLighter

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level = logging.DEBUG, filename = config.resetlog_name)
logging.info(u'Reset module started')

def reset_day():
    try:
        db_worker = SQLighter(config.database_name)
        db_worker.reset_day()
    except Exception as e:
        logging.error(e)

    logging.info(u'Reset module ended')

reset_day()