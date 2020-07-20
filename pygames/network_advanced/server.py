import socket
import _thread
import sys
import pickle
from player import Player

server = "localhost"
port = 5555

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

max_conns = 2
currentPlayer = 0
s.listen(max_conns)
print("Waiting for connection, server started...")

p1 = Player(0, 225, 50, 50, RED)
p2 = Player(450, 225, 50, 50, GREEN)
players = [p1, p2]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            #print("Received: {}".format(data))
            players[player] = data
            
            if not data:
                print("NO DATA RECEIVED")
                break
            else:                
                if player == 1:
                   reply = players[0] 
                else:
                   reply = players[1]

                #print("Sending: {}".format(reply))

            if reply == "Q":
                conn.close()                
                s.close()
                break
            
            conn.sendall(pickle.dumps(reply))
        except:
            break
    
    print("Client disconected...")
    conn.close()


while True:
    if currentPlayer < max_conns:
        conn, addr = s.accept()
        print("Connected to: {}".format(addr))

        _thread.start_new_thread(threaded_client, (conn, currentPlayer))
        currentPlayer += 1
