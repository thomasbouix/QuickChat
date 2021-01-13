#!/usr/bin/python3

import unittest, sys, sqlite3, os
from datetime import *
sys.path[:0] = ['../']
import QuickChat_bdd, QuickChat_server

class testBDD(unittest.TestCase):

    def setUp(self):
        # Création de BDD
        print("set-up")
        os.system('rm -f quick_chat.db')
        self.db_path = 'quick_chat.db'
        self.connect = sqlite3.connect(self.db_path)
        self.cursor = self.connect.cursor()

    def test_createDb(self):
        print("createDB")
        QuickChat_bdd.createDb(self.db_path)
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        # print(self.cursor.execute(sql).fetchall())
        # self.assertEqual(self.cursor.execute(sql).fetchall(), [('Room',), ('User',), ('Message',)])

    def test_deleteDb(self):
        print("deleteDB")
        QuickChat_bdd.deleteDb(self.db_path)
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        # print(self.cursor.execute(sql).fetchall())
        # self.assertEqual(self.cursor.execute(sql).fetchall(), [])

    def test_getMessagesByRoomId(self):
        QuickChat_bdd.deleteDb(self.db_path)
        QuickChat_bdd.createDb(self.db_path)

        roomId = 1
        sql = 'INSERT INTO Room (name, password, private, size) VALUES ("room1","pass","False",10)'
        self.cursor.execute(sql)
        sql = 'INSERT INTO Message (userId, roomId, mess, sendDate) VALUES (1,1,"Mon premier message","{}")'.format(datetime.now())
        self.cursor.execute(sql)
        self.connect.commit()

        sql = 'SELECT * FROM Message WHERE roomId="1"'.format(roomId)
        res = QuickChat_bdd.getMessagesByRoomId(roomId)
        # print(string)
        self.assertEqual(self.cursor.execute(sql).fetchall(), res)

    def test_getUsernameById(self):
        pass

    def test_RoomId(self):
        pass

if __name__ == '__main__':
    unittest.main()
