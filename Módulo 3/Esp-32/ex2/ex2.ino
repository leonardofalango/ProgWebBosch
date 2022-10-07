#include <LiquidCrystal.h>
const int botao = 34;
int posx, posy;
LiquidCrystal lcd(27,26,33,32,25,14);
void setup() {
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.clear();  

}

void loop() {
  int i = -1;
  for (i; i < 1; i++)
  {
    lcd.clear();
    lcd.setCursor(5,i);
    lcd.print("Subindo");
    delay(500);
    
  }
  lcd.clear();
  delay(500);
  i = -1;
  for (i; i<15;i++)
  {
    lcd.clear();
    lcd.setCursor(i,0);
    lcd.print("--->");
    delay(250);
  }

}
