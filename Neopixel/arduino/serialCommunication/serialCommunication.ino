#include "FastLED.h"

#define VALUE_SIZE 5
#define NUM_LEDS 24
#define DATA_PIN 3

char c;
String command;
String values[VALUE_SIZE];

CRGB leds[NUM_LEDS];

void setup() {
  Serial.begin(115200);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
}

void turnOn(){
  for(int i = 0; i <= NUM_LEDS; i++){
    leds[i] = CRGB::Blue;
    FastLED.show();
    delay(50);
  }
}

void turnOff(){
  for(int i = 0; i <= NUM_LEDS; i++){
    leds[i] = CRGB::Black;
    FastLED.show();
    delay(50);
  }
}

void turnLed(int pos, int r, int g, int b){
  leds[pos].red = r;
  leds[pos].green = g;
  leds[pos].blue = b;
  FastLED.show();
}

void echo(String value){
  Serial.print("responding-to-");
  Serial.println(value);
}

void parseCommand(String com) {
  String middle; //buffer

  middle = com; //1-255-0-99

  for(int i = 0; i < VALUE_SIZE; i++){
    values[i] = middle.substring(0, middle.indexOf("-"));
    middle = middle.substring(middle.indexOf("-") + 1);
  }

  if(values[0] == "echo"){
    echo(values[1]);
  }else
  if(values[0] == "led"){
    turnLed(values[1].toInt(), values[2].toInt(), values[3].toInt(), values[4].toInt());
  }

  com = "";
}

void serialEvent(){
  if (Serial.available()) {
    c = Serial.read();
    if (c == '\n') {
      parseCommand(command);
      command = "";
      Serial.flush();
    }
    else {
      command += c;
    }
  }
}

void loop() {
  
}
