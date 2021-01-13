#!/usr/bin/python3

import unittest, sys, sqlite3
sys.path[:0] = ['../']
import QuickChat_bdd

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

    def test_getMessageByRoom(self):
        pass
        QuickChat.getMessageByRoomId()

if __name__ == '__main__':
#    unittest.main()
    obj = testBDD()
    obj.setUp()
#   obj.test_deleteDb()
#   obj.test_createDb()
    obj.test_getMessageByRoomId()
