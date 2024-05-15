#include <Encoder.h>

#define RED_PIN 9
#define GREEN_PIN 10
#define BLUE_PIN 11
#define PHOTO_RESISTOR_PIN A5
#define ENCODER_CLK_PIN 12
#define ENCODER_DT_PIN 13
#define ENCODER_SW_PIN A3

Encoder encoder(ENCODER_CLK_PIN, ENCODER_DT_PIN);

int maxLED = 0;
int currentHue = 0;
int encoderPosition = 0;


void setup() {
  Serial.begin(9600);
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(BLUE_PIN, OUTPUT);
  pinMode(ENCODER_SW_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENCODER_SW_PIN), saveMaxLED, FALLING);
}

void loop() {
  int newEncoderPosition = encoder.read()*3;
  static int encoderPosition = 0;

  if (newEncoderPosition != encoderPosition) {
    
    if(newEncoderPosition > encoderPosition){
      if(currentHue < 360) currentHue+=1;
      else currentHue=1;
    }else{
      if(currentHue > 0) currentHue-=1;
      else currentHue=359;
    }
    encoderPosition = newEncoderPosition;
    setRGBColor(currentHue);
  }
}

void setRGBColor(int hue) {
  int saturation = 255; // You can adjust the saturation and brightness as needed
  int brightness = 255;
  
  // Convert HSV to RGB
  int r, g, b;
  HsvToRgb(hue, saturation, brightness, r, g, b);

  analogWrite(RED_PIN, r);
  analogWrite(GREEN_PIN, g);
  analogWrite(BLUE_PIN, b);
}

void HsvToRgb(int h, int s, int v, int &r, int &g, int &b) {
  // Ensure the input values are within the expected range
  h = constrain(h, 0, 359);
  s = constrain(s, 0, 255);
  v = constrain(v, 0, 255);

  int i = h / 60;
  int f = (h % 60) * 255 / 60;
  int p = (v * (255 - s)) / 255;
  int q = (v * (255 - s * f / 255)) / 255;
  int t = (v * (255 - s * (255 - f) / 255)) / 255;

  switch (i) {
    case 0:
      r = v;
      g = t;
      b = p;
      break;
    case 1:
      r = q;
      g = v;
      b = p;
      break;
    case 2:
      r = p;
      g = v;
      b = t;
      break;
    case 3:
      r = p;
      g = q;
      b = v;
      break;
    case 4:
      r = t;
      g = p;
      b = v;
      break;
    case 5:
      r = v;
      g = p;
      b = q;
      break;
  }
}

void saveMaxLED() {
  maxLED = analogRead(PHOTO_RESISTOR_PIN);
  Serial.write(maxLED);
  
}
