#!/usr/bin/python3

import unittest, os, sys, unittest
sys.path[:0] = ['../']
import QuickChat_server, QuickChat_client, QuickChat_bdd

class testClient(unittest.TestCase):

    def test_connexion(self):
        os.system('python3 ../QuickChat_server.py &')
        os.system('sleep 2')
        QuickChat_client.connexion()
        self.assertTrue(QuickChat_client.sio.connected)


if __name__ == '__main__':
    unittest.main()
