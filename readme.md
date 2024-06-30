# Weather Window - A Visual Weather App

## Description
This Python application provides a user-friendly interface to retrieve and display current weather data for any location.

## Features
- Intuitive GUI: Search for your desired location and view a comprehensive weather report.
- Real-Time Weather: Get current temperature (°C), wind speed (km/h), cloud cover (%), and humidity.
- Time and Date Display: See the current date and time for the specified location.
- API Integration: Retrieves weather data from a reliable weather service provider.

## Installation
1. Create a Virtual Environment (Recommended):
- Virtual environments isolate project dependencies from your system-wide Python installation, preventing conflicts.

   ```shell
   python -m venv my_env  # Replace "my_env" with your desired environment name
   ```
- Activate the virtual environment
   ```shell
   source my_env/bin/activate  # For Linux/macOS
   my_env\Scripts\activate.bat  # For Windows
   ```

2. Install Required Libraries.

   ```shell
   pip install -r requirements.txt
   ```

## Obtain an API Key
1. Weather Window uses a weather API to retrieve data. You'll need an API key from a provider like https://www.weatherapi.com/.

2. Replace API Key.
- Open app.py and replace API_KEY with your actual API key.

3. Run the Application.

   ```shell
   python app.py
   ```
- This will launch the application in your web browser, usually at http://127.0.0.1:5001/.

## Usage
1. Enter your desired location in the search bar at the top.

2. Click "Search".

3. The application will display the current weather information and time/date for the entered location.

## Skills and Knowledge Gained
Developing Weather Window provided me with the opportunity to learn and improve upon various programming and development skills. Here are some key takeaways:

* **Python Fundamentals:** Strengthened my understanding of core Python concepts like variables, functions, data types, control flow, and loops.
* **Flask Framework:** Gained proficiency in using Flask, a popular web framework, for building user interfaces and handling user interactions.
* **API Integration:** Successfully integrated with a weather service provider's API to retrieve real-time weather data.
* **Libraries and Packages:** Learned to effectively utilize libraries like `requests` for API communication, `json` for data parsing, and `timezone_query` (my custom module) for location-based time and date retrieval.
* **Command Line Interface:** Increased comfort using the command line for tasks like installing libraries, creating virtual environments, and running the application. 
* **Project Structure:** Developed skills in organizing code into well-structured and maintainable files.

This project has been a valuable learning experience, and I'm excited to continue building my skills in web development!

## License
This project is licensed under the [MIT License](LICENSE).

## Author
- Chaitany Chaudhary

