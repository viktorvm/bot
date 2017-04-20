#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config

from SQLighter import SQLighter

db_worker = SQLighter(config.database_name)
db_entries = db_worker.select_all()

def reset_day():
    db_worker.reset_day()

reset_day()