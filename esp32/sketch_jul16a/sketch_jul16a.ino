#define PWM1 16 //R_PWM
#define PWM2 15 //L_PWM
#define PO 7    //L_EN

void setup() {
  pinMode(PWM1, OUTPUT);
  pinMode(PWM2, OUTPUT);
  pinMode(PO, OUTPUT);
  digitalWrite(PO, LOW);
}

void loop() {
  
  analogWrite(PWM1, 255);
  analogWrite(PWM2, 0);
  delay(2000);
}
