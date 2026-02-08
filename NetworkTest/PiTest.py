import socket
import threading

#hub ports
DATA_TO_HUB_PORT = 5000
DATA_FROM_HUB_PORT = 4000

#esp ports
DATA_TO_ESP_PORT = 90
DATA_FROM_ESP_PORT = 80

esp_ip = '10.22.162.200'
hub_ip = '127.0.0.1'

ack_msg = "PI-ACK"

#this listens to the hub, sends an ack msg back to hub and forwards msg to esp
def hub_listener():
    # sockA listens to the hub
    sockA = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockA.bind(('0.0.0.0', DATA_FROM_HUB_PORT))

    while True:
        #receives msg from hub
        data, addr = sockA.recvfrom(1024)
        print(f"PI RECEIVED FROM HUB: {data.decode()}")
        print(addr)

        #acknowleding hub that data was received
        sockA.sendto(ack_msg.encode(), (hub_ip, DATA_TO_HUB_PORT))

        try:
            # Forwarding the data to the ESP32
            sockA.sendto(data, (esp_ip, DATA_TO_ESP_PORT))
            print(f"Forwarded to ESP at {esp_ip} on port {DATA_TO_ESP_PORT}")
        except Exception as e:
            print(f"Forwarding failed: {e}")

        print("---------------------------------------------")

#this listens to esp, sends ack msg back to esp and forwards msg to hub
def esp_listener():
    # sockB listens to the esp
    sockB = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sockB.bind(('0.0.0.0', DATA_FROM_ESP_PORT))

    while True:
        # receives msg from hub
        data, addr = sockB.recvfrom(1024)
        print(f"PI RECEIVED FROM ESP: {data.decode()}")
        print(addr)

        # acknowleding esp that data was received
        if(data.decode() != "ESP-ACK"):
            sockB.sendto(ack_msg.encode(), (esp_ip, DATA_TO_ESP_PORT))

        try:
            # Forwarding the data to the HUB
            sockB.sendto(data, (hub_ip, DATA_TO_HUB_PORT))
            print(f"Forwarded to HUB at {hub_ip} on port {DATA_TO_HUB_PORT}")
        except Exception as e:
            print(f"Forwarding failed: {e}")

        print("---------------------------------------------")


print("Pi Simulator Started...")
print("---------------------------------------------")

hub_listen_thread = threading.Thread(target=hub_listener, daemon=True)
esp_listen_thread = threading.Thread(target=esp_listener, daemon=True)

hub_listen_thread.start()
esp_listen_thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nSHUTTING DOWN PI SIMULATOR...")