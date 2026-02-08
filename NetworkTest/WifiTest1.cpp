#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = "Akul's Pixel 6";
const char* password = "Akul12345";

WiFiUDP udp;
unsigned int localPort = 80; // The port your Python script is hitting
char packetBuffer[255]; 

void setup() {
  Serial.begin(115200);
  
  // 1. Correct the addresses to match the 192.168.43.x range
  IPAddress local_IP(10, 22, 162, 200); 
  IPAddress gateway(10, 22, 162, 89);    // Android Hotspot default
  IPAddress subnet(255, 255, 255, 0);
  IPAddress primaryDNS(8, 8, 8, 8);
  
  // 2. THIS LINE IS CRITICAL: You must actually apply the config!
  if (!WiFi.config(local_IP, gateway, subnet, primaryDNS)) {
    Serial.println("STA Failed to configure");
  }
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) { 
    delay(500); 
    Serial.print("."); 
  }

  udp.begin(localPort);
  Serial.print("\nActual IP assigned: ");
  Serial.println(WiFi.localIP()); // Verify it actually set to .200
  Serial.printf("Listening for UDP on port %d\n", localPort);
}

void loop() {
  int packetSize = udp.parsePacket();
  if (packetSize) {
    int len = udp.read(packetBuffer, 255);
    if (len > 0) packetBuffer[len] = 0; // Null terminate the string
    Serial.print("Received: ");
    Serial.println(packetBuffer);
  }
}
