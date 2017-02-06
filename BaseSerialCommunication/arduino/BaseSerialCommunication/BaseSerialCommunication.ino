#define VALUE_SIZE 3
char c;
String command;
String values[VALUE_SIZE];

void echo(String value){
  Serial.print("responding-to-");
  Serial.println(value);
}

void parseCommand(String com) {
  String middle;
  middle = com;

  for(int i = 0; i < VALUE_SIZE; i++){
    values[i] = middle.substring(0, middle.indexOf("-"));
    middle = middle.substring(middle.indexOf("-") + 1);
  }

  if(values[0] == "echo"){
    echo(values[1]);
  }
}

void setup() {
  Serial.begin(115200);
}

void loop() {
  
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
