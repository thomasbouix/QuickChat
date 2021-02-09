#!/usr/bin/python3

import unittest, os, sys, unittest
import socketio, time, sqlite3
import shutil,shlex, subprocess

sys.path[:0] = ['../']
#import QuickChat_client
import QuickChat_server as server
import QuickChat_bdd as bdd
from datetime import datetime


class testServer(unittest.TestCase):

    db_path = 'quick_chat.db'

    list_subprocess = []

    # def test_reception_historique(self):
    #     date = datetime.now()
    #     bdd.resetDb(self.db_path)
    #     connect = sqlite3.connect(self.db_path)

    #     cursor = connect.cursor()
    #     cursor.execute('INSERT INTO User (username, password) VALUES ("user1","pass")')
    #     cursor.execute('INSERT INTO Room (name, password, private, size) VALUES ("room1","pass","False",10)')
    #     cursor.execute('INSERT INTO Message (userId, roomId, mess, sendDate) VALUES (1,1,"Mon premier message","{}")'.format(date))
    #     connect.commit()
    #     res = server.getHistorique("room1")
    #     self.assertTrue( res == ['{} - user1 : Mon premier message'.format(str(date).split('.')[0])])

    # def kill_subprocess(self):
    #     while len(self.list_subprocess) != 0 :
    #         p = self.list_subprocess.pop()
    #         p.terminate()

    # def launch_server(self):

    #     cmd = "python3 ../server.py &"
    #     args = shlex.split(cmd)
    #     p  = subprocess.Popen(args) # launch command as a subprocess
    #     self.list_subprocess.append(p)
    #     time.sleep(5) #Temps que le serveur se mette en place

    # def setUp(self):

    #     self.launch_server()

    #     self.db_path = 'quick_chat.db'
    #     self.conn = sqlite3.connect(self.db_path)
    #     self.cursor = self.conn.cursor()
    #     self.sio_test = socketio.Client()

    #     #Affiche un message lorsque le serveur nous informe que le
    #     #client est connecté
    #     @self.sio_test.on('connect')
    #     def connect():
    #         print("Connecté au serveur.")
    #         print(self.sio_test.get_sid())
    #         # self.sio_test.emit('message', {"data" : "Message test"})

    #     #Affiche les messages envoyés par le serveur
    #     @self.sio_test.on('message')
    #     def message(data):
    #         print(data)

    #     self.sio_test.connect('http://localhost:5000')

    #     #Création de la BDD
    #     bdd.resetDb(self.db_path)
    #     req = "INSERT INTO ROOM(name, password, private, size) VALUES(\"room_test\", \"\", 1, 10);"
    #     self.cursor.execute(req)
    #     self.conn.commit()

    #     time.sleep(2)

    # def tearDown(self):
    #     bdd.deleteDb(self.db_path)
    #     self.sio_test.disconnect()
    #     self.kill_subprocess()

    # def test_reception_donnees_connexion(self):

    #     #On emet des données type connexion au serveur
    #     self.sio_test.emit('connexion', {"username":"Jean", "room":"room_test"})
    #     self.sio_test.emit('connexion', {"username":"Jeremy", "room":"room_test"})
    #     self.sio_test.emit('connexion', {"username":"Jonathan", "room":"room_test"})

    #     #On fait attendre le test 2 secondes afin que l'ajout des données ait le
    #     #temps de se faire
    #     time.sleep(2)

    #     #Verification de l'ajout du user dans la BDD
    #     req = "SELECT username FROM USER;"
    #     res = self.cursor.execute(req).fetchall()
    #     self.conn.commit()
    #     # print(res)
    #     self.assertEqual(res, [('Jean',), ('Jeremy',), ('Jonathan',)])


    # def test_reception_donnees_message(self):

    #     #On emet des données type connexion au serveur
    #     self.sio_test.emit('connexion', {"username":"Jean", "room":"room_test"})
    #     self.sio_test.emit('connexion', {"username":"Jeremy", "room":"room_test"})
    #     self.sio_test.emit('connexion', {"username":"Jonathan", "room":"room_test"})

    #     #On emet des données type message au serveur
    #     self.sio_test.emit('message_user',\
    #      {"username":"Jean",\
    #      "message":"Bonjour, je suis Jean"})
    #     self.sio_test.emit('message_user',\
    #      {"username":"Jeremy",\
    #       "message":"Bonjour, je suis Jeremy"})
    #     self.sio_test.emit('message_user',\
    #      {"username":"Jonathan",\
    #       "message":"Bonjour, je suis Jonathan"})
    #     self.sio_test.emit('message_user',\
    #      {"username":"Jeremy",\
    #       "message":"Bonjour tout le monde !"})

    #     #On fait attendre le test 2 secondes afin que l'ajout des données ait le
    #     #temps de se faire
    #     time.sleep(2)

    #     req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=1;"
    #     res = self.cursor.execute(req).fetchall()
    #     self.conn.commit()
    #     # print(res)
    #     self.assertEqual(res, [(1, 1, 1, 'Bonjour, je suis Jean')])

    #     req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=2;"
    #     res = self.cursor.execute(req).fetchall()
    #     self.conn.commit()
    #     # print(res)
    #     self.assertEqual(res, [(2, 2, 1, 'Bonjour, je suis Jeremy')])


    #     req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=3;"
    #     res = self.cursor.execute(req).fetchall()
    #     self.conn.commit()
    #     # print(res)
    #     self.assertEqual(res, [(3, 3, 1, 'Bonjour, je suis Jonathan')])


    #     req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=4;"
    #     res = self.cursor.execute(req).fetchall()
    #     self.conn.commit()
    #     # print(res)
    #     self.assertEqual(res, [(4, 2, 1, 'Bonjour tout le monde !')])
    
    def test_add_user(self):
        bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()

        # right password format 
        userInfo = {'username':'user1','password':'Aa1234567,'}
        server.add_user(userInfo)
        sql = "SELECT password FROM User WHERE username='user1';"
        res = cursor.execute(sql).fetchall()[0][0]    
        self.assertEqual(res, "Aa1234567,") 

         # wrong password format 
        userInfo = {'username':'user2','password':'123456789'}
        server.add_user(userInfo)
        sql = "SELECT password FROM User WHERE username='user2';"
        self.assertNotIn(('123456789',),cursor.execute(sql).fetchall()) 

        connect.commit()

    def test_add_room(self):
        bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()

        roomInfo = {'roomname':'room1','password':'123456789','private':1,'size':50}
        server.add_room(roomInfo)

        sql = "SELECT password FROM Room WHERE name='room1';"
        res = cursor.execute(sql).fetchall()[0][0]

        self.assertEqual(res, "123456789")

        connect.commit()
    
    def test_join_room(self):
        bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        # Sign up the room and the user 
        roomInfo = {'roomname':'room1','password':'123456789','private':1,'size':50}
        server.add_room(roomInfo)
        userInfo = {'username':'user1','password':'Aa1234567,'}
        server.add_user(userInfo)

        server.join_room("room1","user1")
        sql = 'SELECT idroom FROM RoomUser WHERE iduser=1;'

        self.assertEqual(cursor.execute(sql).fetchall()[0][0], 1)

        connect.commit()
        
if __name__ == '__main__':
    unittest.main()
