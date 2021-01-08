import unittest
import sqlite3
from quick_tools import verifCreationTables
import random
import string

class QuickToolsTester(unittest.TestCase):

	def test_verifCreationTables(self):
		
		random_len = random.randint(1,20)
		test_nom = ''.join(random.choice(string.ascii_letters) for i in range(random_len))
		self.assertFalse(verifCreationTables(test_nom))

		self.assertTrue(verifCreationTables('Room'))
		self.assertTrue(verifCreationTables('Message'))
		self.assertTrue(verifCreationTables('User'))


if __name__ == '__main__':
    unittest.main()
