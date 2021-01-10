import sqlite3

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

	else:
		print("\nUsers ERROR: password should > 8 chars, includes numbers and special character")
	
	connect.commit()

def addMessage(db_path, userId, roomId, mess):

	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	
	sql = 'INSERT INTO Message (userId, roomId,mess) VALUES (?,?,?)'
	cursor.execute(sql,(userId,roomId,mess))
	
	connect.commit()



def createDb(db_path):
	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()

	cursor.execute('CREATE TABLE Room ([id] INTEGER PRIMARY KEY,[name] TEXT UNIQUE, [password] TEXT NOT NULL, [private] BOOLEAN, [size] INTEGER)')
	cursor.execute('CREATE TABLE User ([id] INTEGER PRIMARY KEY,[username] TEXT UNIQUE, [password] TEXT NOT NULL)')
	cursor.execute('CREATE TABLE Message ([id] INTEGER PRIMARY KEY,[userId] INTEGER NOT NULL, [roomId] INTEGER NOT NULL, [mess] TEXT NOT NULL, [sendDate] TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(userId) REFERENCES User(id), FOREIGN KEY(roomId) REFERENCES Room(id))')
	
	connect.commit()


# Db creation :
# db_path = 'quick_chat.db' 