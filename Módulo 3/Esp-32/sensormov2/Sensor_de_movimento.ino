#define led 2
const int sensor = 4;
bool mov;
void setup() {
  pinMode(led,OUTPUT);
  pinMode(sensor, INPUT);
}

void loop() {
  mov = digitalRead(sensor);
  if (mov){
    digitalWrite(led, HIGH);
    
  }
  else{
    digitalWrite(led, LOW);
  }
}
