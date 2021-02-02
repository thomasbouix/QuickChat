#!/usr/bin/python3

import unittest, os, sys, unittest
sys.path[:0] = ['../']
import QuickChat_server, QuickChat_client, QuickChat_bdd, sqlite3
from datetime import *

class testServer(unittest.TestCase):

    db_path = 'quick_chat.db'

    def test_reception_historique(self): 
        date = datetime.now()
        QuickChat_bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)

        cursor = connect.cursor()
        cursor.execute('INSERT INTO User (username, password) VALUES ("user1","pass")')
        cursor.execute('INSERT INTO Room (name, password, private, size) VALUES ("room1","pass","False",10)')
        cursor.execute('INSERT INTO Message (userId, roomId, mess, sendDate) VALUES (1,1,"Mon premier message","{}")'.format(date))
        connect.commit()

        res = QuickChat_server.getHistorique("room1")
        self.assertTrue( res == ['{} - user1 : Mon premier message'.format(str(date).split('.')[0])])

    def test_create_room_user(self):
    	connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
    	cursor.execute('DROP TABLE IF EXISTS RoomUser;')

		QuickChat_server.create_room_user(self.db_path)
		sql = "SELECT name FROM sqlite_master WHERE type='table';"
		res = cursor.execute(sql).fetchall()
		self.assertIn(('RoomUser',), res)
        connect.commit()


    def test_delete_room_user(self):
    	connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
    	cursor.execute('DROP TABLE IF EXISTS RoomUser;')
    	cursor.execute('CREATE TABLE RoomUser ([idroom] INTEGER NOT NULL, [iduser] INTEGER NOT NULL);')

		QuickChat_server.delete_room_user(self.db_path)
		sql = "SELECT name FROM sqlite_master WHERE type='table';"
		res = cursor.execute(sql).fetchall()
		self.assertNotIn(('RoomUser',), res)
        connect.commit()

    def test_add_message(self):
    	QuickChat_bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()

        QuickChat_server.add_message("user1","message1")

        sql = 'SELECT userId FROM Message WHERE mess = "message1";'
        userId = cursor.execute(sql).fetchall()[0][0]
        username = QuickChat_bdd.getUsernameById(userId)
		self.assertEqual(username, "user1")
        connect.commit()

    def test_add_user(self):
    	QuickChat_bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()

        QuickChat_server.add_user("user1")
        sql = 'SELECT * FROM User;'

		self.assertEqual(cursor.execute(sql).fetchall()[0][0], "user1")
        connect.commit()

    def test_add_room(self):
    	pass

    def verifier_existence(self):
    	pass

    def join_room(self):
    	pass

    def leave_room(self):
    	pass



if __name__ == '__main__':
    unittest.main()
