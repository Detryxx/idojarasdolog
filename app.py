"""
requests -- for requesting data fro the api
ast -- for literal_eval, to turn the returnded str into a dict
"""
 
import requests
import ast
import gui
 
api_errors = {
    1006: "City not found",
    1003: "No input",
    
}

def get_weather(city=str):
    """
    Keyword Arguments:
    city -- the user defined city to wich to get the weather from
 
    Fetches the temperature and the condition from the city given
    trough the weatherapi api and checks for errors.
    """
    response_API = requests.get(
        # fetches the data with of the given city
        f"http://api.weatherapi.com/v1/current.json?key=b2c05218b2004702b9784017250407&q={city}&aqi=no"
    )
 
    try:  # tries to fetch the temperature in Celsius and the condition
        temp = ast.literal_eval(response_API.text).get("current").get("temp_c")
        condition = (
            ast.literal_eval(response_API.text)
            .get("current")
            .get("condition")
            .get("text")
        )
    except:  # if it cant fetch the above stated data, an error must have orruced so it returns the rror code
        error_code = ast.literal_eval(response_API.text).get("error").get("code")
        return error_code
    else:  # if good, returns the requested data
        return city.title(), temp, condition


if __name__ == "__main__":
    gui.launch()