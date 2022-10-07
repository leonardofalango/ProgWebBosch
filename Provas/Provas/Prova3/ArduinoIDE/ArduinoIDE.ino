#include <dht.h>
#include <LiquidCrystal.h> 
#include <FirebaseESP32.h>
#include <WiFi.h>
#define WIFI_SSID "Vivo-Internet-BF17"
#define WIFI_PASSWORD "78814222"
#define FIREBASE_HOST "https://prova-98629-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "kE2sOlH3H3rQUmg1VTtqp4hSbkumeXGgyWA20DsY"
FirebaseData firebaseData;
FirebaseJson json;
dht DHT;
#define pinoLed 12
#define pinoLed1 15
#define pinoLed2 13
#define pinoLed3 2 //Led imbutido do ESP-32, e led que irá ascender quando enviar os dados
#define DHTPin A0


//LiquidCrystal lcd(19,23,18,17,16,15);   
LiquidCrystal lcd(27,26,33,32,25,14);
int count = 0;




//SETUP
void setup() {
  Serial.begin(9600); //Ligando o serial

  pinMode(DHTPin, INPUT); //Definindo o pino que vai receber as informações do ESP-32
  pinMode(pinoLed, OUTPUT);
  pinMode(pinoLed1, OUTPUT);
  pinMode(pinoLed2, OUTPUT);
  pinMode(pinoLed3, OUTPUT);
  
  //Settando o lcd
  lcd.begin(16,2);
  lcd.clear(); //Limpando qualquer coisa que estiver na tela do lcd
  lcd.setCursor(3,0);
  lcd.print("Iniciar!!!");
  delay(2000);
 
  lcd.clear();
  lcd.setCursor(3,0);
  lcd.print("Conectando");

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD); //Ligando o WIFI
  while(WiFi.status() != WL_CONNECTED){
    if (count > 3){
      count = 0;
      lcd.clear();
      lcd.setCursor(3,0);
      lcd.print("Conectando");
    }
    Serial.print(".");
    lcd.print(".");
    count = count + 1;
    delay(500);
  }
  Serial.println("Conectado!");
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  lcd.clear();
  lcd.print("Conectado!");
  
  //Settando o Firebase
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  Firebase.setReadTimeout(firebaseData, 1000 * 60);
  Firebase.setwriteSizeLimit(firebaseData, "tiny");
}

void loop(){
  //Ligando o led pois aqui começa a leitura e armazenamento de dados
  digitalWrite(pinoLed3, HIGH);
  
  //Lendo os valores de temperatura e umidade
  DHT.read11(DHTPin);
  float temp = DHT.temperature;
  int umi = DHT.humidity;
  
  //Printando os valores de temperatura e umidade no Serial
  Serial.print("Umidade: ");
  Serial.println(umi);
  Serial.print("Temperatura: ");
  Serial.println(temp);
  
  
  //Verificando a temperatura para acender os LED's corretamente
  //pinoLed <= 25ºC
  // 25ºC < pinoLed1 < 27ºC
  //pinoLed2 > 27ºC

  if (temp <= 25){
    digitalWrite(pinoLed, HIGH);
    digitalWrite(pinoLed1, LOW);
    digitalWrite(pinoLed2, LOW);
  }
  else if (temp > 25 and temp < 27){
    digitalWrite(pinoLed, LOW);
    digitalWrite(pinoLed1, HIGH);
    digitalWrite(pinoLed2, LOW);
  }
  else if (temp >= 27){
    digitalWrite(pinoLed, LOW);
    digitalWrite(pinoLed1, LOW);
    digitalWrite(pinoLed2, HIGH);
  }
  
  
  
  
  
  
  
  

  //Printando no lcd os valores lidos
  lcd.clear(); //Limpando a tela
  lcd.setCursor(0,0);
  lcd.print("Temperatura: ");
  lcd.print(temp);
  lcd.setCursor(0,1);
  lcd.print("Umidade: ");
  lcd.print(umi);
  
  //Enviando os dados para o Firebase
  json.set("/Temperatura", temp);
  json.set("/Umidade", umi);
  Firebase.updateNode(firebaseData, "/DHT", json);
  
  digitalWrite(pinoLed3, LOW); //Desligando o led pois acabou de enviar os dados


  
  //Envia dados a cada 30 segundos, por isso esse contador
  for (int i=30; i>0; i--){
    lcd.clear(); //Limpando a tela
    lcd.setCursor(0,0);
    lcd.print("Temperatura: ");
    lcd.print(temp);
    lcd.setCursor(0,1);
    lcd.print("Umidade: ");
    lcd.print(umi);
    lcd.setCursor(14,2); //Colocando quando vai ser a próxima vez que o ESP-32 irá mandar os dados
    lcd.print(i);
    delay(1000); //Loop irá se repetir 30 vezes com delay de 1 seg
  }
}
