import socket
import atexit
host = '127.0.0.1' #localhost
port = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port)) #connect to host and port of server
    print('connected')

    while True:
        #recieve message from server
        data = s.recv(1024)
        print('recieved from server: ', data.decode())
        #enter message to send
        data = input('say something to the server: ')
        s.send(data.encode())
        if data == 'break':
            break
    # s.close()
#