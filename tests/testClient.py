#!/usr/bin/python3

import unittest, os, sys, unittest
sys.path[:0] = ['../']

import QuickChat_server, QuickChat_client, QuickChat_bdd
import shutil,shlex, subprocess

import time

class testClient(unittest.TestCase):

    list_subprocess = []

    def kill_subprocess(self):
        while len(self.list_subprocess) != 0 :
            p = self.list_subprocess.pop()
            p.terminate()

    def launch_server(self):

        cmd = "python3 ../QuickChat_server.py &"
        args = shlex.split(cmd)
        p  = subprocess.Popen(args) # launch command as a subprocess
        self.list_subprocess.append(p)
        time.sleep(5) #Temps que le serveur se mette en place

    def test_connexion(self):
        self.launch_server()
        QuickChat_client.connexion()
        self.assertTrue(QuickChat_client.sio.connected)

    def test_historique(self):
        print("Mauvais type")
        entier = 0
        self.assertFalse(QuickChat_client.affichageHistorique(entier))
	
        print("Test list vide")
        vide = []
        self.assertFalse(QuickChat_client.affichageHistorique(vide))

    def tearDown(self):
        QuickChat_client.deconnexion()
        self.kill_subprocess()

if __name__ == '__main__':
    unittest.main()
