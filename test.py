from victoryconnect.tcp_connection import TCPConnection

con = TCPConnection("127.0.0.1",5000,None)

con.connect()

while True:
    pass