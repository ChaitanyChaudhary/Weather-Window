from flask import Flask, render_template, request
import requests
import json

from timezone_query import get_time_date


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/get_Weather_data', methods=["POST"])
def get_Weather_data():
    user_location = request.form.get('locationInput')  # Get location from form data
    try:
        # api key is from https://www.weatherapi.com/
        url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={user_location}"

        # api request
        r = requests.get(url)
        wdic = json.loads(r.text)
        wtmp = wdic["current"]["temp_c"]
        wvind = wdic["current"]["wind_kph"]
        cloudy = wdic["current"]["cloud"]
        humidity = wdic["current"]["humidity"]
    except Exception as e:
        print(f"API request fails: {e}")
        return render_template("index.html", error="API request failed")  # Handle API errors in the template

    # Get and display the current time and date for the specified location
    current_time_date = get_time_date(user_location)

    # print weather data into console.
    print(f"The current weather in {user_location} is {wtmp} degress \nWind is {wvind} miles per hour \nCloud Cover {cloudy}% \nHumidity {humidity}%")

    return render_template("index.html", user_location=user_location, current_time_date=current_time_date, wtmp=wtmp, wvind=wvind, cloudy=cloudy, humidity=humidity)


app.run(debug=True, port=5001)
