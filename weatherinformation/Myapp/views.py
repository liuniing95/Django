from django.shortcuts import render
import requests
from .Readjson import GetTime, GetSuntime, GetCityID, NowWeather, FutureWeather
import json
def index(request):
    city = request.GET.get('city')
    if city == None:
        city = 'Toronto'
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=64491913cbf16a5211245c3e20c8f3d2".format(city)
    WeatherInformation = requests.get(url).text
    cityid = GetCityID(WeatherInformation)
    Futureurl = "http://api.openweathermap.org/data/2.5/forecast?id={}&units=metric&appid=64491913cbf16a5211245c3e20c8f3d2".format(cityid)
    FutureInformation = requests.get(Futureurl).text
    Datelist, Templist, Humidlist = FutureWeather(FutureInformation)
    Weather, Main, Sys = NowWeather(WeatherInformation)

    return render(request, 'index.html',{
        'Datelist' : json.dumps(Datelist),
        'Templist' : json.dumps(Templist),
        'icon' : Weather[0]['icon'],
        'description' : Weather[0]['description'],
        'temp' : Main['temp'],
        'temp_min' : Main['temp_min'],
        'temp_max': Main['temp_max'],
        'cityname' : city,
        'sunrise': GetSuntime(Sys['sunrise']),
        'sunset': GetSuntime(Sys['sunset']),
        'humidity': Main['humidity'],


    })

