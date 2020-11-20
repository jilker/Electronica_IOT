import socket
import pickle
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65435        # The port used by the server

def recibir(socket,size_data):
    recv_data=pickle.loads(socket.recv(size_data))
    return recv_data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    actions = recibir(s,1024)
    s.shutdown(socket.SHUT_RDWR)
    s.close()
print(actions)
#print('Received', repr(data))