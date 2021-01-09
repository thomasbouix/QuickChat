import unittest
import sqlite3
from quick_tools import verifCreationTables
from quick_tools import createDb
import random
import string

class QuickToolsTester(unittest.TestCase):

	# def testVerifCreationTables(self):
	#
	# 	random_len = random.randint(1,20)
	# 	test_nom = ''.join(random.choice(string.ascii_letters) for i in range(random_len))
	# 	self.assertFalse(verifCreationTables(test_nom))
	#
	# 	self.assertTrue(verifCreationTables('Room'))
	# 	self.assertTrue(verifCreationTables('Message'))
	# 	self.assertTrue(verifCreationTables('User'))

	def testCreateDb(self):
		createDb("quick_chat.db")
		connect = sqlite3.connect("quick_chat.db")
		cursor = connect.cursor()
		sql = "SELECT name FROM sqlite_master WHERE type='table';"
		print(cursor.execute(sql).fetchall())
		self.assertEqual(cursor.execute(sql).fetchall(), [('Room',), ('User',), ('Message',)])

if __name__ == '__main__':
    unittest.main()
