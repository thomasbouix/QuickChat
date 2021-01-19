import sqlite3, os

def createDb(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	cursor.execute('CREATE TABLE Room ([id] INTEGER PRIMARY KEY AUTOINCREMENT,[name] TEXT UNIQUE NOT NULL, [password] TEXT NOT NULL, [private] BOOLEAN NOT NULL, [size] INTEGER NOT NULL)')
	cursor.execute('CREATE TABLE User ([id] INTEGER PRIMARY KEY AUTOINCREMENT,[username] TEXT UNIQUE NOT NULL, [password] TEXT NOT NULL)')
	cursor.execute('CREATE TABLE Message ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [userId] INTEGER NOT NULL, [roomId] INTEGER NOT NULL, [mess] TEXT NOT NULL, [sendDate] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(userId) REFERENCES User(id), FOREIGN KEY(roomId) REFERENCES Room(id))')

	connect.commit()

def deleteDb(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	cursor.execute('DROP TABLE IF EXISTS Room')
	cursor.execute('DROP TABLE IF EXISTS User')
	cursor.execute('DROP TABLE IF EXISTS Message')

	connect.commit()


def resetDb(db_path) :
	if (os.path.exists(db_path) == False) : 
		createDb(db_path)
	else :
		deleteDb(db_path)
		createDb(db_path)


def getMessagesByRoomId(db_path, roomId):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT * FROM Message WHERE roomId="{}"'.format(roomId)
	messageList = cursor.execute(sql).fetchall()

	return messageList
	

def getUsernameById(db_path, userId):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT username FROM User WHERE id = {}'.format(userId)
	username = cursor.execute(sql).fetchone()[0]

	return username


def getRoomId(db_path, roomName):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	sql = 'SELECT id FROM Room WHERE name="{}";'.format(roomName)
	roomId = cursor.execute(sql).fetchone()[0]

	return roomId
