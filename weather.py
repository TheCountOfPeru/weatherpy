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

def queryWeatherAPIFor(thisLocation):
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
    
def getWeatherDescription(weatherQueryResults): 
    return weatherQueryResults["weather"][0]["description"]

def getTemperature(weatherQueryResults):
    return weatherQueryResults["main"]["temp"] - kelvinConstant

def getFeelsLikeTemperature(weatherQueryResults):
    return weatherQueryResults["main"]["feels_like"] - kelvinConstant

def getHumidity(weatherQueryResults):
    return weatherQueryResults["main"]["humidity"]

def getLocationName(weatherQueryResults):       
    return weatherQueryResults["name"]

def getLocationCountry(weatherQueryResults):         
    return weatherQueryResults["sys"]["country"]

def convertQueryResultToDict(weatherQueryResults):
  
    weatherInfomationDict = {
        "description": getWeatherDescription(weatherQueryResults),
        "temperature":getTemperature(weatherQueryResults),
        "feels_like": getFeelsLikeTemperature(weatherQueryResults),
        "humidity":getHumidity(weatherQueryResults),
        "locationName":getLocationName(weatherQueryResults),
        "locationCountry":getLocationCountry(weatherQueryResults),
    }
    return weatherInfomationDict

def displayWeatherReport(weatherDictionary):
    wd = weatherDictionary
    print(wd["description"] + ", " + str(wd["temperature"]) + )

if __name__ == "__main__":
    parser = argumentParserBuilder()
    args = parser.parse_args()
    weatherQueryResults = queryWeatherAPIFor(args.location)
    weatherDictionary = convertQueryResultToDict(weatherQueryResults)
    displayWeatherReport(weatherDictionary)