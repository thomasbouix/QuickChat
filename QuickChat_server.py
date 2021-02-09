import sqlite3

from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

# for socketio
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['TESTING'] = True
socketio = SocketIO(app, async_mode='eventlet')

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

def main():
    socketio.run(app)

if __name__ == '__main__':
    main()
