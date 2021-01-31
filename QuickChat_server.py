from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room
import json
import sqlite3

# for socketio
import eventlet

app = Flask(__name__)
app.config['TESTING'] = True
socketio = SocketIO(app, async_mode='eventlet')

@socketio.on('connexion')
def connexion(data):
    conn = sqlite3.connect('test_donnees.db')
    c = conn.cursor()

    #On recupere les données du message envoyé
    donnees = json.loads(data)
    usr = donnees['username']
    room = donnees['room']

    print("User : {}, Room : {}".format(usr, room))

    #On recupere l'id de la room choisie
    req = "SELECT id FROM ROOM WHERE name=\"{}\";".format(room)
    print(req)
    id_room = c.execute(req).fetchall()
    conn.commit()

    print(id_room)
    id_room = id_room[0]
    if id_room is not None:
        #TODO : Quand room_id sera ajouté dans la table username,le rajouter
        #dans la requête

        #On insere l'user dans la base de données
        req = "INSERT INTO USER(username, password) VALUES (\"{}\", \"\");".format(usr)
        c.execute(req)
        conn.commit()

        #On envoie un message à tous les utilisateurs pour les prevenir
        msg_usr = "Utilisateur {} vient d'entrer dans la room {}".format(usr, room)
        socketio.emit(msg_usr)
    else:
        print('Erreur, aucune room correspondante.')

    conn.close()

import time
@socketio.on('message_user')
# @socketio.event
def message(data):
    conn = sqlite3.connect('test_donnees.db')
    c = conn.cursor()

    #On recupere les données du message envoyé
    donnees = json.loads(data)
    usr = donnees['username']
    message = donnees['message']

    #on recupere l'id de l'user
    req = "SELECT id from User where username=\"{}\";".format(usr)
    user_id = c.execute(req).fetchall()[0][0]


    #on ajoute le message a la base de donnees
    print("User_id :")
    print(user_id)
    values = "{}, 1, \"{}\"".format(user_id, message)
    req = "INSERT INTO MESSAGE (userId, roomId, mess) VALUES ({});".format(values)
    c.execute(req)
    conn.commit()
    conn.close()

    #On recupère le temps actuel pour l'afficher à côté du message
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    message = "{} à {} => {}".format(usr, current_time, message)

    #on recupere le sid
    # sid = request.namespace.socket.sessid

    socketio.emit(message)

def main():
    socketio.run(app)

if __name__ == '__main__':
    eventlet.monkey_patch()
    main()
