#define COIN_PIN 2

float current_credit = 0.0f;

void setup() {
  Serial.begin(9600);
  
  pinMode(COIN_PIN, INPUT_PULLUP);
  
  attachInterrupt(digitalPinToInterrupt(COIN_PIN), coin_received, FALLING);

  Serial.println("Starting..");
}

void loop() {

}

void coin_received() {
  current_credit += 1.0;
  Serial.println("--------!");
  Serial.print("Current credit: ");
  Serial.println(current_credit);
  Serial.println("--------!");
}

