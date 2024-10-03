#include <Arduino.h>
#include <UnicViewAD.h>

// #define Lpwm 1
// #define Rpwm 2
// #define enableL 16
// #define enableR 39
// #define tictac 4
// #define pedalInput 7
// #define pedalOutput 15
#define contaGiro 2

// variaveis de configuração PWM
// const int channel = 1;      // uint8_t
// const int frequency = 1000; // uint32_t
// const int resolution = 12;  // uint8_t

LCM Lcm(Serial2);

int girosNum;

int quantosGiros() {
  pinMode(contaGiro, INPUT_PULLDOWN);
  int giros = digitalRead(contaGiro);
  if(giros == HIGH) {
    girosNum += 1;    
  }
  return girosNum;
}

int direcao() {
  int asciiCode = Lcm.readVP(100);
  if(asciiCode == 18536) {
    Serial.print("Vp 100: Horario");
    // pinMode(enableL, OUTPUT);
    // pinMode(enableR, OUTPUT);
    // pinMode(Lpwm, OUTPUT);
    // pinMode(Rpwm, OUTPUT);
    // digitalWrite(enableL, LOW);
    // digitalWrite(enableR, HIGH);
    // digitalWrite(Lpwm, LOW);
    // digitalWrite(Rpwm, HIGH);
    // ledcAttachPin(Rpwm, channel);

  } else if (asciiCode == 16737) {
    Serial.print("Vp 100: Anti Horario");
    // ledcSetup(channel, frequency, resolution);
    // pinMode(enableL, OUTPUT);
    // pinMode(enableR, OUTPUT);
    // pinMode(Lpwm, OUTPUT);
    // pinMode(Rpwm, OUTPUT);
    // digitalWrite(enableR, LOW);
    // digitalWrite(enableL, HIGH);
    // digitalWrite(Rpwm, LOW);
    // digitalWrite(Lpwm, HIGH);
    // ledcAttachPin(Lpwm, channel);
  }

}

void setup() {
  Lcm.begin();
  Serial.begin(115200);
  Serial2.begin(115200, SERIAL_8N1, 42, 41, false, 100);
}

void loop() {
  // pinMode(7, INPUT_PULLDOWN);
  // pinMode(15, OUTPUT);
  // digitalWrite(15, HIGH);

  // int pedalValue = digitalRead(pedalInput);
  // bool pedalEnabled = pedalValue == 1;
  // if (pedalEnabled)
  // {
    
  //   Serial.print("Vp 80: ");
  //   Serial.println(Lcm.readVP(80));

  //   Serial.print("Vp 69: ");
  //   Lcm.writeVP(69, quantosGiros());
  //   Serial.println(Lcm.readVP(69));

  //   Serial.print("Vp 100: ");
  //   Serial.println(Lcm.readVP(100));

  //   // display();
  // }
  // else
  // {
  //   pinMode(7, INPUT_PULLDOWN);
  //   pinMode(15, OUTPUT);
  //   digitalWrite(enableL, LOW);
  //   digitalWrite(enableR, LOW);
  //   digitalWrite(Lpwm, LOW);
  //   digitalWrite(Rpwm, LOW);
  // }
  // direcao();

  Serial.print("Vp 80: ");
  Serial.println(Lcm.readVP(80));

  Serial.print("Vp 69: ");
  Lcm.writeVP(69, quantosGiros());
  Serial.println(Lcm.readVP(69));

  delay(300);

}