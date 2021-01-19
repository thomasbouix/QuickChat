import sqlite3
# from QuickChat_bdd import CreateDb

def addMessage(db_path, userId, roomId, mess):

	connect = sqlite3.connect(db_path)
	cursor = connect.cursor()
	
	sql = 'INSERT INTO Message (userId, roomId,mess) VALUES (?,?,?)'
	cursor.execute(sql,(userId,roomId,mess))
	
	connect.commit()