#include <Arduino.h>

#include "StepperMotor.h"

void setup()
{
    Serial.begin(115200);
    delay(2000);

    initializeStepperMotor();
}

void loop()
{
    runStepperMotor();
}
