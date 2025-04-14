def process_weather_request() :
    print('processing weather request')


from bs4 import BeautifulSoup as soup
import requests

# For Inputs
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
    # print(lat)
    # print(long)

   
    return lat, lon

def get_weather(city,state):
    city = city_fix(city)
    state = state_abbrev(state)
    lat, lon = get_coords(city, state)
    return get_weather_coords(lat, lon, my_key)







# API

import requests
import json




my_key = "cb89c37822875b5b47319c98f6cb1522"

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


print(get_weather("Portland", "me"))
# coords = get_coords("portland","me")
# weather = get_weather(coords[0],coords[1],my_key)

# print(weather)



