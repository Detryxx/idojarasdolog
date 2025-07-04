import requests
import json
response_API = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=2e0846b09ae1c196567ee72580eecec0')
print(response_API.status_code)