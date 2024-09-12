import requests

def get_weather(city):
    url = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid=cb601adec96ff55891dcf40967b3c803"
    response = requests.request('GET', url)
    return response.json()
