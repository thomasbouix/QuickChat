import socketio
from docopt import docopt

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
    
def main():
    arguments = docopt(help)
    if arguments['-p']:
        port = arguments['-p']
    if arguments['--host']:
        host = arguments['--host']

    connexion()

if __name__ == '__main__':
    main()
