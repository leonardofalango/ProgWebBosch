#include <FirebaseESP32.h>
#include <WiFi.h>
#include "dht.h"

#define pino 4
dht DHT;

#define WIFI_SSID "Vivo-Internet-BF17"
#define WIFI_PASSWORD "78814222"


#define FIREBASE_HOST "https://espfirebaseteste-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "FyLE6hKH97Lw6dWObGIn8p8fSBZlK5eYH7GAd9kv"
FirebaseData firebaseData;
FirebaseJson json;

void setup() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.begin(115200);
  
  while(WiFi.status() != WL_CONNECTED){
  Serial.print(".");
    delay(200);
  }
  Serial.println("Conectado!");
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  Firebase.setReadTimeout(firebaseData, 1000 * 60);
  Firebase.setwriteSizeLimit(firebaseData, "tiny");

}

void loop() {
  DHT.read11(pino);
  Serial.print("Umidade: ");
  Serial.println(DHT.humidity);
  Serial.print("Temperatura: ");
  Serial.println(DHT.temperature, 0);
  delay(500);
  json.set("/temperatura", t);
  json.set("/umidade", h);
  Firebase.updateNode(firebaseData, "/Sensor", json);
  delay(5000);
  
}
