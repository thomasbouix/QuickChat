from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

# for socketio
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config['TESTING'] = True
socketio = SocketIO(app, async_mode='eventlet')

def main():
    socketio.run(app)

if __name__ == '__main__':
    main()
