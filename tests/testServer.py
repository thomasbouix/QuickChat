#!/usr/bin/python3

import unittest, os, sys, unittest
sys.path[:0] = ['../']
import QuickChat_server, QuickChat_client, QuickChat_bdd, sqlite3
from datetime import *

class testServer(unittest.TestCase):

    db_path = 'test_quick_chat.db'

    def test_reception_historique(self):
 
        date = datetime.now()
        QuickChat_bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)

        cursor = connect.cursor()
        cursor.execute('INSERT INTO User (username, password) VALUES ("player1","pass")')
        cursor.execute('INSERT INTO Room (name, password, private, size) VALUES ("room1","pass","False",10)')
        cursor.execute('INSERT INTO Message (userId, roomId, mess, sendDate) VALUES (1,1,"Mon premier message","{}")'.format(date))
        connect.commit()

        res = QuickChat_server.getHistorique("room1")
        self.assertTrue(res == '["{player1} - {} : {Mon premier message}", ...]'.format(date))

if __name__ == '__main__':
    unittest.main()
