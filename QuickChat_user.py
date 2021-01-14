import sqlite3
# from QuickChat_bdd import CreateDb


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