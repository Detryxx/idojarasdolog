"""
requests -- for requesting data fro the api
ast -- for literal_eval, to turn the returnded str into a dict
"""
 
import requests
import ast
import gui
 
api_errors ={ 
    1002: 	"API key not provided.",
    1003: 	"Parameter 'q' not provided.",
    1005: 	"API request url is invalid",
    1006: 	"No location found matching parameter 'q'",
    2006: 	"API key provided is invalid",
    2007: 	"API key has exceeded calls per month quota.",
    2008: 	"API key has been disabled.",
    2009: 	"API key does not have access to the resource. Please check pricing page for what is allowed in your API subscription plan.",
    9000: 	"Json body passed in bulk request is invalid. Please make sure it is valid json with utf-8 encoding.",
    9001: 	"Json body contains too many locations for bulk request. Please keep it below 50 in a single request.",
    9999: 	"Internal application error."
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