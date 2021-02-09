import socketio
import sys
from docopt import docopt

if len(sys.argv) < 3:
    print('\033[91m***Error - Usage : Python3 test_ws_client.py [username] [room]\033[0m')
    exit(1)

username = sys.argv[1]
room = sys.argv[2]

sio = socketio.Client()
host = 'localhost'
port = 5000

# Gestion des arguments passés lors de l'éxécution du script
help = """
Usage:
    QuickChat_client.py <username> <room> [--host <name> -p <port>]

Options:
    -h --help       : Obtenir de l'aide
    --host <name>   : Choix de l'host (defaut: localhost)
    -p <port>       : Choix du port (defaut: 5000)
"""

# Affichage d'un message lorsque le client reçois un évènement de connexion du serveur
@sio.on('connect')
def connect():
	if(sio.connected):
		print('\033[32msuccessfully connected\033[39m')

# Fonction permettant une tentative de connexion au serveur
def connexion():
	sio.connect('http://{}:{}'.format(host, str(port)))
	sleep(1)
	sio.emit('join', {'username': username, 'room': room})

# Affichage d'un message en cas de perte de connexion avec le serveur
@sio.on('disconnect')
def disconnect():
	print('\033[31mdisconnected\033[39m')

def disconnection():
	sio.emit('leave', {'username': username, 'room': room})

@sio.on('message')
def handle_message(data):
	print('received message from {}: '.format(data['username']) + data['payload'])

def sendMessage(msg):
	sio.emit('message', {'username': username, 'payload': msg, 'room': room})

def SignupUser():
	password = input()
	sio.emit('Signup_user', {'username': username, 'password': password})

def SignupRoom():
	sio.emit('Signup_room', {'roomname': room, 'password': NULL, 'private': False, 'size': 20})

def main():
	arguments = docopt(help)
	if arguments['-p']:
		port = arguments['-p']
	if arguments['--host']:
		host = arguments['--host']

	connexion()

if __name__ == '__main__':
	main()
	while True :
		message = input()
		sendMessage(message)
