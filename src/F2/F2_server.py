from socket import *

turn = 2
initial_balance = 0
initial_balance_hex = hex(initial_balance)
serverName = 'localhost'
serverPort1 = 10000 #F1
serverPort = 11000 # F2
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')
while 1:
    message3, clientAddress3 = serverSocket.recvfrom(2048)
    modifiedMessage = message3.decode()
    print(modifiedMessage)
    msg = 'hi'


    message4, clientAddress4 = serverSocket.recvfrom(2048)
    modifiedMessage1 = message4.decode()
    print(modifiedMessage1)
    serverSocket.sendto(msg.encode(), (serverName, serverPort1))