import ssl
from socket import *
import base64

#Mail Content
subject = "TERM PROJECT"
textT = "text/plain"
msg = "Sending mail with SMTP protocol is DONE."
endmsg = "\r\n.\r\n"

# Choose gmail mail server
mailserver = ("smtp.gmail.com", 587)

#Sender and receiver
#mailFrom = "mailFrom@gmail.com"
mailFrom = input("Mail From:")
rcptTo = input("Mail To:")
#rcptTo = "rcptTo@gmail.com"

passw = input("Password:")

#Authentication information
username = base64.b64encode(mailFrom.encode()).decode()
password = base64.b64encode(passw.encode()).decode()

# Create socket called clientSocket and establish a TCP connection with mail server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

#Get response and print
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

#Send STARTTLS command
command = 'STARTTLS\r\n'
clientSocket.send(command.encode())
#Get response and print
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

#Wrap socket for security
Socket = ssl.wrap_socket(clientSocket)

#Send Auth Login command
Socket.sendall('AUTH LOGIN\r\n'.encode())
recv = Socket.recv(1024).decode()
print(recv)
if (recv[:3] != '334'):
    print('334 reply not received from server')

#Send username
Socket.sendall((username + '\r\n').encode())
recv = Socket.recv(1024).decode()
print(recv)
if (recv[:3] != '334'):
    print('334 reply not received from server')

#Send password
Socket.sendall((password + '\r\n').encode())
recv = Socket.recv(1024).decode()
print(recv)
if (recv[:3] != '235'):
    print('235 reply not received from server')

# Send Mail From command and print server response.
Socket.sendall(('MAIL FROM: <' + mailFrom + '>\r\n').encode())
recv = Socket.recv(1024).decode()
print(recv)
if (recv[:3] != '250'):
    print('250 reply not received from server')

# Send Rcpt To command and print server response.
Socket.sendall(('RCPT TO: <' + rcptTo + '>\r\n').encode())
recv = Socket.recv(1024).decode()
print(recv)
if (recv[:3] != '250'):
    print('250 reply not received from server')

# Send DATA command and print server response.
Socket.send('DATA\r\n'.encode())
recv = Socket.recv(1024).decode()
print(recv)
if (recv[:3] != '354'):
    print('354 reply not received from server')

# Send message data.
message = 'Mail from:' + mailFrom + '\r\n'
message += 'Recipient To:' + rcptTo + '\r\n'
message += 'Subject:' + subject + '\r\n'
message += 'Text type:' + textT + '\t\n'
message += '\r\n' + msg
Socket.sendall(message.encode())

# Message ends with a single period.
Socket.sendall(endmsg.encode())
recv = Socket.recv(1024).decode()
print(recv)
if (recv[:3] != '250'):
    print('250 reply not received from server')

# Send QUIT command and get server response.
Socket.sendall('QUIT\r\n'.encode())

# Close connection
Socket.close()
