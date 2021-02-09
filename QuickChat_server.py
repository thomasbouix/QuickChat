from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from datetime import datetime
from QuickChat_bdd import *

# for socketio
import eventlet
eventlet.monkey_patch()

# Nom de la BDD
db_path = 'quick_chat.db'

app = Flask(__name__)
app.config['TESTING'] = True
socketio = SocketIO(app, async_mode='eventlet')


def getHistorique(roomName):
    historique = []
    roomId = getRoomId(db_path, roomName)
    messages = getMessagesByRoomId(roomId)
    for message in messages:
        historique.append('{} - {} : {}'.format(message[4].split('.')[0], getUsernameById(db_path, message[1]), message[3]))

    return historique


@socketio.on('Signup_room')
def add_room(roomInfo):
	addRoom(roomInfo['roomname'], roomInfo['password'], roomInfo['private'], roomInfo['size'])


@socketio.on('Signup_user')
def add_user(data):
	addUser(db_path,data['username'],data['password']) 

@socketio.on('message')
def handle_message(data):
	username = data['username']
	payload = data['payload']
	addmessagefromclient(username,payload)
	print('received message from {}: '.format(data['username']) + data['payload'])
	# socketio.emit('message', data, broadcast=True, room=data['room'])

@socketio.on('join')
def on_join(data):
	username = data['username']
	room = data['room']
	join_room(room,username)

def join_room(room,username):
	iduser = getIDfromusername(username)
	idroom = getRoomId(db_path,room)
	if iduser == 0:
		print('\033[91mServer log\033[0m Please sign up with this username')
		# emit('message', {'username': 'server' ,'payload': '\033[94m{} is not declared.\033[0m'.format(username)}, room=room)
	elif idroom == 0:
		print('\033[91mServer log\033[0m Please sign up with this roomname')
		# emit('message', {'username': 'server' ,'payload': '\033[94m{} is not declared.\033[0m'.format(room)}, room=room)
	else:
		join_roomfromid(iduser,idroom)
		print('\033[91mServer log\033[0m {} has joined {}'.format(username, room))
		# emit('message', {'username': 'server' ,'payload': '\033[94m{} has entered the room.\033[0m'.format(username)}, room=room)

@socketio.on('leave')
def on_leave(data):
	username = data['username']
	room = data['room']
	leave_room(room,username)
	print('\033[91mServer log\033[0m {} has left {}'.format(data['username'], data['room']))
	# emit('message', {'username': 'server', 'payload': '\033[94m{} has left the room.\033[0m'}.format(username), room=room)

def main():
    socketio.run(app)
    pass

if __name__ == '__main__':
    main()
