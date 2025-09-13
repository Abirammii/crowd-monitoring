const int greenLED = 7;  // LED for normal condition
const int redLED = 6;    // LED for high crowd alert
const int buzzer = 9;    // Buzzer connected to pin 9
char data;

void setup() {
    pinMode(greenLED, OUTPUT);
    pinMode(redLED, OUTPUT);
    pinMode(buzzer, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        data = Serial.read();

        if (data == '1') {
            digitalWrite(greenLED, HIGH); // Turn on Green LED
            digitalWrite(redLED, LOW);    // Turn off Red LED
            digitalWrite(buzzer, HIGH);   // Turn on buzzer
            delay(1000);                  // Buzzer on for 1 sec
            digitalWrite(buzzer, LOW);    // Turn off buzzer
        } else {
            digitalWrite(greenLED, LOW);
            digitalWrite(redLED, HIGH);   // Turn on Red LED
            digitalWrite(buzzer, LOW);    // Ensure buzzer is off
        }
    }
}
