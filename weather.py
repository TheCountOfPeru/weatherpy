import requests
import json
import argparse

kelvinConstant = 273.15


def convertKelvinToCelcius(temperatureInKelvin):
    return temperatureInKelvin - kelvinConstant
    
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

def roundFloatUp(aFloat):
    return ('{:.0f}'.format(aFloat))

def displayWeatherReport(weatherDictionary):
    wd = weatherDictionary
    print(wd["description"] + ", " + str(roundFloatUp(wd["temperature"])) + "C, / feels like " 
    + str(roundFloatUp(wd["feels_like"])) + "C | Humidity: " + str(wd["humidity"]) + "% | " +
    wd["locationName"] + ", " + wd["locationCountry"])

def queryWeatherAPIFor(thisLocation, APIKey):
    parameters = {"q": thisLocation, "appid": APIKey}
    response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
    if(response.status_code!=200):
        return response.status_code
    return response.json()

def quitIfNotResponse200(weatherQueryResults):
    if(isinstance(weatherQueryResults,int)):
        print("HTTP error: "+ str(weatherQueryResults))
        exit()

def argumentParserBuilder():
    parser = argparse.ArgumentParser(
        description='weatherpy - basic weather information'
    )
    parser.add_argument(
        'location',
        help='Input location for query. Use "city name" or "city name,country code"',
    )
    return parser

if __name__ == "__main__":
    parser = argumentParserBuilder()
    args = parser.parse_args()
    configuration = json.load(open("config.json"))
    weatherQueryResults = queryWeatherAPIFor(args.location, configuration["APIKey"])
    quitIfNotResponse200(weatherQueryResults)
    displayWeatherReport(convertQueryResultToDict(weatherQueryResults))