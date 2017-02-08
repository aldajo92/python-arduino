#include "FastLED.h"

#define VALUE_SIZE 3
#define NUM_LEDS 144
#define DATA_PIN 3

int charbuffer = 0;
int offsetBuffer = 0;

const CRGB customColor[] = 
  {
    CRGB(0, 0, 0),
    CRGB(0, 255, 0),
    CRGB(255, 255, 0),
    CRGB(0, 0, 255),
    CRGB(255, 0, 255),
    CRGB(0, 255, 255)
  };

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
  }
  FastLED.show();
}

void turnLed(String value, int offset){
  for(int i=0; i<value.length(); i++){
    charbuffer = (int) value[i] - 48;
    leds[i + offset] = customColor[charbuffer];
  }
}

void echo(String value){
  Serial.print("responding-to-");
  Serial.println(value);
}

void parseCommand(String com) {
  String middle; //buffer

  middle = com;

  for(int i = 0; i < VALUE_SIZE; i++){
    values[i] = middle.substring(0, middle.indexOf("-"));
    middle = middle.substring(middle.indexOf("-") + 1);
  }

  if(values[0] == "echo"){
    echo(values[1]);
  }else
  if(values[0] == "led"){
    offsetBuffer = values[1].toInt();
    turnLed(values[2], offsetBuffer);
  }else
  if(values[0] == "update"){
    FastLED.show();
    Serial.flush();
  }else
  if(values[0] == "off"){
    turnOff();
  }

  com = "";
}

void aserialEvent(){
  if (Serial.available()) {
    c = Serial.read();
    if (c == '\n') {
      parseCommand(command);
      command = "";
    }
    else {
      command += c;
    }
  }
}

void loop() {
  if (Serial.available()) {
    c = Serial.read();
    if (c == '\n') {
      parseCommand(command);
      command = "";
    }
    else {
      command += c;
    }
  }
}
