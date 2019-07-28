import pyowm

owm = pyowm.OWM('8ffcdc8981123525a41755fad15b12e0' , Language = "ru")

place = input('В каком городе/стране?')

observation = owm.weather_at_place('place')
w = observation.get_weather()

print(w) 