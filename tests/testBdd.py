import unittest, sqlite3, sys
sys.path[:0] = ['../']
import QuickChat_bdd
from QuickChat_bdd import createDb
from QuickChat_bdd import deleteDb

class test_creation_delete_bdd(unittest.TestCase):

	def setUp(self):
		#Création de BDD
		self.db_path = 'quick_chat.db'
		self.connect = sqlite3.connect(self.db_path)
		self.cursor = self.connect.cursor()

#sqlite_sequence : table interne qui gère les AUTOINCREMENT + insupprimable

	def test_createDb(self):
		createDb(self.db_path)
		sql = "SELECT name FROM sqlite_master WHERE type='table';"
		res = self.cursor.execute(sql).fetchall()
		self.assertIn(('Room',), res)
		self.assertIn(('User',), res)
		self.assertIn(('Message',), res)
		self.assertIn(('sqlite_sequence',), res)

	def test_deleteDb(self):
		deleteDb(self.db_path)
		sql = "SELECT name FROM sqlite_master WHERE type='table';"
		#print(self.cursor.execute(sql).fetchall())
		self.assertEqual(self.cursor.execute(sql).fetchall(), [('sqlite_sequence',)])

if __name__ == '__main__':
    unittest.main()
