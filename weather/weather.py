from voice.pyttsx3_voice import voice
from bs4 import BeautifulSoup as soup
import requests

# for ease of development, comment this function out
# to just print things normally instead.
def print(string):
    voice(string, 34)

# Transfer Inputs
states = {
    "al": "Alabama",
    "ak": "Alaska",
    "az": "Arizona",
    "ar": "Arkansas",
    "ca": "California",
    "co": "Colorado",
    "ct": "Connecticut",
    "de": "Delaware",
    "dc": "District of Columbia",
    "fl": "Florida",
    "ga": "Georgia",
    "gu": "Guam",
    "hi": "Hawaii",
    "id": "Idaho",
    "il": "Illinois",
    "in": "Indiana",
    "ia": "Iowa",
    "ks": "Kansas",
    "ky": "Kentucky",
    "la": "Louisiana",
    "me": "Maine",
    "md": "Maryland",
    "ma": "Massachusetts",
    "mi": "Michigan",
    "mn": "Minnesota",
    "ms": "Mississippi",
    "mo": "Missouri",
    "mt": "Montana",
    "ne": "Nebraska",
    "nv": "Nevada",
    "nh": "New Hampshire",
    "nj": "New Jersey",
    "nm": "New Mexico",
    "ny": "New York",
    "nc": "North Carolina",
    "nd": "North Dakota",
    "mp": "Northern Mariana Islands",
    "oh": "Ohio",
    "ok": "Oklahoma",
    "or": "Oregon",
    "pa": "Pennsylvania",
    "pr": "Puerto Rico",
    "ri": "Rhode Island",
    "sc": "South Carolina",
    "sd": "South Dakota",
    "tn": "Tennessee",
    "tx": "Texas",
    "tt": "Trust Territories",
    "ut": "Utah",
    "vt": "Vermont",
    "va": "Virginia",
    "vi": "Virgin Islands",
    "wa": "Washington",
    "wv": "West Virginia",
    "wi": "Wisconsin",
    "wy": "Wyoming"
}


def state_abbrev(input):
    for key, value in states.items():
        if value.lower() == input.lower():
            return key
    return input

def city_fix(input):
    if " " in input:
            words = input.split()
            city = "-".join(words)
            return city.lower()
    else:
        return input.lower()

# Get coordinates for API
def get_coords(city, state):
    url = f'https://www.wunderground.com/weather/us/{state}/{city.lower()}'

    req = requests.get(url)
    web_page = req.content

    web = soup(web_page,'html.parser')

    name_box = web.find('span', class_ = 'subheading')
    name = name_box.text.split() 

    for item in name:
        if "°N" in item:
            lat = float(name[3])
        elif "°S" in item:
            lat = float(name[3])
            lat = lat * (-1)
        elif "°W" in item:
            lon = float(name[5])
            lon = lon * (-1)
        elif "°E" in item:
            lon = float(name[5])
    return lat, lon


# API dictionary return
def get_weather_coords(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    return {
        "temp": data["main"]["temp"],
        "feels like": data["main"]["feels_like"],
        "high": data["main"]["temp_max"],
        "low": data["main"]["temp_min"],
        "wind speed": data["wind"]["speed"],
        "condition": data["weather"][0]["main"],
        "humidity": data["main"]["humidity"]
    }



# Conmbines all functions above
import os


def get_weather(city, state):
    API_KEY = os.getenv("WEATHER_API_KEY")  # Load API key from environment variable
    if not API_KEY:
        raise ValueError("API Key not found. Please set the WEATHER_API_KEY environment variable.")
    city = city_fix(city)
    state = state_abbrev(state)
    lat, lon = get_coords(city, state)
    return get_weather_coords(lat, lon, API_KEY)



# Maps conditions a user might request to the keys we use in the output from get_weather_coords
ALL_CONDITIONS = {
    "temperature": "temp",
    "feels": "feels like",
    "high": "high",
    "low": "low",
    "wind": "wind speed",
    "weather": "condition",
    "condition": "condition",
    "humidity": "humidity"
}

def find_in_list(item, list):
    if item in list:
        return list.index(item)
    else:
        return None
def parse_request(request):
    import re
    # Lowercase, split into words, then strip non-alphabet characters (like commas and stuff)
    tokens = [re.sub(r"[^a-z]", "", word) for word in request.lower().split()]
    if "exit" in tokens:
        return True 

    state = None
    state_tok = -1
    for state_abbrv, state_full in states.items():
        idx = find_in_list(state_abbrv.lower(), tokens)
        if idx is None:
            idx = find_in_list(state_full.lower(), tokens)
        if idx is not None:
            state = state_abbrv
            state_tok = idx
    if state is None:
        return error("Please specify a state")
    if state_tok == 0:
        return error("Please specify a city before the state")
    
    # Just assume the city is right before the state
    city = tokens[state_tok-1]

    # requested_cond holds the actual word the user input, not the key we'll use
    # e.g. If the user writes "temperature", requested_cond="temperature" but
    # we'll look for data["temp"]
    requested_cond = None
    for condition in ALL_CONDITIONS.keys():
        idx = find_in_list(condition.lower(), tokens)
        if idx is not None:
            requested_cond = condition
            break
    if requested_cond is None:
        return error("Please specify a weather condition")

    data = get_weather(city, state)[ALL_CONDITIONS[requested_cond]]
    # TODO: This sentence format won't always make sense grammatically, so we should be smarter about it
    print(f"The {requested_cond} in {city.capitalize()}, {state.capitalize()} is {data}")
    return False


def error(message):
    print(f"Error: {message}")
    return False

# This is the function used by the driver, and the only
# public function of this module
# TODO: request user input properly
def process_weather_request():
    while True:
        print("What weather information would you like?")
        if parse_request(input()):
            return