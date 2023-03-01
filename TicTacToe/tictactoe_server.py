import socket, atexit, pygame, time
from pygame.constants import KEYDOWN, KEYUP, K_DOWN, K_UP, K_s, K_w
from pygame.locals import *

class Player:
    def __init__(self):
        self.v = None
    def value(self):
        return self.v

class X(Player):
    def __init__(self):
        Player().__init__()
        self.v = 'x'

class O(Player):
    def __init__(self):
        super().__init__()
        print(super())
        self.v = 'o'

class TicTacToe():
    def __init__(self): 
        self.board= {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
        self.p = 'x'
        self.s = None
        self.running = True
    def play(self, conn, socket):
        self.conn = conn
        self.s = socket

        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Tic-Tac-Toe server")
        for x in range(0,600,200):
            for y in range(0,600,200):
                pygame.draw.rect(self.screen,(255,255,255), (x,y,200,200),1)

        while self.running:
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                    x,y = pygame.mouse.get_pos()
                    print('x: {}, y: {}'.format(x,y))
                    self.conn.sendall('{}, {}'.format(x,y).encode())



    def update(self, pos, val):
        self.board[pos] = val

class Server():
    def __init__(self):
        self.host = '127.0.0.1'
        self.port= 1234
        self.backlog = 5
        self.screen = None
        self.player= ''
        self.g = TicTacToe()
        #self.connect in __init__
    
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port)) #start server connection 
            print('socket binded to port %s' %(self.port))
            print('Socket is listening...')
            s.listen(1)
            conn, addr = s.accept()  #accept connection 
            with conn:
                self.g.play(conn, s)
                print('Got a connecton from ', addr)
                conn.send('thank you for connecting '.encode())


    def startGame(self):
        print('Starting game...')
        pygame.init()  #initiate pygame and set caption
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Tic-Tac-Toe server")
        for x in range(0,600,200):
            for y in range(0,600,200):
                pygame.draw.rect(self.screen,(255,255,255), (x,y,200,200),1)
        print('Server: set up board')
        # while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            # if self.player == 'x':
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                print('event.type: pygame.msebtn')
                x,y = pygame.mouse.get_pos()
                print('server: ','x:',x,'y',y)
                # x,y = event.pos
                # data = str(x) + ',' + str(y)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self.host,self.port))
                print('socket binded to port %s' %(self.port))
                s.listen(self.backlog)
                conn, addr = s.accept() #get client's socket obj and network address
                print('Socket is listening...')
                print('Got a connecton from ', addr) #
                with conn:
                    while True:
                        # self.player = 'x'  
                        data = str(x) + ',' + str(y)
                        data = b'server message'
                        print(data, ' server data')
                        print('Server: mouse btn position: ', data)
                        conn.send(data.encode())
                        # self.player= 'o'
                        data = conn.recv(1024).decode('utf-8')
                        print(addr,":", data.encode())
                        print('Server: Message recieved: ', data)
                        pygame.display.update()  

                        
    
    def drawX(self,x,y, screen):  
        pygame.draw.line(screen,(255,255,255),(x-50,y-50),(x+50,y+50),1) 
        pygame.draw.line(screen,(255,255,255),(x+50,y-50),(x-50,y+50),1)


      
   
if __name__ == '__main__':
    player = X() #server is X
    server = Server()
    server.start()
    # server.start()


