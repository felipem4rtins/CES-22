# Felipe Martins Gomes
# Comp 20
# Exercício: Servidor de Chat
# Programa compilado com PyCharm 2018.1.2


import socket
import sys
import time

s = socket.socket()
host = input(str("Por favor, digite o nome do host do servidor: "))
port = 8080
s.connect((host, port))
print("Conectado ao servidor de chat.")
while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server: ", incoming_message)
    message = input(str(">> "))
    message = message.encode()
    s.send(message)
    print("Mensagem enviada.")