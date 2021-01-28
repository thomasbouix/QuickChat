import unittest
import sys, os

sys.path.append('../')

import QuickChat_server as server
import QuickChat_client as client
import sqlite3
import QuickChat_bdd as bdd
import socketio

#Client test afin de pouvoir tester le serveur
sio_test = socketio.Client()
host = 'localhost'
port = 5000
sio_test.connect('http://{}:{}'.format(host, str(port)))

if(sio_test.connected):
    print('\033[32mIn a minute\033[39m')
    sio_test.emit("connexion")

# class testReceptionDonneesClient(unittest.TestCase):
#
#     def setUp(self):
#         #Création de la BDD
#         self.db_path = 'test_donnees.db'
#         self.connect = sqlite3.connect(self.db_path)
#         self.cursor = self.connect.cursor()
#         bdd.createDb(self.db_path)
#
#
#     def test_reception_donnees_connexion(self):
#         sio_test.emit('connexion', "{\'user\':\'Jean\', \'room\':\'room_test\'}")
#         sio_test.emit('connexion', "{\'user\':\'Jeremy\', \'room\':\'room_test\'}")
#         sio_test.emit('connexion', "{\'user\':\'Jonathan\', \'room\':\'room_test\'}")
#         #Verification de l'ajout du user dans la BDD
#         req = "SELECT username FROM USER;"
#         res = self.cursor.execute(req).fetchall()
#         print(res)
#         self.assertEqual(res, ['Jean','Jeremy','Jonathan']) #A verifier le format de res
#
#
#     def test_reception_donnees_message(self):
#         sio_test.emit('message', {"data" : "{'user':'Jean', 'message':'Bonjour, je suis Jean'}"})
#         req = "SELECT id, userId, roomId, text FROM MESSAGE WHERE id=1"
#         res = self.cursor.execute(req).fetchall()
#         print(res)
#         self.assertEqual(res, ['1','1','1', 'Bonjour, je suis Jean'])
#
#         data = '{\'user\':\'Jeremy\', \'message\':\'Bonjour, je suis Jeremy\'}'
#         sio_test.emit('message', data)
#         req = "SELECT * FROM MESSAGE WHERE id=2"
#         res = self.cursor.execute(req).fetchall()
#         print(res)
#         self.assertEqual(res, ['2','2','1', 'Bonjour, je suis Jeremy'])
#
#         sio_test.emit('message', "{\'user\':\'Jonathan\', \'message\':\'Bonjour, je suis Jonathan\'}")
#         req = "SELECT * FROM MESSAGE WHERE id=3"
#         res = self.cursor.execute(req).fetchall()
#         print(res)
#         self.assertEqual(res, ['3','3','1', 'Bonjour, je suis Jonathan'])
#
#         sio_test.emit('message', "{\'user\':\'Jeremy\', \'message\':\'Bonjour tout le monde !\'}")
#         req = "SELECT * FROM MESSAGE WHERE id=4"
#         res = self.cursor.execute(req).fetchall()
#         print(res)
#         self.assertEqual(res, ['3','2','1', 'Bonjour tout le monde !'])
#
#     def tearDown(self):
#         os.system('rm test_donnees.db')
#
# if __name__ == '__main__':
#     unittest.main()
