# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def add_row(self, chat_id, chat_username, chat_first_name):
        with self.connection:
            return self.cursor.execute('INSERT INTO botMemory(chat_id, chat_username, chat_first_name, need_remind,'
                                       'done, reminds_today, errors) VALUES(' + str(chat_id) + ', ' + chat_username +
                                       ', ' + chat_first_name + ', 1, 0, 0, 0)')

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM botMemory').fetchall()

    def select_single(self, chat_id):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM botMemory WHERE chat_id = ?', (chat_id,)).fetchall()

    def upd_col(self, col, val, chat_id):
        with self.connection:
            return self.cursor.execute('UPDATE botMemory SET ' + str(col) + ' = ' + str(val) + ' WHERE chat_id = ' + str(chat_id))

    def delete_row(self, chat_id):
        with self.connection:
            return self.cursor.execute('DELETE from botMemory WHERE chat_id = ' + str(chat_id))

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM botMemory').fetchall()
            return len(result)

    def reset_day(self):
        with self.connection:
            return self.cursor.execute('UPDATE botMemory SET done = 0, reminds_today = 0 WHERE id > 0')

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()