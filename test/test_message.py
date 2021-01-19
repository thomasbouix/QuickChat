import unittest, sqlite3, random, string
from QuickChat_bdd import CreateDb
from QuickChat_message import addMessage


db_path = 'quick_chat.db'


conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
c = conn.cursor()


class QuickToolsTester(unittest.TestCase):
	def test1_addMessage(self):
		addMessage(db_path,0,0,'faux')  # add a correct messqge
		sql = "select mess from Message where mess = 'faux';"
		mess = ''
		for row in c.execute(sql):
			mess = row[0]
		self.assertEqual(mess,'faux')


if __name__ == '__main__':
	unittest.main()
	conn.commit()
	conn.close()
