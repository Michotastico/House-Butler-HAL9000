import urllib
import json
from datetime import datetime


class Weather:
    def __init__(self, city, pid):
        self.url = "http://api.openweathermap.org/data/2.5/forecast?id="+str(city)+"&units=metric&appid="+pid
        self.last_update = ''
        self.last_hour = ''
        self.forecast = None

    def is_updated(self):
        date = datetime.now()
        date = unicode(date).split(" ")[0]
        return self.last_update == date

    def clean_past(self):
        hour = unicode(datetime.now()).split(" ")[1].split(".")[0]
        if hour > self.last_hour:
            self.forecast[self.last_update] = self.forecast[self.last_update][1:]

    def get_data(self):
        response = urllib.urlopen(self.url)
        data = json.loads(response.read())
        forecast = data['list']
        self.last_update, self.last_hour = parse_date(forecast[0])

        _forecast = {}
        days = []
        for weather in forecast:
            day, hour = parse_date(weather)
            days.append(day)
            if day not in _forecast:
                _forecast[day] = {}
                _forecast[day]['forecast'] = []
            _forecast[day]['forecast'].append(weather)
        self.forecast = _forecast

        midday = '12:00:00'
        for day in days:
            forecast = self.forecast[day]['forecast']
            temp_min = forecast[0]['main']['temp_min']
            temp_max = forecast[0]['main']['temp_max']
            for f in forecast:
                tmp_min = f['main']['temp_min']
                tmp_max = f['main']['temp_max']
                if tmp_min < temp_min:
                    temp_min = tmp_min
                if tmp_max > temp_max:
                    temp_max = tmp_max
                day, hour = parse_date(f)
                if hour == midday:
                    self.forecast[day]['weather'] = f['weather'][0]['main']
            if day == self.last_update:
                self.forecast[day]['weather'] = self.forecast[day]['forecast'][0]['weather'][0]['main']
            self.forecast[day]['temp_min'] = temp_min
            self.forecast[day]['temp_max'] = temp_max

    def update(self):
        if not self.is_updated():
            self.get_data()
        else:
            self.clean_past()

    def show(self):
        for key, fore in self.forecast.items():
            print key, fore['weather'], fore['temp_min'], fore['temp_max']


def parse_date(data):
    return data['dt_txt'].split(" ")


