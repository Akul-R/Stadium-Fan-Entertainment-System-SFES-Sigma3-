import socket
import threading
import sys

PI_IP = '127.0.0.1'
IN_PORT = 5000
OUT_PORT = 4000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', IN_PORT))

def hub_transmit():
    while True:
        msg = input("Enter command for ESP: ")
        if msg:
            sock.sendto(msg.encode(), (PI_IP, OUT_PORT))
            print(f"MESSAGE SENT TO PI ON {PI_IP}, PORT {OUT_PORT}")
            print("\n---------------------------------------------")


def hub_receive():
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            sys.stdout.write(f"\r[FROM PI]: {data.decode()}\n")
            sys.stdout.write("Enter command for ESP: ")
            sys.stdout.flush()
            print("\n---------------------------------------------")


        except Exception as e:
            print(f"RECEIVE ERROR: {e}")
            print("---------------------------------------------")

print("HUB STARTED...")
print("---------------------------------------------")

transmitter_thread = threading.Thread(target=hub_transmit, daemon=True)
transmitter_thread.start()
hub_receive()




