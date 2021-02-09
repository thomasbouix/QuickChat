#!/usr/bin/python3

import unittest, os, sys, unittest
sys.path[:0] = ['../']
import QuickChat_server, QuickChat_client, QuickChat_bdd, sqlite3
from datetime import *

class testServer(unittest.TestCase):

    db_path = 'quick_chat.db'

    # Classmethod appelé à la fin de tous les tests
    # @classmethod
    # def setUpClass(cls):
    #     # Initialisation de la db et du path
    #     cls.db_path = 'quick_chat.db'
    #     print("Initialise cls.db_path to quick_chat.db")
    #     cls.connect = sqlite3.connect(cls.db_path)
    #     cls.cursor = cls.connect.cursor()

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
    
    def test_Create_Table_Room_db(self):
        # Test de la création de la table des rooms
        QuickChat_server.createTableRoom()
        print("Test de creation de la table")
        requete = "SELECT name FROM sqlite_master WHERE type='table';"
        self.assertEqual(self.cursor.execute(requete).fetchall(), [('sqlite_sequence',), ('Room',)])
        
        requete = "DROP TABLE Room;"
        self.cursor.execute(requete)

    
    def test_Add_Room(self):
        # Test d'ajout d'une salle
        QuickChat_server.createTableRoom()
        QuickChat_server.addRoom("room1", "0000", False, 10)
        print("Test de creation d'une room dans la table")
        requete = "SELECT * FROM Room;"
        resp = self.cursor.execute(requete).fetchall()
        self.assertEqual(resp, [(1, 'room1', '0000', 0, 10)])
        
        requete = "DROP TABLE Room;"
        self.cursor.execute(requete)
    
    # Classmethod appelé à la fin de tous les tests
    # @classmethod
    # def tearDownClass(cls):
    #     cls.connect.close()
    #     if(os.path.exists(cls.db_path)):
    #         print("Destruction de la db")
    #         os.remove(cls.db_path)


if __name__ == '__main__':
    unittest.main()
