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
#define pedalInput 7
#define pedalOutput 15
#define limitSwitch 40

#define RS 3
#define E 46
#define D4 9
#define D5 35
#define D6 45
#define D7 37

LiquidCrystal lcd(RS, E, D4, D5, D6, D7);

// variaveis de configuração PWM
const int channel = 1;      // uint8_t
const int frequency = 1000; // uint32_t
const int resolution = 12;  // uint8_t

int direction;
uint16_t turns = 0;
int potentiometerValue;
Tipo_MediaMovel mediaPotentiometer;

int updateDirection()
{
  pinMode(tictac, INPUT_PULLDOWN);
  int button = digitalRead(tictac);
  if (button == LOW)
  {
    direction = 1;
  }
  else
  {
    direction = 0;
  }
  return direction;
}

void updateScreen()
{
  lcd.clear();
  lcd.print("vel:");

  lcd.print(potentiometerValue * 100 / 4095);
  lcd.print("%");

  lcd.setCursor(9, 0);
  if (!direction)
  {
    lcd.print("dir:AH");
  }
  else
  {
    lcd.print("dir:H");
  }

  lcd.setCursor(0, 1);
  lcd.print("Voltas:");
  int limitSwitchValue = digitalRead(limitSwitch);
  if (limitSwitchValue == 1.)
  {
    turns++;
  }
  lcd.print(turns);
}

uint16_t CalculaMediaMovel(Tipo_MediaMovel *pMediaMovel, uint16_t NovaAmostra)
{
  pMediaMovel->Soma += NovaAmostra - pMediaMovel->Fila[pMediaMovel->IndexFila];
  pMediaMovel->Fila[pMediaMovel->IndexFila] = NovaAmostra;
  pMediaMovel->IndexFila++;
  if (pMediaMovel->IndexFila >= Amostras)
    pMediaMovel->IndexFila = 0;

  return pMediaMovel->Soma / Amostras;
}

void rotation()
{
  if (direction == 0)
  {
    ledcSetup(channel, frequency, resolution);
    pinMode(enableL, OUTPUT);
    pinMode(enableR, OUTPUT);
    pinMode(Lpwm, OUTPUT);
    pinMode(Rpwm, OUTPUT);
    digitalWrite(enableR, LOW);
    digitalWrite(enableL, HIGH);
    digitalWrite(Rpwm, LOW);
    digitalWrite(Lpwm, HIGH);
    ledcAttachPin(Lpwm, channel);
  }
  else
  {
    ledcSetup(channel, frequency, resolution);
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

void display()
{
  ledcWrite(channel, potentiometerValue);
}

void setup()
{
  Serial.begin(115200);
  lcd.begin(16, 2);
}

void loop()
{
  potentiometerValue = CalculaMediaMovel(&mediaPotentiometer, analogRead(potentiometer));
  display();
  pinMode(7, INPUT_PULLDOWN);
  pinMode(15, OUTPUT);
  digitalWrite(15, HIGH);
  int pedalValue = digitalRead(pedalInput);
  updateDirection();
  updateScreen();
  rotation();
  if (pedalValue == 1)
  {
    Serial.println(potentiometerValue);

    // display();
  }
  else
  {
    pinMode(7, INPUT_PULLDOWN);
    pinMode(15, OUTPUT);
    digitalWrite(enableL, LOW);
    digitalWrite(enableR, LOW);
    digitalWrite(Lpwm, LOW);
    digitalWrite(Rpwm, LOW);
  }
  delay(15);
}