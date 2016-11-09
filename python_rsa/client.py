import socket
import os
from Crypto.PublicKey import RSA
from Crypto import Random

host = ''
port = 12800

connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.bind((host, port))
connexion.listen(5)
clientconnexion, connexioninfo = connexion.accept()
enc_data = clientconnexion.recv(1024) # receive encrypted data
print(enc_data)
print("---done 1 ---")
file = open("Keys.txt", "r")
privatestr = file.read() # retrieve exported private key from file
file.close()

print(privatestr)
print("---done 2 ---")
privatekey = RSA.importKey(privatestr) # import private key
data = privatekey.decrypt(enc_data) # decrypt sent encrypted data
print("---done 3 ---")
print(data)

os.system("pause")
