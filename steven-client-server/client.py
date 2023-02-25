import socket
import pygame
from pygame.locals import *


class Client:
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port
        self.connect()
        
        self.b = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:'',}
        self.running = True
        self.p = 'o'
        self.clock = pygame.time.Clock()

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.HOST, self.PORT))

    def setup(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
        pygame.display.set_caption("client")

        
    def start(self):
        print("Connected to ", self.HOST)
        self.socket.sendall('Connection establish'.encode())

        while self.running:
            pygame.display.update()

            for event in pygame.event.get():
                data = self.socket.recv(1024).decode()
                if not data:
                    print(data)
                print('Received', data)
            
                if event.type == QUIT:
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    print("x, y: {}, {}".format(x,y))

app = Client('10.0.0.250', 1234)
app.start()

##        while True:
##            data = s.recv(1024).decode()
##            if not data:
##                break
##            print('Received', data)
##            s.sendall(input('Enter: ').encode())


