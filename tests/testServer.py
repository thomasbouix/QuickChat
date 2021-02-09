#!/usr/bin/python3

import unittest, os, sys, unittest
sys.path[:0] = ['../']
import QuickChat_server, QuickChat_bdd, sqlite3 #QuickChat_client

from datetime import *

class testServer(unittest.TestCase):

    db_path = 'quick_chat.db'

    def test_reception_historique(self): 
        date = datetime.now()
        QuickChat_bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)

        cursor = connect.cursor()
        cursor.execute('INSERT INTO User (username, password) VALUES ("user1","pass")')
        cursor.execute('INSERT INTO Room (name, password, private, size) VALUES ("room1","pass","False",10)')
        cursor.execute('INSERT INTO Message (userId, roomId, mess, sendDate) VALUES (1,1,"Mon premier message","{}")'.format(date))
        connect.commit()

        res = QuickChat_server.getHistorique("room1")
        self.assertTrue( res == ['{} - user1 : Mon premier message'.format(str(date).split('.')[0])])


    def test_add_user(self):
        QuickChat_bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()

        # right password format 
        userInfo = {'username':'user1','password':'Aa1234567,'}
        QuickChat_server.add_user(userInfo)
        sql = "SELECT password FROM User WHERE username='user1';"
        res = cursor.execute(sql).fetchall()[0][0]    
        self.assertEqual(res, "Aa1234567,") 

         # wrong password format 
        userInfo = {'username':'user2','password':'123456789'}
        QuickChat_server.add_user(userInfo)
        sql = "SELECT password FROM User WHERE username='user2';"
        self.assertNotIn(('123456789',),cursor.execute(sql).fetchall()) 

        connect.commit()

    def test_add_room(self):
        QuickChat_bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()

        roomInfo = {'roomname':'room1','password':'123456789','private':1,'size':50}
        QuickChat_server.add_room(roomInfo)

        sql = "SELECT password FROM Room WHERE name='room1';"
        res = cursor.execute(sql).fetchall()[0][0]

        self.assertEqual(res, "123456789")

        connect.commit()
    
    def test_join_room(self):
        QuickChat_bdd.resetDb(self.db_path)
        connect = sqlite3.connect(self.db_path)
        cursor = connect.cursor()
        # Sign up the room and the user 
        roomInfo = {'roomname':'room1','password':'123456789','private':1,'size':50}
        QuickChat_server.add_room(roomInfo)
        userInfo = {'username':'user1','password':'Aa1234567,'}
        QuickChat_server.add_user(userInfo)

        QuickChat_server.join_room("room1","user1")
        sql = 'SELECT idroom FROM RoomUser WHERE iduser=1;'

        self.assertEqual(cursor.execute(sql).fetchall()[0][0], 1)

        connect.commit()

if __name__ == '__main__':
    unittest.main()
