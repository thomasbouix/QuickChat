import unittest, sqlite3, random, string
from quick_tools import createDb, addUser,verifyUserPassword,addMessage


db_path = 'quick_chat.db'


conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
c = conn.cursor()


class QuickToolsTester(unittest.TestCase):

	def test1_verifyUserPassword(self):

		self.assertFalse(verifyUserPassword('qwer')) # not long enough
		self.assertFalse(verifyUserPassword('qwer123456')) # no special character

		random_str_len = random.randint(5,10)
		
		correct_password = ''.join(random.choice(string.ascii_lowercase) for i in range(random_str_len))
		correct_password += '123456,'

		self.assertTrue(verifyUserPassword(correct_password))

	def test2_addUser(self):

		c.execute('DROP TABLE IF EXISTS Room;')
		c.execute('DROP TABLE IF EXISTS User;')
		c.execute('DROP TABLE IF EXISTS Message;')
		createDb(db_path)

		addUser(db_path,'yann.c','qwer123456,')  # add a correct user
		sql = "select username from User where username = 'yann.c';"
		user_name = ''
		for row in c.execute(sql):
			user_name = row[0]
		self.assertEqual(user_name,'yann.c')

		addUser(db_path,'huiling.b','pass')  # add a user with wrong password format
		sql = "select username from User where username = 'huiling.b';"
		name = ''
		for row in c.execute(sql):
			name = row[0]
		self.assertEqual(name,'')
		
	def test3_addMessage(self):
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

