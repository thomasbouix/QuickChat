import sqlite3
# TODO: Import other files

def createTableRoom():
	conn = sqlite3.connect('quick_chat.db')
	c = conn.cursor()

	# Create the table Room
	req = '''CREATE TABLE Room(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		password TEXT NOT NULL,
		private BOOLEAN NOT NULL,
		size INTEGER NOT NULL 
	);'''
	c.execute(req)
	conn.commit()


# private = 1: private, private = 0: public
def addRoom(name, password, private, size):
	conn = sqlite3.connect('quick_chat.db')
	c = conn.cursor()

	# Insert a new room in table
	req = '''INSERT INTO Room (name, password, private, size) VALUES ("%s", "%s", %d, %d);''' % (name, password, private, size)
	c.execute(req)
	conn.commit()

