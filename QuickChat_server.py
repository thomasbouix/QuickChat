from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
from datetime import datetime
from QuickChat_bdd import *

# for socketio
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['TESTING'] = True
socketio = SocketIO(app, async_mode='eventlet')


def getHistorique(roomName):
    historique = []
    roomId = getRoomId(roomName)
    messages = getMessagesByRoomId(roomId)
    for message in messages:
        historique.append('{} - {} : {}'.format(message[4].split('.')[0], getUsernameById(message[1]), message[3]))

    return historique


def main():
    socketio.run(app)

if __name__ == '__main__':
    main()
