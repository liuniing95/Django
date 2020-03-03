import json
import time

class Weatherdata:
    def __init__(self, weather, main, wind, clouds, dt, sys):
        self.weather = weather
        self.main = main
        self.wind = wind
        self.clouds = clouds
        self.dt = dt
        self.sys = sys

def GetTime(time1):
    LocalTime = time.localtime(time1)
    return (time.strftime('%m-%d %H:%M', LocalTime))

def GetSuntime(time1):
    LocalTime = time.localtime(time1)
    return (time.strftime('%H:%M',LocalTime))

def GetCityID(txt):
    js = json.loads(txt)
    return (js['id'])

def NowWeather(txt):
    js = json.loads(txt)
    weatherdata = Weatherdata(js['weather'],js['main'],js['wind'],js['clouds'],js['dt'],js['sys'])
    return (weatherdata.weather,weatherdata.main,weatherdata.sys)

def FutureWeather(txt):
    js = json.loads(txt)
    list = js['list']
    listFuture = []
    FCDate = []
    FCTemperature = []
    FCHumity = []
    for i in range(0,len(list)):
        futurewather = Weatherdata(list[i]['weather'],list[i]['main'],list[i]['wind'],list[i]['clouds'],list[i]['dt'],list[i]['sys'])
        listFuture.append(futurewather)
    for i in range(0,len(listFuture)):
        FCDate.append(GetTime(listFuture[i].dt))
        FCTemperature.append(listFuture[i].main['temp'])
        FCHumity.append(listFuture[i].main['humidity'])
    return (FCDate,FCTemperature,FCHumity)
