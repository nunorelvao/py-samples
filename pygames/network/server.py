import socket
import _thread
import sys

server = "localhost"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

max_conns = 2
currentPlayer = 0
s.listen(max_conns)
print("Waiting for connection, server started...")


def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1]) 

pos = [(0, 0), (100, 100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            #print("Received: {}".format(data))
            pos[player] = data
            
            if not data:
                print("NO DATA RECEIVED")
                break
            else:                
                if player == 1:
                   reply = pos[0] 
                else:
                   reply = pos[1]

                #print("Sending: {}".format(reply))

            if reply == "Q":
                conn.close()                
                s.close()
                break
            
            conn.sendall(str.encode(make_pos(reply)))
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
