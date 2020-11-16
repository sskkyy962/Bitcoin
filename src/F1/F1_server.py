from socket import *
import hashlib

turn = 1
initial_balance = 0
initial_balance_hex = hex(initial_balance)

serverPort2 = 11000  # F2
serverPort1 = 20000  # client-recieve
serverPort = 10000  # F1
serverSocketF1 = socket(AF_INET, SOCK_DGRAM)
serverName = 'localhost'
serverSocketF1.bind(('', serverPort))
print('The server is ready to receive')

while 1:
    message, clientAddress = serverSocketF1.recvfrom(2048)
    client_send = clientAddress
    modifiedMessage = message.decode()
    print(modifiedMessage)
    clientA = modifiedMessage
    # serverSocket.sendto(clientA.encode(), (serverName, serverPort1))
    serverSocketF1.sendto(clientA.encode(), (serverName, serverPort2))

    message1, clientAddress1 = serverSocketF1.recvfrom(2048)
    f1 = clientAddress1
    msg = message1.decode()
    print(msg)

    if client_send == clientAddress:  # receive tx and appending to temp_t.txt
        with open('Temp_T', '+a') as w:
            w.write(clientA.lstrip() + "\n")
        #
        with open('Temp_T', 'r') as f:
            counter = 0
            f_content = f.read()
            coList = f_content.split("\n")
            for i in coList:
                if i:
                    counter += 1
            # print(counter)
        if counter == 4:
            turn += 1
            if (turn % 2) == 1:
                serverSocketF1.close()
            else:
                lastblockhash = '{:32x}'.format(0)
                with open('Temp_T', 'r') as r:
                    f_content1 = r.readline()
                    print(f_content1)
                    f_content2 = r.readline()
                    f_content3 = r.readline()
                    f_content4 = r.readline()

                    def hash(mes):
                        m = hashlib.sha256()
                        m.update(mes.encode("utf-8"))
                        m.hexdigest()
                        return m

                    a = hash(mes=f_content1)
                    print(a)
                    b = hash(mes=f_content2)
                    print(b)
                    c = hash(mes=f_content3)
                    print(c)
                    d = hash(mes=f_content4)
                    print(d)





    # if f1 == clientAddress1:
