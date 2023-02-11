import socket

ADDRESS = "127.0.0.1",10003
SIZE = 1024 

calcin=input("Inserire calcolo 'num1 op num2': ")
calc=calcin.split()

if(len(calc)==3 and calc[0].isnumeric() and calc[2].isnumeric()):
    print("Connessione verso %s:%d" % ADDRESS)   
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect(ADDRESS)

    s.send(calc[0].encode())
    s.recv(1)
    s.send(calc[1].encode())
    s.recv(1)
    s.send(calc[2].encode())

    res=s.recv(SIZE).decode()
    if(res!=""):   
        print(res)
    else:
        print("Servizio negato\n")
else:
    print("Errore nell'input")


input("Press Enter to continue...")