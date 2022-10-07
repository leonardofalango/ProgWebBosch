#include "dht.h"
#define pinoLed 12
#define pinoLed1 15
#define pinoLed2 13
#define pinoLed3 2
#define pino A0
dht DHT;
void setup()
{
  pinMode(pinoLed, OUTPUT);
  pinMode(pinoLed1, OUTPUT);
  pinMode(pinoLed2, OUTPUT);
  pinMode(pinoLed3, OUTPUT);
  digitalWrite(pinoLed, HIGH);
  digitalWrite(pinoLed1, HIGH);
  digitalWrite(pinoLed2, HIGH);
  digitalWrite(pinoLed3, HIGH);
}

void loop()
{

}
