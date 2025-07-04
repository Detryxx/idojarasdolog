import requests
import ast


def get_weather(city = str):
    response_API = requests.get(f'http://api.weatherapi.com/v1/current.json?key=b2c05218b2004702b9784017250407&q={city}&aqi=no')

    try:
        temp = ast.literal_eval(response_API.text).get("current").get("temp_c")
        condition = ast.literal_eval(response_API.text).get("current").get("condition").get("text")
        is_it_good = response_API.status_code
    except:
        error_code = ast.literal_eval(response_API.text).get("error").get("code")
        return error_code
    else:
        return city, temp, condition, is_it_good


if __name__ == "__main__":
    print(get_weather("London"))