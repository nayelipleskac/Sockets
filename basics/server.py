import socket, atexit

#Address Family (AF) - IPv4
#Socket Type- TCP
host = '127.0.0.1' #binds to localhost 127.0.0.1
port = 1234
backlog=5 # number of pending connections in queue

# def handle_exit():
#     print('This runs after a keyboard interrupt')
#     s.close()
# atexit.register(handle_exit)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    print('socket binded to port %s' %(port))
    s.listen(backlog)
    conn, addr = s.accept() #get client's socket obj and network address
    print('Socket is listening...')
    print('Got a connecton from ', addr)
    # conn.send('thank you for connecting '.encode())
    with conn:
        while True: 
            data = input('Hello, say something to the client: ')
            print('waiting for the clients response...')
            if data == 'break':
                break
            conn.send(data.encode())
            data = conn.recv(1024).decode('utf-8')
            print(addr,":", data.encode())
            print('Message recieved: ', data)

    # s.close()
    