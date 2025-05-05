import requests
import os
from dotenv import load_dotenv
from help_func import *

# LOAD THE .ENV FILE FOR API KEY
load_dotenv()
API_KEY = os.getenv("ACCUWEATHER_API_KEY")

# CURRENT WEATHER FUNCTION
def getCurrentWeather(location_key: str, city: str) -> None:
    # PUSH REQUEST FOR CURRENT WEATHER IN THE SELECTED CITY
    url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey={API_KEY}&details=true"
    response = requests.get(url)
    #IF SUCCESSFUL, PRINT THE INFO
    if response.status_code == 200:
        try:
            data = response.json()[0]
            time = data["LocalObservationDateTime"][11:19]
            isDay = data['IsDayTime']
            weather_text = data["WeatherText"]
            temperature = data["Temperature"]["Metric"]["Value"]
            temp_unit = data["Temperature"]["Metric"]["Unit"]
            find_hour_weather(weather_text, time, city, isDay)
            color = '\033[31m' if temperature >= 17.0 else '\033[34m'
            print(f"🌡️  Temperature: {color}{temperature}°{temp_unit}\033[0m")
        # IF CITY CODE HAS AN ERROR, RETURN ERROR
        except IndexError:
            print(f"\033[31mError getting weather information for the city '{city}'\033[0m")
            return
    #ELSE, RETURN ERROR
    else: 
        try:
            data = response.json()
            print(f"\033[31mError {response.status_code}: {data['Message']}\033[0m")
            return
        except IndexError:
            print(f"\033[31mError getting weather information for the city '{city}'\033[0m")

# REPEAT FOR OTHER FUNCTIONS:

def getNextHourWeather(location_key: str, city: str) -> None:
    url = f"http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/{location_key}?apikey={API_KEY}&metric=true"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()[0]
            time = data["DateTime"][11:19]
            isDay = data['IsDaylight']
            weather_text = data["IconPhrase"]
            temperature = data["Temperature"]["Value"]
            temp_unit = data["Temperature"]["Unit"]
            find_hour_weather(weather_text, time, city, isDay)
            color = '\033[31m' if temperature >= 17.0 else '\033[34m'
            print(f"🌡️  Temperature: {color}{temperature}°{temp_unit}\033[0m")
        except IndexError:
            print(f"\033[31mError getting weather information for the city '{city}'\033[0m")
    
    else: 
        try:
            data = response.json()
            print(f"\033[31mError {response.status_code}: {data['Message']}\033[0m")
        except IndexError:
            print(f"\033[31mError getting weather information for the city '{city}'\033[0m")




def getNext12Hours(location_key: str, city: str) -> None:
    url = f"http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/{location_key}?apikey={API_KEY}&metric=true"
    response = requests.get(url)

    if response.status_code == 200:
        for i in range(12):
            try:
                data = response.json()[i]
                time = data["DateTime"][11:19]
                if i == 0:
                    date = data["DateTime"][0:10].split("-")
                    print(f'Hourly weather on {date[2]}.{date[1]}.{date[0]} in {city} is: ')
                isDay = data['IsDaylight']
                temperature = data["Temperature"]["Value"]
                weather_text = data["IconPhrase"]
                temp_unit = data["Temperature"]["Unit"]
                
                find_hour_weather(weather_text, time, city, isDay)

                color = '\033[31m' if temperature >= 17.0 else '\033[34m'
                print(f"🌡️  Temperature: {color}{temperature}°{temp_unit}\033[0m\n")
            except IndexError:
                print(f"\033[31mError getting weather information for the city '{city}'\033[0m")
    
    else: 
        try:
            data = response.json()
            print(f"\033[31mError {response.status_code}: {data['Message']}\033[0m")
        except IndexError:
            print(f"\033[31mError getting weather information for the city '{city}'\033[0m")
            



def getTodayWeather(location_key: str, city: str) -> None:
    url = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}?apikey={API_KEY}&metric=true"
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            forecast = data["DailyForecasts"][0]
            min_temp = forecast["Temperature"]["Minimum"]["Value"]
            max_temp = forecast["Temperature"]["Maximum"]["Value"]
            weather_text_day = forecast["Day"]["IconPhrase"]
            weather_text_night = forecast["Night"]["IconPhrase"]
            temp_unit = forecast["Temperature"]["Minimum"]["Unit"]
            print(f"Today's weather in {city} is: ")
            color_min = "\033[31m" if float(min_temp) >=17.0 else "\033[34m"
            color_max = "\033[31m" if float(max_temp) >=17.0 else "\033[34m"
            print(f"🌡️  Min. Temperature: {color_min}{min_temp}°{temp_unit}\033[0m")
            print(f"   Max. Temperature: {color_max}{max_temp}°{temp_unit}\033[0m")
            find_day_weather(weather_text_day, weather_text_night)
        except IndexError:
            print(f"\033[31mError getting weather information for the city '{city}'\033[0m")
    
    else: 
        try:
            data = response.json()
            print(f"\033[31mError {response.status_code}: {data['Message']}\033[31m")
        except IndexError:
            print(f"\033[31mError getting weather information for the city '{city}'\033[0m")




def get5DaysWeather(location_key: str, city: str) -> None:
    url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}?apikey={API_KEY}&metric=true"
    response = requests.get(url)

    if response.status_code == 200:
        for i in range(5):
            try:
                data = response.json()
                forecast = data["DailyForecasts"][i]
                date = forecast["Date"][0:10].split("-")
                min_temp = forecast["Temperature"]["Minimum"]["Value"]
                max_temp = forecast["Temperature"]["Maximum"]["Value"]
                weather_text_day = forecast["Day"]["IconPhrase"]
                weather_text_night = forecast["Night"]["IconPhrase"]
                temp_unit = forecast["Temperature"]["Minimum"]["Unit"]

                print(f"\nWeather on {date[2]}.{date[1]}.{date[0]} in {city} is: ")
                color_min = "\033[31m" if float(min_temp) >=17.0 else "\033[34m"
                color_max = "\033[31m" if float(max_temp) >=17.0 else "\033[34m"
                print(f"🌡️  Min. Temperature: {color_min}{min_temp}°{temp_unit}\033[0m")
                print(f"   Max. Temperature: {color_max}{max_temp}°{temp_unit}\033[0m")

                find_day_weather(weather_text_day, weather_text_night)
                print()
            except IndexError:
                print(f"\033[31mError getting weather information for the city '{city}'\033[0m")
    
    else: 
        try:
            data = response.json()
            print(f"\033[31mError {response.status_code}: {data['Message']}\033[0m")
        except IndexError:
            print(f"\033[31mError getting weather information for the city '{city}'\033[0m")