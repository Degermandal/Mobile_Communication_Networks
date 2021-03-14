from socket import *
import time

#Server address, localhost is used.
serverName = '127.0.0.1'
#Port specified by the server
serverPort = 12000
#Create UDP socket, use IPv4 protocol
clientSocket = socket(AF_INET, SOCK_DGRAM)
#Set the socket timeout value to 1 second
clientSocket.settimeout(1)

for i in range(0, 10):
    sendTime = time.time()
    #Generate datagrams, encode bytes to send
    message = ('Ping %d %s' % (i + 1, sendTime)).encode()
    try:
        #Send information to the server
        clientSocket.sendto(message, (serverName, serverPort))
        #Get information from the server, also get the server address
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)
        #Calculate round trip time
        rtt = time.time() - sendTime

        print('Sequence %d: Reply from %s RTT = %.4fs' % (i + 1, serverName, rtt))
    except Exception as e:
        #print(e)
        print('Sequence %d: Request timed out' % (i + 1))

#close the socket
clientSocket.close()