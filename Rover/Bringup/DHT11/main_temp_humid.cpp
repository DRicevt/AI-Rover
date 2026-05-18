#include <Arduino.h>

#include "TempHumidSensor.h"

void setup()
{
    Serial.begin(115200);
    delay(2000);

    initializeTempHumidSensor();
}

void loop()
{
    printTempHumidReadingIfReady();
    delay(50);
}
