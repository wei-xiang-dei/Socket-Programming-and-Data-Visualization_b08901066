import socket 
import json
import numpy as np
import matplotlib.pyplot as plt


HOST = "192.168.161.17"
PORT = 6969
print("Starting server at: ", (HOST, PORT))
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            print("Received from socket server:", data,"\n")
            print("data.count(\"{\"):",data.count('{'),"\n")

            if (data.count('{') != 1):
                # Incomplete data are received.
                choose = 0
                buffer_data = data.split('}')
                while buffer_data[choose][0] != '{':
                    choose += 1
                data = buffer_data[choose] + '}'
            print("accessed data:", data,"\n")
            obj = json.loads(data)
            
            t = obj['s']
            plt.scatter(t, obj['x'], c='blue') # x, y, z, gx, gy, gz
            plt.xlabel("sample num")
            plt.pause(0.0001)
            plt.scatter(t,obj['y'],c='yellow')
            plt.xlabel("sample num")
            plt.pause(0.0001)
            plt.scatter(t,obj['z'],c='green')
            plt.xlabel("sample num")
            plt.pause(0.0001)

            if (data.count('{') != 1):
                # Incomplete data are received.
                choose = 0
                buffer_data = data.split('}')
                while buffer_data[choose][0] != '{':
                    choose += 1
                data = buffer_data[choose] + '}'
           