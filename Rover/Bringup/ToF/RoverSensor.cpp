#include "RoverSensor.h"

#include <Arduino.h>
#include <SparkFun_VL53L5CX_Library.h>
#include <Wire.h>

SparkFun_VL53L5CX sensor;
VL53L5CX_ResultsData data;

void initializeSensor()
{
    Serial.println("Starting sensor...");

    Wire.begin();

    if (!sensor.begin())
    {
        Serial.println("Sensor failed!");
        Serial.println("Check VIN, GND, SDA on GP0, SCL on GP1, and 3.3 V I2C pull-ups.");
        while (1);
    }

    Serial.println("Sensor initialized!");

    sensor.setResolution(8 * 8);      // 64 zones
    sensor.setRangingFrequency(10);   // 10 Hz
    sensor.startRanging();

    Serial.println("Ranging started!");
}

void printDistanceGridIfReady()
{
    if (sensor.isDataReady())
    {
        if (sensor.getRangingData(&data))
        {
            Serial.println("Distance Grid (mm):");

            for (int i = 0; i < 64; i++)
            {
                Serial.print(data.distance_mm[i]);
                Serial.print("\t");

                if ((i + 1) % 8 == 0)
                    Serial.println();
            }

            Serial.println("-----------------------");
        }
    }
}
