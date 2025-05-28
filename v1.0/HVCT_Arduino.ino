//HVCT_Arduino v1.0 - HoneyFoxQueen
#include <IRremote.hpp> //Developed by Armin Joachimsmeyer
#include <Arduino.h>

#define IR_RECEIVE_PIN 2
#define IR_DELAY 200
#define KEY_DELAY 400 




void setup() {
	Serial.begin(9600);
	while (!Serial);
	IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);
}

int cache_key = 0;
int pressed_key = 0;
unsigned long pressed_time = 0;

void loop(){

	if(IrReceiver.decode()){
		
		IrReceiver.resume();

		pressed_key = IrReceiver.decodedIRData.command
		if(pressed_key != 0x0){
			if(pressed_key == cache_key){
				if(pressed_time == 0){pressed_time = millis();} //start timer
				if((millis() - pressed_time) >= KEY_DELAY){
					Serial.println(pressed_key);
				}
				
			}else{
				if(pressed_time != 0){pressed_time = 0;}
				Serial.println(pressed_key);
			}
			cache_key = pressed_key;
		}
	}else{
		cache_key = 0;
	}
	delay(IR_DELAY);
}