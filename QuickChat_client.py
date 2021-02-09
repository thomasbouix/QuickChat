"""
    QuickChat_client : Gestion des messages clients et des arguments lors de l'execution du script
"""

import socketio
from docopt import docopt

sio = socketio.Client()
host = 'localhost'
port = 5000

help = """
Usage:
    QuickChat_client.py <username> <room> [--host <name> -p <port>]

Options:
    -h --help       : Obtenir de l'aide
    --host <name>   : Choix de l'host (defaut: localhost)
    -p <port>       : Choix du port (defaut: 5000)
"""


@sio.on('connect')
def connect():
    """ Affichage d'un message lorsque le client reçois un évènement de connexion du serveur """
    if sio.connected:
        print('\033[32msuccessfully connected\033[39m')

@sio.on('disconnect')
def disconnect():
    """ Affichage d'un message en cas de perte de connexion avec le serveur """
    print('\033[31mdisconnected\033[39m')

def connexion():
    """ Fonction permettant une tentative de connexion au serveur """
    sio.connect('http://{}:{}'.format(host, str(port)))

#Fonction permettant de se deconnecter
def deconnexion():
    """ Description : TODO """
    sio.disconnect()

@sio.on('historique')
def affichageHistorique(data_historique):
    if type(data_historique) != list:
        print("pas type list")
            return False

    if not data_historique:
        print("pas d'historique")
            return False

    for message in data_historique :
        print(message)
        print('\n')

def main():
    """ Gestion des arguments passés lors de l'éxécution du script """
    arguments = docopt(help)
    if arguments['-p']:
        port = arguments['-p']
    if arguments['--host']:
        host = arguments['--host']

    connexion()

if __name__ == '__main__':
    main()
