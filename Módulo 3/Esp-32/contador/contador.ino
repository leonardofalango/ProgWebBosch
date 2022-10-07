#include <LiquidCrystal.h>

const int botao = 34;
int button;
int contador = 0;
LiquidCrystal lcd(27,26,33,32,25,14);
void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  pinMode(botao, INPUT);
  button = 0;

}

void loop() {
  button = digitalRead(botao);
  Serial.println(button);
  if (button == 0)
  {
    contador ++;
    lcd.clear();
    lcd.setCursor(7,0);
    lcd.print(contador);
    if (contador > 10){
    lcd.clear();
    contador = 0;
    lcd.setCursor(7,0);
    lcd.print(contador);}
    delay(250);
  }
}
