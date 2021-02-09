
"""
    QuickChat_server : Gestion de l'historique d'une room
"""

import sqlite3
from datetime import datetime
from QuickChat_bdd import *
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
# for socketio
import eventlet

# Nom de la BDD
db_path = 'quick_chat.db'

app = Flask(__name__)
app.config['TESTING'] = True
socketio = SocketIO(app, async_mode='eventlet')

@socketio.on('connexion')
def connexion(data):
    conn = sqlite3.connect('quick_chat.db')
    c = conn.cursor()

    #On recupere les données du message envoyé
    usr = data['username']
    room = data['room']
    join_room(room)

    # print("User : {}, Room : {}".format(usr, room))

    #On recupere l'id de la room choisie
    id_room = getRoomId(db_path, room)
    
    if id_room is not None:
        #TODO : Quand room_id sera ajouté dans la table username,le rajouter
        #dans la requête

        #On insere l'user dans la base de données
        addUser(db_path, usr, "1*EISE5A")

        #On envoie l'historique à l'utilisateur


        #On envoie un message à tous les utilisateurs pour les prevenir
        msg_usr = "Utilisateur \033[94m{}\033[0m vient d'entrer dans la \033[94mroom {}\033[0m".format(usr, room)
        socketio.emit('message', msg_usr, room=room)
    else:
        print('Erreur, aucune room correspondante.')

    conn.close()

import time
@socketio.on('message_user')
# @socketio.event
def message(data):
    conn = sqlite3.connect('quick_chat.db')
    c = conn.cursor()

    #On recupere les données du message envoyé
    usr = data['username']
    message = data['message']

    #on recupere l'id de l'user
    #TODO : A remplacer après ajout de getUserId
    req = "SELECT id from User where username=\"{}\";".format(usr)
    user_id = c.execute(req).fetchall()[0][0]

    #On recupere l'id de la room
    room_id = getRoomId(db_path, "room_test")

    #Ajout du message à la BDD
    addMessage(db_path, user_id, room_id, message)

    #On recupère le temps actuel pour l'afficher à côté du message
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    message = "{} - {} : {}".format(usr, current_time, message)

    #on recupere le sid
    # sid = request.namespace.socket.sessid

    socketio.emit('message', message, room="room_test")

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
    eventlet.monkey_patch()
    main()
