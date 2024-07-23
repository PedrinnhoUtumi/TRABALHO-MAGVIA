#include <Arduino.h>
#include <LiquidCrystal.h>

#define LedPlate 17 
#define potentiometer 5 
#define Lpwm 1 
#define Rpwm 2 
#define enable 16 

#define RS 3 
#define E 46 
#define D4 9 
#define D5 35 
#define D6 45 
#define D7 37 

LiquidCrystal lcd(RS, E, D4, D5, D6, D7);

//variaveis de configuração PWM
const int channel = 1; //uint8_t
const int freq = 1000; //uint32_t
const int resolution = 12; //uint8_t

int direction = 1;
uint8_t voltas = 0;
int pot;

void update_screen(){
  lcd.clear();
  lcd.print("v: ");
  lcd.print(pot);
  lcd.setCursor(8, 0);
  if (!direction){
    lcd.print("S: AH");
  } else { 
    lcd.print("S: H");
  }

  lcd.setCursor(0, 1);
  lcd.print("Voltas: ");
  lcd.print(voltas);
}

void setup(){
  Serial.begin(115200);
  pinMode(enable, OUTPUT);
  pinMode(Rpwm, OUTPUT);
  digitalWrite(enable, HIGH);
  digitalWrite(Rpwm, LOW);
  ledcSetup(channel, freq, resolution);  
  ledcAttachPin(Lpwm, channel);
  
  lcd.begin(16,2);
}
 
void loop(){
  pot = analogRead(potentiometer);
  ledcWrite(channel, pot);
  Serial.println(pot);

  update_screen();
  voltas++;
  
  delay(100);
}