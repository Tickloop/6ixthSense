int red = 7;
int green = 6;
int blue = 5;
int state = 0;
int tx = 1;
int rx = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(blue, OUTPUT);
  allLOW();
  pinMode(tx, OUTPUT);
  pinMode(rx, INPUT);
}

void loop() {
  int i =0;
  int m=0;
  delay(500);
  if(Serial.available() > 0){
    state = Serial.read();
  }
  
  if(state == '7'){
    allLOW();
    digitalWrite(red, LOW);
    Serial.println("LED: RED");
    state = 0;
  }
  else if(state == '6'){
    allLOW();
    digitalWrite(green, LOW);
    Serial.println("LED: GREEN");
    state = 0;
  }
  else if(state == '5'){
    allLOW();
    digitalWrite(blue, LOW);
    Serial.println("LED: BLUE");
    state = 0;
  }else if(state == '0'){
    allLOW();
    state = 0;
  }
}

void allLOW(){
  digitalWrite(red, HIGH);
  digitalWrite(green, HIGH);
  digitalWrite(blue, HIGH);
}
