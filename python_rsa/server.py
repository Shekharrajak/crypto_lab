import socket
import os
from Crypto.PublicKey import RSA
from Crypto import Random

rng = Random.new().read
RSAkey = RSA.generate(1024, rng)

privatekey = RSAkey
publickey = RSAkey.publickey()
print(privatekey.exportKey()) #export under the 'PEM' format (I think)
print(publickey.exportKey())

file = open("Keys.txt", "w")
file.write(privatekey.exportKey()) #save exported private key
file.close()

data = "hello world"
enc_data = publickey.encrypt(data, 16) #encrypt message with public key
print(str(enc_data))

host = "localhost"
port = 12800
connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.connect((host, port))
# connexion.send(str(enc_data)) # send encrypted data, this appears to be the source of the problem
connexion.send(enc_data[0])
dec_data = RSAkey.decrypt(enc_data) # test decryption
print(dec_data)

os.system("pause")
