#include "TempHumidSensor.h"

#include <Arduino.h>
#include <DHT.h>

namespace
{
constexpr uint8_t DHT_PIN = 10;
constexpr uint8_t DHT_TYPE = DHT11;
constexpr unsigned long READ_INTERVAL_MS = 2000;

DHT dht(DHT_PIN, DHT_TYPE);
unsigned long lastReadMs = 0;
}

void initializeTempHumidSensor()
{
    Serial.println("Starting DHT11 temperature/humidity sensor...");
    Serial.println("DHT11 data pin: Pico GP10");

    dht.begin();

    Serial.println("DHT11 initialized!");
}

void printTempHumidReadingIfReady()
{
    const unsigned long nowMs = millis();

    if (nowMs - lastReadMs < READ_INTERVAL_MS)
    {
        return;
    }

    lastReadMs = nowMs;

    const float humidity = dht.readHumidity();
    const float temperatureC = dht.readTemperature();
    const float temperatureF = dht.readTemperature(true);

    if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF))
    {
        Serial.println("Failed to read from DHT11 sensor. Check power, ground, data on GP10, and pull-up resistor.");
        return;
    }

    Serial.print("Humidity: ");
    Serial.print(humidity, 1);
    Serial.print("%\tTemperature: ");
    Serial.print(temperatureC, 1);
    Serial.print(" C / ");
    Serial.print(temperatureF, 1);
    Serial.println(" F");
}
