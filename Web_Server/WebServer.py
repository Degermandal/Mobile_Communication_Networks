#http://192.168.56.1:6789/HelloWorld.html
#http://localhost:6789/HelloWorld.html
#http://192.168.56.1:6789/Network.html

# import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket

#Fill in start
#Connect the TCP socket to the specified port ---
serverSocket.bind(('', 6789))
#Maximum number of connections is 1 ---
serverSocket.listen(1)
#Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')

    #After the client receives the connection request, create a new TCP connection socket ---
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end

    try:
        #Receive the message sent by the client ---
        message = connectionSocket.recv(1024)#Fill in start #Fill in end
        print("Message:", message)
        filename = message.split()[1]
        print("FileName:", filename)
        f = open(filename[1:])
        outputdata = f.read()#Fill in start #Fill in end
        # Send one HTTP header line into socket

        # Fill in start
        header = ' HTTP/1.1 200 OK\nConnection: close\nContent-Type: text/html\nContent-Length: %d\n\n' % (
            len(outputdata))
        connectionSocket.send(header.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            #I changed the below code with the above code because it gived to me error
            #connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        # Send response message for file not found

        #Fill in start
        #connectionSocket.send((' HTTP/1.1 404 Not Found ').encode())
        connectionSocket.send(('404 Not Found').encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()

