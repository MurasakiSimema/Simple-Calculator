from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

def NewClient():
    while True:
        client, address = server.accept()
        print("Connessione da: %s:%d" % address)
        thread = Thread(target=Comunicazione, args=(client,))
        thread.start()


def Comunicazione(client):
    num1 = float(client.recv(SIZE).decode())
    client.send(ACK.encode()) 
    op = client.recv(SIZE).decode()
    client.send(ACK.encode()) 
    num2 = float(client.recv(SIZE).decode())

    if(op=='+'):
        res=num1+num2
        client.send(str(res).encode())
    elif (op=='-'):
        res=num1-num2
        client.send(str(res).encode())
    elif (op=='/'):
        res=num1/num2
        client.send(str(res).encode())
    elif(op=='*'):
        res=num1*num2
        client.send(str(res).encode())
    else:
        client.send("".encode())
        




PORT = 10003
HOSTNAME = "localhost" 
SIZE = 1024
ACK = "\x06" 

server = socket(AF_INET, SOCK_STREAM)
server.bind((HOSTNAME, PORT))

server.listen()
mainThread = Thread(target=NewClient)
mainThread.start()
mainThread.join()  # Aspetta l'esecuzione del mainThread
server.close()