import unittest
import sqlite3
from quick_tools import createDb
import random
import string

class QuickToolsTester(unittest.TestCase):

	def test_verif_creation_tables(self):
		random_len = random.randint(1,20)
		test_nom = ''.join(random.choice(string.ascii_letters) for i in range(random_len))
		self.assertFalse(verif_creation_tables(test_nom))
		self.assertTrue(verif_creation_tables('Room'))
		self.assertTrue(verif_creation_tables('Message'))
		self.assertTrue(verif_creation_tables('User'))
