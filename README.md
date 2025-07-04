# Weather App

A simple weather application built with Python and Tkinter that fetches current weather information for any city using the WeatherAPI service.

## Features

- Get current weather conditions for any city
- Display temperature in Celsius
- Shows city name and weather condition description
- Error handling for invalid cities or API issues
- Simple and intuitive GUI interface

## File Structure

```
├── app.py          # Main application logic and API handling
└── gui.py          # GUI interface using Tkinter
```

## Requirements

- Python 3.x
- `requests` library for API calls
- `tkinter` for GUI

## Installation and Usage

1. Clone or download this repository
2. Navigate to the project directory
3. Install required dependencies:
   ```bash
   pip install requests tkinter
   ```
4. Start the weather app:
    ```bash
    python app.py
    ```
This will launch the GUI interface where you can:
1. Enter a city name in the input field
2. Click "Submit" or press Enter to get weather information
3. View the results including city name, temperature, and weather condition

## Application Details

### app.py

Contains the core weather fetching functionality:

- `get_weather(city)`: Main function that fetches weather data from WeatherAPI
- Error handling for various API response codes
- Returns either weather data (city, temperature, condition) or error code(s)

### gui.py

Implements the graphical user interface:

- Creates a Tkinter window with input field and display labels
- Handles user interactions (button clicks, Enter key)
- Displays weather information or error messages
- `launch()`: Starts the GUI main loop
- `refresh_info()`: Updates the display with new weather data

## Error Handling

The application handles common errors:

- **Error 1006**: City not found
- **Error 1003**: No input provided
- Other API errors are displayed with their error codes
