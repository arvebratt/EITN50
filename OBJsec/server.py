import socket
import time

localIP         = "127.0.0.1"
localPort       = 20001
bufferSize      = 1024
msgFromServer   = "recieved my friend!"
bytesToSend     = str.encode(msgFromServer)
handshake       = False


# Creating datagram socket and binding IP address and port
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening, awaiting handshake from client.")

bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
message = bytesAddressPair[0]
address = bytesAddressPair[1]

clientMsg = format(message)
clientIP  = format(address)
print(clientMsg)
if(clientMsg == "b'hej server'"):
    UDPServerSocket.sendto(str.encode("hej client"), address)