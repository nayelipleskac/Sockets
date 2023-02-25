import socket
import pygame
from pygame.locals import *


class Server:
    def __init__(self, host='localhost', port=1234):
        self.HOST = host
        self.PORT = port
        self.connect()
        
        self.b = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',}
        self.running = True
        self.p = 'x'
        self.clock = pygame.time.Clock()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.HOST, self.PORT))
        self.socket.listen(1)

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption("Server")

    def start(self):
        self.conn, self.addr = self.socket.accept()
        print('Connected by', self.addr)

        while self.running:
            pygame.display.update()

            for event in pygame.event.get():
                data = self.conn.recv(1024).decode()
                if not data:
                    pass
                print('Received', data)
                
                if event.type == QUIT:
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    print("x, y: {}, {}".format(x,y))
                    self.conn.sendall("{}, {}".format(x, y).encode())

app = Server()
app.start()

##        while True:
##            data = self.conn.recv(1024).decode()
##            if not data:
##                break
##            print('Received', data)
##            self.conn.sendall(input('Enter: ').encode())                


