#!/usr/bin/python3

import unittest, sys, sqlite3, os
from datetime import *
sys.path[:0] = ['../']
import QuickChat_bdd, QuickChat_server

class testBDD(unittest.TestCase):

    def setUp(self):
        # Création de BDD
        print("set-up")
        self.db_path = 'quick_chat.db'
        self.connect = sqlite3.connect(self.db_path)
        self.cursor = self.connect.cursor()

    def test_createDb(self):
        print("createDB")
        QuickChat_bdd.createDb(self.db_path)
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        print(self.cursor.execute(sql).fetchall())
        self.assertEqual(self.cursor.execute(sql).fetchall(), [('Room',), ('User',), ('Message',)])

    def test_deleteDb(self):
        print("deleteDB")
        QuickChat_bdd.deleteDb(self.db_path)
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        #print(self.cursor.execute(sql).fetchall())
        self.assertEqual(self.cursor.execute(sql).fetchall(), [])

    def test_getMessagesByRoomId(self):
        os.system('rm quick_chat.db')
        roomId = 1
        self.db_path = 'quick_chat.db'
        self.connect = sqlite3.connect(self.db_path)
        self.cursor = self.connect.cursor()
        QuickChat_bdd.createDb(self.db_path)
        sql = 'INSERT INTO Room (name, password, private, size) VALUES ("room1","pass","False",10)'
        self.cursor.execute(sql)
        sql = 'INSERT INTO Message (userId, roomId, mess, sendDate) VALUES (1,1,"Mon premier message","{}")'.format(datetime.now())
        self.cursor.execute(sql)
        self.connect.commit()

        sql = 'SELECT * FROM Message WHERE roomId="1"'.format(roomId)
        
        res = QuickChat_bdd.getMessagesByRoomId(roomId)
        # print(string)
        self.assertEqual(self.cursor.execute(sql).fetchall(), res)


if __name__ == '__main__':
#    unittest.main()
    obj = testBDD()
#   obj.setUp()
#   obj.test_deleteDb()
#   obj.test_createDb()
    obj.test_getMessagesByRoomId()
