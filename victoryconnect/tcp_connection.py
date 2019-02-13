import socket
from threading import Thread

class TCPConnection(Thread):
    def __init__(self, serverIP, serverPort, clientRef):
        Thread.__init__(self)
        self.daemon = True
        self.ip = serverIP
        self.port = serverPort
        self.client = clientRef

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s = s

        self.isConnected = False
        self.isReconnecting = True

        s.connect((self.ip, self.port))
        print("Connected!")
        self.start()

        self.isReconnecting = False
        self.reconnectAttempt = 0
        self.isConnected = True
        self.ping = -1


    def heartbeat_tick(self):

    def recv_tick(self):
        data = self.s.recv(4096)
        if not data:
            pass
        print(data)

    def run(self):
        while True:
            heartbeat_tick()
            recv_tick()
            

    def recv_heartbeat(timestamp):


    def send_packet(self, toSend):
