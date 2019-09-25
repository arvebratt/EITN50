import socket
import DiffieHellman
import pickle

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

def key_exchange():
    # Diffie Hellman
    privatekey = DiffieHellman.clientValues()
    baseMod = (0,0)
    baseMod = DiffieHellman.sharedValues(baseMod[0], baseMod[1])
    #Sending public base and modulo
    UDPClientSocket.sendto(pickle.dumps(baseMod), serverAddressPort)
    #Recieving calculated value from server
    bytesAddressPair = UDPClientSocket.recvfrom(bufferSize)
    serverValue = pickle.loads(bytesAddressPair[0])
    #Sending clientside DH-value
    clientValue = DiffieHellman.calc_dh(baseMod[0], privatekey, baseMod[1])
    UDPClientSocket.sendto(pickle.dumps(clientValue), serverAddressPort) 
    #Calculating real DH-value
    dh_value = DiffieHellman.calc_dh(serverValue, privatekey, baseMod[1])

    print(dh_value)
    return dh_value

key = key_exchange()
print(key)

# Send to server using created UDP socket
while True:
    msgFromClient = input("What do you want to send? ", )

    UDPClientSocket.sendto(str.encode(msgFromClient), serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    print(format(msgFromServer[0]))