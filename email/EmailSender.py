from socket import *
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'gmail-smtp-in.l.google.com'

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)

# Port number may change according to the mail server
clientSocket.connect((mailserver, 25))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
	print('220 reply not received from server.')

# Send HELO command and print server response.

heloCommand = 'HELO gmail \r\n'
print(heloCommand)
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
	print('250 reply not received from server.')

# Send MAIL FROM command and print server response.

FROM = 'MAIL FROM: <quinninthetardis@gmail.com>\r\n'
print(FROM)
clientSocket.send(FROM.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
	print('250 reply not received from server.')

# Send RCPT TO command and print server response.

TO = 'RCPT TO: <drpham.wit@gmail.com>\r\n'
print(TO)
clientSocket.send(TO.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '250':
	print('250 reply not received from server.')

# Send DATA command and print server response.

DATA = 'DATA \r\n'
print(DATA)
clientSocket.send(DATA.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '354':
	print('250 reply not received from server.')

# Send message data. Make sure to include header lines: From, To, Subject
# Message ends with a single period.
END = 'From: <quinninthetardis@gmail.com>\r\nTo: <drpham.wit@gmail.com>\r\nSubject: This is a test\r\nHello!\r\nHave a good day!\r\nQuinn\r\n.\r\n'
print(END)
clientSocket.send(END.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
	print('250 reply not received from server.')
# Send QUIT command and get server response.

QUIT = 'QUIT\r\n'
print(QUIT)
clientSocket.send(QUIT.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '221':
	print('250 reply not received from server.')
