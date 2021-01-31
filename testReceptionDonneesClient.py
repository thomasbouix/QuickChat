import unittest
import sys, os
#
import QuickChat_server as server
import sqlite3
import QuickChat_bdd as bdd
import socketio

#Client test afin de pouvoir tester le serveur
# sio = socketio.Client()
#
# @sio.on('connect')
# def connect():
#     print("I'm connected!")
#     sio.emit('message', "{'foo': 'bar'}")
#
# sio.connect('http://localhost:5000')
# print('my sid is', sio.sid)

db_path = 'test_donnees.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

class testReceptionDonneesClient(unittest.TestCase):

    def test_reception_donnees_connexion(self):
        #Création de la BDD

        bdd.createDb(db_path)
        req = "INSERT INTO ROOM(name, password, private, size) VALUES(\"room_test\", \"\", 1, 10);"
        cursor.execute(req)
        conn.commit()

        sio_test.emit('connexion', "{\"username\":\"Jean\", \"room\":\"room_test\"}")
        sio_test.emit('connexion', "{\"username\":\"Jeremy\", \"room\":\"room_test\"}")
        sio_test.emit('connexion', "{\"username\":\"Jonathan\", \"room\":\"room_test\"}")
        #Verification de l'ajout du user dans la BDD
        req = "SELECT username FROM USER;"
        res = cursor.execute(req).fetchall()
        conn.commit()
        print(res)
        self.assertEqual(res, ['Jean','Jeremy','Jonathan']) #A verifier le format de res


    def test_reception_donnees_message(self):
        sio_test.emit('message_user', "{\"username\":\"Jean\", \"message\":\"Bonjour, je suis Jean\"}")
        req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=1;"
        res = cursor.execute(req).fetchall()
        conn.commit()
        print(res)
        self.assertEqual(res, ['1','1','1', 'Bonjour, je suis Jean'])

        sio_test.emit('message_user', '{\"username\":\"Jeremy\", \"message\":\"Bonjour, je suis Jeremy\"}')
        req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=2;"
        res = cursor.execute(req).fetchall()
        conn.commit()
        print(res)
        self.assertEqual(res, ['2','2','1', 'Bonjour, je suis Jeremy'])

        sio_test.emit('message_user', "{\"username\":\"Jonathan\", \"message\":\"Bonjour, je suis Jonathan\"}")
        req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=3;"
        res = cursor.execute(req).fetchall()
        conn.commit()
        print(res)
        self.assertEqual(res, ['3','3','1', 'Bonjour, je suis Jonathan'])

        sio_test.emit('message_user', "{\"username\":\"Jeremy\", \"message\":\"Bonjour tout le monde !\"}")
        req = "SELECT id, userId, roomId, mess FROM MESSAGE WHERE id=4;"
        res = cursor.execute(req).fetchall()
        conn.commit()
        print(res)
        self.assertEqual(res, ['3','2','1', 'Bonjour tout le monde !'])

if __name__ == '__main__':
    sio_test = socketio.Client()

    @sio_test.on('connect')
    def connect():
        print("I'm connected!")
        print(sio_test.get_sid())
        sio_test.emit('message', '{"data" : "Message test"}')

    @sio_test.on('message')
    def message(data):
        print(data)

    sio_test.connect('http://localhost:5000')
    print('my sid is', sio_test.sid)
    unittest.main()
    bdd.deleteDb(db_path)
