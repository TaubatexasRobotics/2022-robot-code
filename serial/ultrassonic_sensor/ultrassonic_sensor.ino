
#define echoPin 8 
#define trigPin 7 

// defines variables
long duration; // variable for the duration of sound wave travel
int distance; // variable for the distance measurement
int media;

void setup() {
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT
  pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT
  Serial.begin(9600); // // Serial Communication is starting with 9600 of baudrate speed

}

void loop() {
  
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);

  distance = duration * 0.034 / 2; 
  
  Serial.println(distance);
}