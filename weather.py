import requests
import json
import argparse

kelvinConstant = 273.15
APIKey = "a24139ce6321ad86e6b5a7bbe45287b7"

def argumentParserBuilder():
    parser = argparse.ArgumentParser(
        description='weatherpy - basic weather information'
    )
    parser.add_argument(
        'location',
        help='Display weather information for this location',
    )
    return parser

def convertKelvinToCelcius(temperatureInKelvin):
    return temperatureInKelvin - kelvinConstant

def queryWeatherFor(thisLocation):
    parameters = {"q": thisLocation, "appid": APIKey}
    # Make a get request to get the latest position of the international space station from the opennotify api.
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
    # Print the status code of the response.
    print(response.status_code)
    # print(response.content)
    # weatherData = response.json()
    # print(type(data))
    # print(convertKelvinToCelcius(weatherData["main"]["temp"]))
    return response.json()


def displayWeatherFor(weatherQueryResults):



if __name__ == "__main__":
    parser = argumentParserBuilder()
    args = parser.parse_args()
    weatherQueryResults = queryWeatherFor(args.location)
    
