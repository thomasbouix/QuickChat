import unittest, os, unittest, sqlite3, sys
sys.path[:0] = ['../']
import QuickChat_public_room

class testClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialisation de la db et du path
        cls.db_path = 'quick_chat.db'
        print("Initialise cls.db_path to quick_chat.db")
        cls.connect = sqlite3.connect(cls.db_path)
        cls.cursor = cls.connect.cursor()
    
    def test_Create_Table_Room_db(self):
        # Test de la création de la table des rooms
        QuickChat_public_room.createTableRoom()
        print("Test de creation de la table")
        requete = "SELECT name FROM sqlite_master WHERE type='table';"
        self.assertEqual(self.cursor.execute(requete).fetchall(), [('sqlite_sequence',), ('Room',)])
        
        requete = "DROP TABLE Room;"
        self.cursor.execute(requete)

    
    def test_Add_Room(self):
        # Test d'ajout d'une salle
        QuickChat_public_room.createTableRoom()
        QuickChat_public_room.addRoom("room1", "0000", False, 10)
        print("Test de creation d'une room dans la table")
        requete = "SELECT * FROM Room;"
        resp = self.cursor.execute(requete).fetchall()
        self.assertEqual(resp, [(1, 'room1', '0000', 0, 10)])
        
        requete = "DROP TABLE Room;"
        self.cursor.execute(requete)

    @classmethod
    def tearDownClass(cls):
        cls.connect.close()
        if(os.path.exists(cls.db_path)):
            print("Destruction de la db")
            os.remove(cls.db_path)

if __name__ == '__main__':
    unittest.main()
