from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while 1:
    connectionSocket,addr = serverSocket.accept()
    print('Find a new connection from %s',addr)
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.decode('utf-8').upper().encode()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()

