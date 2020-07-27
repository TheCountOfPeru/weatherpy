import requests
import json

kelvinConstant = 273.15

def convertKelvinToCelcius(temperatureInKelvin):
    return temperatureInKelvin - kelvinConstant

def weatherpy():
    print("weatherpy")
    # parameters = {"q": "calgary", "appid": "a24139ce6321ad86e6b5a7bbe45287b7"}
    # # Make a get request to get the latest position of the international space station from the opennotify api.
    # response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
    # # Print the status code of the response.
    # # print(response.status_code)
    # # print(response.content)
    # weatherData = response.json()
    # # print(type(data))
    # print(convertKelvinToCelcius(weatherData["main"]["temp"]))

if __name__ == "__main__":
    weatherpy()
