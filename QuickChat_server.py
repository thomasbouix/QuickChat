from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

# for socketio
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['TESTING'] = True
socketio = SocketIO(app, async_mode='eventlet')

@socketio.on('connexion')
def connexion(data):
    pass

@socketio.on('message')
def message(data):
    print(data)
    # #on ouvre la base de donnees
    # self.c = None
    # self.req = None
    # self.conn = sqlite3.connect(name)
    # self.c = self.conn.cursor()
    #
    # #on recupere les donnees
    # usr = data['username'] #on extrait le nom de l'utilisateur
    # msg = data['message'] #on extrait le message
    #
    # #on recupere l'id de l'user
    # req = "select id from User where username=%s" %(usr)
    # usr_table = self.c.execute(req).fetchall()
    # user_id = usr_table['id']
    #
    # #on recupere le sid
    # sid = request.namespace.socket.sessid
    #
    # #on ajoute le message a la base de donnees
    # fields = "userID, text"
    # values = "%d, %s" %(user_id, msg)
    # sql = "insert into %s (%s) values (%s)" %('Message', fields, values)
    # cur.execute(sql)
    # conn.commit()
    # self.conn.close()
    # emit("broadcast message",  {"message": msg}, broadcast=True, room=rooms(sid))

def main():
    socketio.run(app)

if __name__ == '__main__':
    main()
