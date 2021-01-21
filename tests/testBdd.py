#!/usr/bin/python3

import unittest, sys, sqlite3, os
from datetime import *
sys.path[:0] = ['../']
import QuickChat_bdd, QuickChat_server

class testBDD(unittest.TestCase):

	def setUp(self):
		#Création de BDD
		self.db_path = 'quick_chat.db'
		self.connect = sqlite3.connect(self.db_path)
		self.cursor = self.connect.cursor()

		# sqlite_sequence : table interne qui gère les AUTOINCREMENT + insupprimable
	
	def test_createDb(self):
		QuickChat_bdd.deleteDb(self.db_path)
		QuickChat_bdd.createDb(self.db_path)
		sql = "SELECT name FROM sqlite_master WHERE type='table';"
		res = self.cursor.execute(sql).fetchall()
		self.assertIn(('Room',), res)
		self.assertIn(('User',), res)
		self.assertIn(('Message',), res)
		self.assertIn(('sqlite_sequence',), res)

	def test_deleteDb(self):
		QuickChat_bdd.deleteDb(self.db_path)
		sql = "SELECT name FROM sqlite_master WHERE type='table';"
		#print(self.cursor.execute(sql).fetchall())
		self.assertEqual(self.cursor.execute(sql).fetchall(), [('sqlite_sequence',)])

	def test_Message_add(self):
		QuickChat_bdd.deleteDb(self.db_path)
		QuickChat_bdd.createDb(self.db_path)
		
		QuickChat_bdd.addMessage(self.db_path,0,0,'faux')  # add a correct messqge
		sql = "select mess from Message where mess = 'faux';"
		mess = ''
		for row in self.cursor.execute(sql):
			mess = row[0]
		self.assertEqual(mess,'faux')

	def test_getMessagesByRoomId(self):
		QuickChat_bdd.deleteDb(self.db_path)
		QuickChat_bdd.createDb(self.db_path)

		roomId = 1
		sql = 'INSERT INTO Room (name, password, private, size) VALUES ("room1","pass","False",10)'
		self.cursor.execute(sql)
		sql = 'INSERT INTO Message (userId, roomId, mess, sendDate) VALUES (1,1,"Mon premier message","{}")'.format(datetime.now())
		self.cursor.execute(sql)
		self.connect.commit()

		sql = 'SELECT * FROM Message WHERE roomId="{}"'.format(roomId)
		res = QuickChat_bdd.getMessagesByRoomId(roomId)
		# print(string)
		self.assertEqual(self.cursor.execute(sql).fetchall(), res)

	def test_getUsernameById(self):
		QuickChat_bdd.deleteDb(self.db_path)
		QuickChat_bdd.createDb(self.db_path)

		userId = 1
		sql = 'INSERT INTO User (username, password) VALUES ("player1","pass")'
		self.cursor.execute(sql)
		self.connect.commit()

		sql = 'SELECT username FROM User WHERE Id="{}";'.format(userId)

		res = QuickChat_bdd.getUsernameById(userId)
		# print(string)
		self.assertEqual(self.cursor.execute(sql).fetchall()[0][0], res)

	def test_getRoomId(self):
		QuickChat_bdd.deleteDb(self.db_path)
		QuickChat_bdd.createDb(self.db_path)

		roomName = "room1"
		sql = 'INSERT INTO Room (name, password, private, size) VALUES ("room1","pass","False",10)'
		self.cursor.execute(sql)
		self.connect.commit()

		sql = 'SELECT id FROM Room WHERE name="{}";'.format(roomName)
		res = QuickChat_bdd.getRoomId(roomName)
		# print(string)
		self.assertEqual(self.cursor.execute(sql).fetchall()[0][0], res)


if __name__ == '__main__':
	os.system('rm -f quick_chat.db')
	unittest.main()
