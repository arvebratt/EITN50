import socket

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
while True:
    msgFromClient = input("What do you want to send? ", )

    UDPClientSocket.sendto(str.encode(msgFromClient), serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    print(format(msgFromServer[0]))