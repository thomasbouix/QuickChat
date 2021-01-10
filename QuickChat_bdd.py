import sqlite3

def createDb(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	cursor.execute('CREATE TABLE Room ([id] INTEGER PRIMARY KEY AUTOINCREMENT,[name] TEXT UNIQUE NOT NULL, [password] TEXT NOT NULL, [private] BOOLEAN NOT NULL, [size] INTEGER NOT NULL)')
	cursor.execute('CREATE TABLE User ([id] INTEGER PRIMARY KEY AUTOINCREMENT,[username] TEXT UNIQUE NOT NULL, [password] TEXT NOT NULL)')
	cursor.execute('CREATE TABLE Message ([id] INTEGER PRIMARY KEY AUTOINCREMENT,[userId] INTEGER NOT NULL, [roomId] INTEGER NOT NULL, [mess] TEXT NOT NULL, [sendDate] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(userId) REFERENCES User(id), FOREIGN KEY(roomId) REFERENCES Room(id))')

	connect.commit()

def deleteDb(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	cursor.execute('DROP TABLE IF EXISTS Room')
	cursor.execute('DROP TABLE IF EXISTS User')
	cursor.execute('DROP TABLE IF EXISTS Message')

	connect.commit()

# Db creation :
db_path = 'quick_chat.db'

#createDb(db_path)