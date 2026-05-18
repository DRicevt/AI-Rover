#include <Arduino.h>

#include "RoverSensor.h"

void setup()
{
    Serial.begin(115200);
    delay(3000);

    initializeSensor();
}

void loop()
{
    printDistanceGridIfReady();
    delay(50);
}
