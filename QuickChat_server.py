"""
    QuickChat_server : Gestion de l'historique d'une room
"""

from datetime import datetime
from QuickChat_bdd import *
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
# for socketio
import eventlet
eventlet.monkey_patch()

# Nom de la BDD
db_path = 'quick_chat.db'

app = Flask(__name__)
app.config['TESTING'] = True
socketio = SocketIO(app, async_mode='eventlet')


def getHistorique(roomName):
    """ Fonction permettant de recupérer l'historique d'une Room """
    historique = []
    roomId = getRoomId(db_path, roomName)
    messages = getMessagesByRoomId(roomId)
    for message in messages:
        historique.append('{} - {} : {}'.format(message[4].split('.')[0], getUsernameById(db_path, message[1]), message[3]))

    return historique


def main():
    """ MAIN """
    socketio.run(app)

if __name__ == '__main__':
    main()
