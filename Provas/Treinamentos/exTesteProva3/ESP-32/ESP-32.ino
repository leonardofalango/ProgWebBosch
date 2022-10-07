#include <LiquidCrystal.h>
#define pinoSensor A0
#define pinoSensorGas A7
#define pinoLed 12
#include <FirebaseESP32.h>
#include <WiFi.h>
#include "dht.h"
dht DHT;

#define WIFI_SSID "Vivo-Internet-BF17"
#define WIFI_PASSWORD "78814222"


#define FIREBASE_HOST "https://extesteprova-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "uBThbpjrMwVmf5XqR4uL5lUVU4hDhzHHfEC935yB"
FirebaseData firebaseData;
FirebaseJson json;
  
LiquidCrystal lcd(27,26,33,32,25,14);
void setup() {
  Serial.begin(9600); //Ligando o serial
  //Settando o lcd
  lcd.begin(16,2);
  lcd.clear();
  lcd.setCursor(3,0);
  lcd.print("Iniciar!!!");
  delay(2000);



  lcd.clear();
  lcd.setCursor(3,0);
  lcd.print("Conectando");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD); //Ligando o WIFI
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    lcd.print(".");
    delay(500);
  }
  Serial.println("Conectado!");
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());

  //Settando os pinos que iremos usar
  pinMode(pinoSensor, INPUT);
  pinMode(pinoLed, OUTPUT);
  digitalWrite(pinoLed, LOW);


  //Settando o Firebase
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  Firebase.setReadTimeout(firebaseData, 1000 * 60);
  Firebase.setwriteSizeLimit(firebaseData, "tiny");

}

void loop() {
  int gas = analogRead(pinoSensorGas);
  digitalWrite(pinoLed, HIGH);
  lcd.clear();
  int luminosidade = analogRead(pinoSensor);
  Serial.println(luminosidade);
  int luminosidade_pct = map(luminosidade, 0, 4095, 0, 100);
  Serial.println(luminosidade_pct);

  lcd.clear();
  lcd.setCursor(0,1);
  lcd.print("Luz: ");
  lcd.print(luminosidade_pct);

  json.set("/Luminosidade", luminosidade_pct);
  json.set("/analogLuminosidade", luminosidade);
  Firebase.updateNode(firebaseData, "/LumiSensor", json);
  digitalWrite(pinoLed, LOW);

  
  for (int i = 5; i > 0; i--){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nova Leitura: ");
    lcd.print(i);
    lcd.setCursor(0,1);
    lcd.print("Luz: ");
    lcd.print(luminosidade_pct);
    delay(950);
  }
  digitalWrite(pinoLed, HIGH);
  lcd.clear();
  lcd.setCursor(0,1);
  lcd.print("Gás: ");
  lcd.print(gas);
  
  json.set("/Gás", gas);
  Firebase.updateNode(firebaseData, "/LumiSensor", json);
  
  delay(500);
  digitalWrite(pinoLed, LOW);
  for (int i = 5; i > 0; i--){
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Nova Leitura: ");
    lcd.print(i);
    lcd.setCursor(0,1);
    lcd.print("Gas: ");
    lcd.print(gas);
    delay(950);
  }
}
