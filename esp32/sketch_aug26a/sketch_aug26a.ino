#include <WiFi.h> // Biblioteca para ESP32
#include <WiFiManager.h> // Biblioteca WiFiManager

void setup() {
  Serial.begin(115200);

  // Cria uma instância do WiFiManager
  WiFiManager wm;

  // Tenta conectar à rede configurada previamente
  if (!wm.autoConnect("AutoConnectAP")) {
    Serial.println("Falha ao conectar. Reiniciando...");
    delay(3000);
    ESP.restart();
  }

  // Conectado com sucesso
  Serial.println("Conectado com sucesso!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Seu código aqui
}
