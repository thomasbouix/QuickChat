#!/usr/bin/python3

import unittest, os, sys, unittest
sys.path[:0] = ['../']
import QuickChat_server, QuickChat_client, QuickChat_bdd
import shutil,shlex, subprocess
import sqlite3

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

    def test_verifArg(self):
        self.assertFalse(QuickChat_client.verifArg(0))
        self.assertFalse(QuickChat_client.verifArg(6))

        self.assertTrue(QuickChat_client.verifArg(2))
        self.assertTrue(QuickChat_client.verifArg(4))

    def test_writeMessage(self):
        data = {}
        print("Entrée un message : \n")
        data = QuickChat_client.writeMessage(data)
        print(data['message'])

    def test_listArg(self):
        cmd = "python3 ../QuickChat_client.py name room &"
        arg = shlex.split(cmd)
        arg.remove('python3')
        arg.remove('../QuickChat_client.py')
        arg.remove('&')
        data = QuickChat_client.listArg(arg)
        self.assertEqual(data['username'], 'name')
        self.assertEqual(data['room'], 'room')

    def tearDown(self):
        QuickChat_client.deconnexion()
        self.kill_subprocess()


if __name__ == '__main__':
    unittest.main()
