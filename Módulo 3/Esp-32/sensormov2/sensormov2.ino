#define led 2
#define sensor 15
#define saida 4
bool mov;
void setup() {
  pinMode(led, OUTPUT);
  pinMode(sensor, INPUT);
  pinMode(saida, OUTPUT);

}

void loop() {
  mov = digitalRead(sensor);
  if (mov){
    digitalWrite(led, HIGH);
    digitalWrite(saida, HIGH);                                                                           
    }
  else{
    digitalWrite(saida,HIGH);
    digitalWrite(led, LOW);
    }
}
