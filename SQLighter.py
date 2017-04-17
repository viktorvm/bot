# -*- coding: utf-8 -*-
import sqlite3

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add_row(self, chat_id):
        with self.connection:
            return self.cursor.execute('INSERT INTO botMemory(chat_id, done) VALUES(' + str(chat_id) + ', 0)')

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM botMemory').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM botMemory WHERE chat_id = ?', (rownum,)).fetchall()

    def upd_col(self, col, val, id):
        with self.connection:
            return self.cursor.execute('UPDATE botMemory SET ' + str(col) + ' = ' + str(val) + ' WHERE chat_id = ' + str(id))

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM botMemory').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()