import unittest
import sys, os

import socketio
import time
import sqlite3

import shutil
import shlex
import subprocess

sys.path[:0] = ['../']
import QuickChat_server as server
import QuickChat_bdd as bdd

class testReceptionDonneesClient(unittest.TestCase):

    list_subprocess = []

    def kill_subprocess(self):
        while len(self.list_subprocess) != 0 :
            p = self.list_subprocess.pop()
            p.terminate()

    def launch_server(self):

        cmd = "python3.7 ../QuickChat_server.py &"
        args = shlex.split(cmd)
        p  = subprocess.Popen(args) # launch command as a subprocess
        print("sub :")
        print(p)
        self.list_subprocess.append(p)
        time.sleep(5) #Temps que le serveur se mette en place

    def setUp(self):

        self.launch_server()

        self.db_path = 'quick_chat.db'
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.sio_test = socketio.Client()

        #Affiche I'm connected lorsque le serveur nous informe que le
        #client est connecté
        @self.sio_test.on('connect')
        def connect():
            print("I'm connected!")
            print(self.sio_test.get_sid())
            # self.sio_test.emit('message', {"data" : "Message test"})

        #Affiche les messages envoyés par le serveur
        @self.sio_test.on('message')
        def message(data):
            print(data)

        self.sio_test.connect('http://localhost:5000')
        print('my sid is', self.sio_test.sid)

        #Création de la BDD
        bdd.createDb(self.db_path)
        req = "INSERT INTO ROOM(name, password, private, size) VALUES(\"room_test\", \"\", 1, 10);"
        self.cursor.execute(req)
        self.conn.commit()

        time.sleep(2)

    def tearDown(self):
        bdd.deleteDb(self.db_path)
        self.sio_test.disconnect()
        self.kill_subprocess()

    def test_reception_donnees_connexion(self):

        #On emet des données type connexion au serveur
        self.sio_test.emit('connexion', {"username":"Jean", "room":"room_test"})
        self.sio_test.emit('connexion', {"username":"Jeremy", "room":"room_test"})
        self.sio_test.emit('connexion', {"username":"Jonathan", "room":"room_test"})

        #On fait attendre le test 2 secondes afin que l'ajout des données ait le
        #temps de se faire
        time.sleep(2)

        #Verification de l'ajout du user dans la BDD
        req = "SELECT username FROM USER;"
        res = self.cursor.execute(req).fetchall()
        self.conn.commit()
        # print(res)
        self.assertEqual(res, [('Jean',), ('Jeremy',), ('Jonathan',)])


    def test_reception_donnees_message(self):

        #On emet des données type connexion au serveur
        self.sio_test.emit('connexion', {"username":"Jean", "room":"room_test"})
        self.sio_test.emit('connexion', {"username":"Jeremy", "room":"room_test"})
        self.sio_test.emit('connexion', {"username":"Jonathan", "room":"room_test"})

        #On emet des données type message au serveur
        self.sio_test.emit('message_user',\
         {"username":"Jean",\
         "message":"Bonjour, je suis Jean"})
        self.sio_test.emit('message_user',\
         {"username":"Jeremy",\
          "message":"Bonjour, je suis Jeremy"})
        self.sio_test.emit('message_user',\
         {"username":"Jonathan",\
          "message":"Bonjour, je suis Jonathan"})
        self.sio_test.emit('message_user',\
         {"username":"Jeremy",\
          "message":"Bonjour tout le monde !"})

        #On fait attendre le test 2 secondes afin que l'ajout des données ait le
        #temps de se faire
        time.sleep(2)

        req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=1;"
        res = self.cursor.execute(req).fetchall()
        self.conn.commit()
        # print(res)
        self.assertEqual(res, [(1, 1, 1, 'Bonjour, je suis Jean')])

        req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=2;"
        res = self.cursor.execute(req).fetchall()
        self.conn.commit()
        # print(res)
        self.assertEqual(res, [(2, 2, 1, 'Bonjour, je suis Jeremy')])


        req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=3;"
        res = self.cursor.execute(req).fetchall()
        self.conn.commit()
        # print(res)
        self.assertEqual(res, [(3, 3, 1, 'Bonjour, je suis Jonathan')])


        req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=4;"
        res = self.cursor.execute(req).fetchall()
        self.conn.commit()
        # print(res)
        self.assertEqual(res, [(4, 2, 1, 'Bonjour tout le monde !')])
        # self.kill_subprocess()

if __name__ == '__main__':
    unittest.main()
