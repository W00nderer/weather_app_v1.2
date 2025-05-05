import requests
import json
import os
from dotenv import load_dotenv
from weather_func import *

# LOAD THE .ENV FILE FOR API KEY
load_dotenv()
API_KEY = os.getenv("ACCUWEATHER_API_KEY")


# LOAD THE .JSON FILE TO GET THE CITIES PREVIOUSLY INPUTTED
CITIES_FILE = "Python\\weather_app\\cities.json"

def load_accounts():
    # CHECK IF THE FILE IS EMPTY
    if not os.path.exists(CITIES_FILE) or os.stat(CITIES_FILE).st_size == 0:
        return {}

    try:
        # TRY OPENING THE FILE IF NOT EMPTY, LOAD THE CODES INTO A DICT
        with open(CITIES_FILE, 'r', encoding='utf-8') as f:
            city_codes = json.load(f)
            return city_codes

    except json.JSONDecodeError:
        # RETURN AN EMPTY DICT IF ERROR ENCOUNTERED
        print("Warning: cities.json is empty or contains invalid JSON. Skipping load.")
        return {}

city_codes = load_accounts()


# GET THE CODE FOR INPUTTED CITY 
def getCityCode(op: int) -> None:
    # NORMALIZE THE NAME 
    city = input("Enter the name of the city: ").strip().title()
    # IF THE CITY WAS PREVIOUSLY REQUESTED, GET THE CODE FROM THE DICT
    if city in city_codes:
        location_key = city_codes[city]
    # OTHERWISE, SEND REQUEST FOR THE CODE
    else:  
        url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={city}"
        response = requests.get(url)
        # IF SUCCESSFUL, TAKE THE KEY FROM DATA
        if response.status_code == 200:
            try:
                data = response.json()[0]
                location_key = data["Key"]
                city_codes[city] = location_key
            # IF DATA[0] DOES NOT EXIST, THE CITY NAME IS WRONG OR DOES NOT EXIST
            except IndexError:
                print(f"\033[31mError getting weather information for the city '{city}'\033[0m")
                return
        # ELSE, RETURN ERROR GIVEN
        else: 
            try:
                data = response.json()
                print(f"\033[31mError {response.status_code}: {data['Message']}\033[0m")
                return
            except IndexError:
                print(f"\033[31mError getting weather information for the city '{city}'\033[0m")
    # MATCH THE OPERATION REQUESTED
    match op:
        case 1:
            getCurrentWeather(location_key, city)
        case 2:
            getNextHourWeather(location_key, city)
        case 3:
            getNext12Hours(location_key, city)
        case 4:
            getTodayWeather(location_key, city)
        case 5:
            get5DaysWeather(location_key, city)
        case _:
            print("\033[31mUnexpected error\033[0m")


while True:
    print("Welcome to Weather App!")
    print("1: get the current weather")
    print("2: get the weather for the next hour")
    print("3: get the weather for the next 12 hours")
    print("4: get today's forecast")
    print("5: get forecast for the next 5 days")
    print("6: exit")
    ans = input("Enter the number of operation: ")
    match ans:
        case '1':
            getCityCode(1)
        case '2':
            getCityCode(2)
        case '3':
            getCityCode(3)
        case '4':
            getCityCode(4)
        case '5':
            getCityCode(5)
        case '6':
            break
        case _:
            print('\033[31mError: wrong command\033[0m')

# BEFORE EXITING THE PROGRAM, SAVE THE DICT TO JSON FILE
with open(CITIES_FILE, "w", encoding="utf-8") as f:
    json.dump(city_codes, f, ensure_ascii=False, indent=4)
    
