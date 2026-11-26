from datetime import date
from enum import Enum


class WeatherType(Enum):

    SUNNY = "SUNNY
    CLOUDY = "CLOUDY
    RAINY = "RAINY"
    FOGGY = "FOGGY"
    SNOWY = "SNOWY"
    WINDY = "WINDY"


class Weather:

    def __init__(self, day, city, country, temp, humidity, wind_speed,
                 weather_type):
        self._day = day
        self._city = city
        self._country = country
        self._temp = temp
        self._humidity = humidity
        self._wind_speed = wind_speed
        self._weather_type = weather_type

    def __del__(self):
        print(f»Запис погоди ({self._city}, {self._day}) видалено»)

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value):
        self._day = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        self._temp = value

    @property
    def humidity(self):
        return self._humidity

    @humidity.setter
    def humidity(self, value):
        self._humidity = value

    @property
    def wind_speed(self):
        return self._wind_speed

    @wind_speed.setter
    def wind_speed(self, value):
        self._wind_speed = value

    @property
    def weather_type(self):
        return self._weather_type

    @weather_type.setter
    def weather_type(self, value):
        self._weather_type = value

    def is_lviv_weather(self, humidity=None, weather_type=None):

        if humidity is None:
            humidity = self._humidity
        if weather_type is None:
            weather_type = self._weather_type

        if humidity > 80 and weather_type == WeatherType.RAINY:
            message = «The typical day in Lviv»
        else:
            message = «You’re lucky, man»
        print(message)
        return message

    def __str__(self):
        return (f»{self._day} | {self._city}, {self._country} | «
                f»{self._temp:>5.1f} °C | вологість {self._humidity}% | «
                f»вітер {self._wind_speed} м/с | {self._weather_type.value}»)

    def display(self):
        print(self)


class WeatherCalendar:

    def __init__(self, records=None):
        self._records = list(records) if records else []

    def __del__(self):
        print(«Календар погоди видалено»)

    @property
    def records(self):
        return self._records

    def add_record(self, weather):
        self._records.append(weather)

    def remove_record(self, weather):
        if weather in self._records:
            self._records.remove(weather)

    @staticmethod
    def find_max_temperature(records, day):
        temps = [w.temp for w in records if w.day == day]
        if not temps:
            print(«Not enough data»)
            return None
        return max(temps)

    def sort_by_day(self):
        self._records.sort(key=lambda w: w.day)

    def display(self):
for weather in self._records:
            weather.display()


def main():
    w1 = Weather(date(2025, 11, 12), «Lviv», «Ukraine», 6.5, 88, 4.2,
                 WeatherType.RAINY)
    w2 = Weather(date(2025, 11, 10), «Kyiv», «Ukraine», 9.0, 60, 3.0,
                 WeatherType.CLOUDY)
    w3 = Weather(date(2025, 11, 10), «Odesa», «Ukraine», 12.3, 55, 6.1,
                 WeatherType.SUNNY)
    w4 = Weather(date(2025, 11, 11), «Lviv», «Ukraine», 4.0, 70, 2.5,
                 WeatherType.FOGGY)

    calendar = WeatherCalendar([w1, w2, w3])
    calendar.add_record(w4)

    print(«Записи до сортування:»)
    calendar.display()

    calendar.sort_by_day()
    print(«\nЗаписи після сортування за днем:»)
    calendar.display()

    print(«\nМаксимальна температура:»)
    day = date(2025, 11, 10)
    result = WeatherCalendar.find_max_temperature(calendar.records, day)
    if result is not None:
        print(f»{day}: {result} °C»)

    print(«\nДень без записів:»)
    WeatherCalendar.find_max_temperature(calendar.records, date(2025, 11, 20))

    print(«\nПеревірка isLvivWeather:»)
    w1.is_lviv_weather()
    w3.is_lviv_weather()
    w1.is_lviv_weather(90, WeatherType.SUNNY)

    print(«\nВидалення запису:»)
    calendar.remove_record(w4)
    calendar.display()


if name == «__main__»:
    main()
