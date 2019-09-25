import socket
import pickle
import DiffieHellman

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

def key_exchange():
    # Diffie Hellman
    privatekey = DiffieHellman.serverValues()
    baseMod = (0,0)
    #Recieving base and modulo from client
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    baseMod = pickle.loads(bytesAddressPair[0])
    #Calculating serverside dh-value and sending it
    serverValue = DiffieHellman.calc_dh(baseMod[0], privatekey, baseMod[1])
    UDPServerSocket.sendto(pickle.dumps(serverValue), bytesAddressPair[1])
    #Recieving clientside DH-value
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    clientValue = pickle.loads(bytesAddressPair[0])
    #Calculating real DH-value
    dh_value = DiffieHellman.calc_dh(clientValue, privatekey, baseMod[1])
    print(dh_value)
    return dh_value

key = key_exchange()
print(key)

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    print("IP-address: {}".format(address))
    print("Says: {}".format(message))

    UDPServerSocket.sendto(str.encode("Got it!"), address)