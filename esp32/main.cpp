#include <Arduino.h>
#include <LiquidCrystal.h>
#include "main.h"

#define LedPlate 17 
#define potentiometer 5 
#define Lpwm 1 
#define Rpwm 2 
#define enableL 16 
#define enableR 39 
#define tictac 4 

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

int direction;
uint8_t voltas = 0;
int pot;
Tipo_MediaMovel mediaPot;


void start(){
  
}

int updateDirection(){
  pinMode(tictac, INPUT_PULLDOWN);
  int button = digitalRead(tictac);
  if (button == LOW){
    direction = 1;
    Serial.println("BOTAO PRESSIONADO");
  } else {
    direction = 0;
    Serial.println("BOTAO DESPRESSIONADO");
  }
  return direction;
}

void updateScreen(){
  lcd.clear();
  lcd.print("vel:");

  lcd.print(pot * 100 / 4095);
  lcd.print("%");
  
  lcd.setCursor(9, 0);
  if (!direction){
    lcd.print("dir:AH");
  } else { 
    lcd.print("dir:H");
  }

  lcd.setCursor(0, 1);
  lcd.print("Voltas:");
  lcd.print(direction);
}

uint16_t CalculaMediaMovel(Tipo_MediaMovel *pMediaMovel, uint16_t NovaAmostra)
{
	pMediaMovel->Soma += NovaAmostra - pMediaMovel->Fila[pMediaMovel->IndexFila];
	pMediaMovel->Fila[pMediaMovel->IndexFila] = NovaAmostra;
	pMediaMovel->IndexFila++;
	if(pMediaMovel->IndexFila >= Amostras)
		pMediaMovel->IndexFila = 0;

	return pMediaMovel->Soma/Amostras;
} 

void rotation() {
  if (direction == 0){
    ledcSetup(channel, freq, resolution);  
    pinMode(enableL, OUTPUT);
    pinMode(enableR, OUTPUT);
    pinMode(Lpwm, OUTPUT);
    pinMode(Rpwm, OUTPUT);
    digitalWrite(enableR, LOW);
    digitalWrite(enableL, HIGH);
    digitalWrite(Rpwm, LOW);
    digitalWrite(Lpwm, HIGH);
    ledcAttachPin(Lpwm, channel);
  } else {
    ledcSetup(channel, freq, resolution);  
    pinMode(enableL, OUTPUT);
    pinMode(enableR, OUTPUT);
    pinMode(Lpwm, OUTPUT);
    pinMode(Rpwm, OUTPUT);
    digitalWrite(enableL, LOW);
    digitalWrite(enableR, HIGH);
    digitalWrite(Lpwm, LOW);
    digitalWrite(Rpwm, HIGH);
    ledcAttachPin(Rpwm, channel);
  } 
}

void setup(){
  Serial.begin(115200);
  
  
  
  lcd.begin(16,2);
}
 
void loop(){
  start();
  



  pot = CalculaMediaMovel(&mediaPot, analogRead(potentiometer));

  ledcWrite(channel, pot);
  Serial.println(pot);

  rotation();

  updateDirection();
  updateScreen();
  voltas++;

  delay(20);
}