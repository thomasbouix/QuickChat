import socketio
from docopt import docopt
import sys

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


# Affichage d'un message lorsque le client reçoit un évènement de connexion du serveur
@sio.on('connect')
def connect():
    if(sio.connected):
        print('\033[32msuccessfully connected\033[39m')
        arg = sys.argv[1:]
        data = listArg(arg)
        sio.emit('connexion', data)
        sio.sleep(1)
        while(1):
            mess = writeMessage(data)
            sio.emit('message_user', mess)

# Affichage d'un message en cas de perte de connexion avec le serveur
@sio.on('disconnect')
def disconnect():
    print('\033[31mdisconnected\033[39m')

# Fonction permettant une tentative de connexion au serveur
def connexion():
    sio.connect('http://{}:{}'.format(host, str(port)))

#Fonction permettant de se deconnecter
def deconnexion():
    sio.disconnect()

# Fonction pour écrire un message
def writeMessage(data):
    data['message'] = input()
    screen_code = "\033[1A[\033[2K"
    sys.stdout.write( screen_code )
    return data

# Vérification du nombre d'arguments
def verifArg(nbArg):
    if (nbArg == 2 or nbArg == 4):
        return True
    return False

# Stocke dans data: username et room
def listArg(arg):
    data = {}
    data['username'] = arg[0]
    data['room'] = arg[1]
    return data

def main():
    arguments = docopt(help)
    if arguments['-p']:
        port = arguments['-p']
    if arguments['--host']:
        host = arguments['--host']
    connexion()

if __name__ == '__main__':
    main()
