import sqlite3, os

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

def resetDb(db_path) :
	if (os.path.exists(db_path) == False) : 
		createDb(db_path)
	else :
		deleteDb(db_path)
		createDb(db_path)

def getMessagesByRoomId(roomId):
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

def addMessage(db_path, userId, roomId, mess):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	
	sql = 'INSERT INTO Message (userId, roomId,mess) VALUES (?,?,?)'
	cursor.execute(sql,(userId,roomId,mess))
	connect.commit()
	
def verifyUserName(user_name):
  	# Extra requirement: user_name has to be unique and cannot have number or special character
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	has_number = False
	has_special_character = False

	for c in user_name:
		if c.isdigit():
			has_number = True
		if (not c.islower()) and (not c.isupper())  and (not c.isdigit()):
			has_special_character = True

	if (not has_number) and (not has_special_character):
		sql = 'SELECT user_name FROM Users;'
		user_names = cursor.execute(sql).fetchall()
		
		if user_name not in [name[0] for name in user_names]:
			return True

	return False

def verifyUserPassword(user_password):
	# Extra requirement: check the password have number,special character, length>8 
	is_number = 0
	special_character = 0

	for i in user_password:
		if i.isdigit():
			is_number = 1

		if (not i.islower()) and (not i.isupper())  and (not i.isdigit()):
			special_character = 1

	if len(user_password)>=8:
		if is_number and special_character:
			return True
		
	return False

def addUser(db_path, username, password):

	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	
	
	if verifyUserPassword(password):
		sql = 'INSERT INTO User (username, password) VALUES (?,?)'
		cursor.execute(sql,(username, password))

	connect.commit()
	

# Db creation :
db_path = 'quick_chat.db'

#createDb(db_path)
