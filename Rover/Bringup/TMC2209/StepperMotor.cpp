#include "StepperMotor.h"

#include <Arduino.h>

namespace
{
constexpr uint8_t DIR_PIN = 6;
constexpr uint8_t STEP_PIN = 7;
constexpr uint8_t EN_PIN = 8;

constexpr unsigned long STEP_INTERVAL_US = 700;
constexpr unsigned long DIRECTION_INTERVAL_MS = 3000;

bool directionClockwise = true;
bool stepState = LOW;
unsigned long lastStepUs = 0;
unsigned long lastDirectionChangeMs = 0;
}

void initializeStepperMotor()
{
    pinMode(DIR_PIN, OUTPUT);
    pinMode(STEP_PIN, OUTPUT);
    pinMode(EN_PIN, OUTPUT);

    digitalWrite(DIR_PIN, directionClockwise ? HIGH : LOW);
    digitalWrite(STEP_PIN, LOW);
    digitalWrite(EN_PIN, LOW);

    lastStepUs = micros();
    lastDirectionChangeMs = millis();

    Serial.println("TMC2209 NEMA 17 bring-up initialized");
    Serial.println("DIR=GP6 STEP=GP7 EN=GP8");
}

void runStepperMotor()
{
    const unsigned long nowMs = millis();
    if (nowMs - lastDirectionChangeMs >= DIRECTION_INTERVAL_MS)
    {
        directionClockwise = !directionClockwise;
        digitalWrite(DIR_PIN, directionClockwise ? HIGH : LOW);
        lastDirectionChangeMs = nowMs;

        Serial.print("Direction: ");
        Serial.println(directionClockwise ? "clockwise" : "counterclockwise");
    }

    const unsigned long nowUs = micros();
    if (nowUs - lastStepUs >= STEP_INTERVAL_US)
    {
        stepState = !stepState;
        digitalWrite(STEP_PIN, stepState);
        lastStepUs = nowUs;
    }
}
