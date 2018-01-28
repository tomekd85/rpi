from dht11 import consts
import time

class WeatherLogger:
    __instance = None

    def __new__(cls):
        if WeatherLogger.__instance is None:
            WeatherLogger.__instance = object.__new__(cls)
        return WeatherLogger.__instance

    def __init__(self):
        self.temperature_logger = open(consts.Weather.TEMPERATURE_LOG_FILE, "a")
        self.humidity_logger = open(consts.Weather.HUMIDITY_LOG_FILE, "a")

    def log_temperature(self, value):
        print("{}|{}|C degrees".format(time.strftime("%d.%m.%Y %H:%M%:%S"), value), file=self.temperature_logger)

    def log_humidity(self, value):
        print("{}|{}|%".format(time.strftime("%d.%m.%Y %H:%M%:%S"), value), file=self.humidity_logger)

    def log_weather(self, temperature, humidity):
        self.log_temperature(temperature)
        self.log_humidity(humidity)

