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

def recieve_handshake():
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        clientMsg = "Message from Client: {}".format(message)
        clientIP  = "Client IP Address: {}".format(address)

        if(clientMsg == "Message from Client: hej min vän"):
            print(clientMsg)
            print(clientIP)
            handshake = True

while(handshake == False):
    recieve_handshake()
    print("Still waiting...")
    time.sleep(1)











# def server_up():
#     # Listen for incoming datagrams
#     while(True):

#         bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
#         message = bytesAddressPair[0]
#         address = bytesAddressPair[1]

#         clientMsg = "Message from Client:{}".format(message)
#         clientIP  = "Client IP Address:{}".format(address)

#         print(clientMsg)
#         print(clientIP)

#         # Sending a reply to client
#         UDPServerSocket.sendto(bytesToSend, address)
