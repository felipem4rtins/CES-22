# Felipe Martins Gomes
# Comp 20
# Exercício: Servidor de Chat
# Programa compilado com PyCharm 2018.1.2


import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print("Servidor iniciado no host:", host)
port = 8080
s.bind((host, port))
print("Conexão feita com sucesso!")
print("Aguardando mensagem...")
s.listen(1)
conn, addr = s.accept()
print(addr, "Conectou-se ao servidor e agora está on-line.")
while 1:
    message = input(str(">> "))
    message = message.encode()
    conn.send(message)
    print("Mensagem enviada.")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client: ", incoming_message)