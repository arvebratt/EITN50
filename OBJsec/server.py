import socket

localIP         = "127.0.0.1"
localPort       = 20001
bufferSize      = 1024
msgFromServer   = "recieved my friend!"
bytesToSend     = str.encode(msgFromServer)
handshake       = False


# Creating datagram socket and binding IP address and port
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening.")

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    print("IP-address: {}".format(address))
    print("Says: {}".format(message))

    UDPServerSocket.sendto(str.encode("Got it!"), address)