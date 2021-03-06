# Import socket module 
import socket 
FORMAT = 'utf-8'

def Main(): 
    # local host IP '127.0.0.1' 
    host = '127.0.0.1'
  
    # Define the port on which you want to connect 
    port = 12345
  
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  
    # connect to server on local computer 
    s.connect((host,port)) 
  
    # message you send to server
    
    
    while True:
        with open(r'.\fixmessages.csv', 'r') as f:
            for line in f:
                if line == ',0':
                    continue
                print('sending to server', line[3:].encode(FORMAT).decode(FORMAT))
                s.send(line[2:].encode(FORMAT))
                data = s.recv(4068)
                print('Received from the server :',str(data.decode(FORMAT))) 
            f.close()
    
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 
