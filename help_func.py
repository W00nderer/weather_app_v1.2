
# MAP WITH ALL THE EMOJIES, FOUND BY THE WEATHER TEXT AND WHETHER IT'S DAY OR NOT
def get_emoji(weather_text: str, isDay: bool) -> str:
    emoji_map = {
        "Sunny": "☀️",
        "Mostly clear": "☀️" if isDay else "🌙",
        "Hazy sunshine": "☀️🌫️",
        "Partly sunny": "🌤️",
        "Mostly sunny": "🌤️",
        "Partly cloudy": "⛅" if isDay else "🌙☁️",
        "Intermittent clouds": "⛅" if isDay else "🌙☁️",
        "Clouds and sun": "⛅",
        "Partly cloudy w/ showers": "🌦️" if isDay else "🌙🌧️",
        "Mostly cloudy": "🌥️" if isDay else "☁️🌙☁️☁️",
        "Mostly cloudy w/ showers": "🌥️🌧️" if isDay else "☁️🌙🌧️",
        "Cloudy": "☁️",
        "Clear": "🌙",
        "Partly clear": "🌙☁️",
        "Rain": "🌧️",
        "Showers": "🌧️",
        "Drizzle": "🌧️",
        "Snow": "🌨️",
        "Thunderstorm": "🌩️",
        "Fog": "🌫️"
    }
    # RETURN A RAINBOW IF WEATHER TEXT NOT FOUND
    return emoji_map.get(weather_text, "🌈")

# NORMALIZE THE FORMAT FOR HOUR AND DAY WEATHER

def find_hour_weather(weather_text: str, time: str, city: str, isDay: bool) -> None:
    emoji = get_emoji(weather_text, isDay)
    color = "\033[33m" if isDay else "\033[35m"
    print(f'{emoji}  The weather in {city} at {time}: {color}{weather_text}\033[0m')
    
def find_day_weather(weather_text_day: str, weather_text_night: str) -> None:
    emoji_day = get_emoji(weather_text_day, True)
    emoji_night = get_emoji(weather_text_night, False)
    print(f"{emoji_day}   Weather in the day: \033[33m{weather_text_day}\033[0m")
    print(f"{emoji_night}  Weather at night: \033[35m{weather_text_night}\033[0m")