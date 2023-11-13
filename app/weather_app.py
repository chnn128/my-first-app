from pgeocode import Nominatim

import requests
import json

from pandas import DataFrame

# display images in a dataframe in colab
# ... h/t: https://towardsdatascience.com/rendering-images-inside-a-pandas-dataframe-3631a4883f6
from IPython.core.display import HTML
from IPython.display import Image, display


def to_image(url):
    return '<img src="'+ url + '" width="32" >'


def chopped_date(start_time):
    return start_time[5:10]


def degree_sign():
    return u"\N{DEGREE SIGN}"


def dashed_line():
    print(str("-------------"))
    return str("-------------")


def get_and_display_location_detail(zip_code = 20057, country_code = "US"):
    nomi = Nominatim(country_code)
    geo = nomi.query_postal_code(zip_code)

    renamed_geo = geo[['place_name', 'state_name', 'postal_code', 'county_name']]
    renamed_geo = renamed_geo.rename(index={'place_name': 'Place', 'state_name': 'State', 'postal_code': 'Zip Code', 'county_name': 'County'})
    print(f" City: {renamed_geo['Place']}\n State: {renamed_geo['State']}\n Zip Code: {renamed_geo['Zip Code']}\n County: {renamed_geo['County']}")
    #print(renamed_geo[['Place', 'State', 'Zip Code', 'County']])
    
    return geo


def request_and_clean_data(geo):
    
    latitude = geo["latitude"]
    longitude = geo["longitude"]

    request_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    response = requests.get(request_url)
    #print(response.status_code)
    parsed_response = json.loads(response.text)


    forecast_url = parsed_response["properties"]["forecast"]
    forecast_response = requests.get(forecast_url)
    #print(forecast_response.status_code)
    parsed_forecast_response = json.loads(forecast_response.text)

    periods = parsed_forecast_response["properties"]["periods"]
    daytime_periods = [period for period in periods if period["isDaytime"] == True]

    return [daytime_periods, forecast_response.status_code]


def forecast_demo(zip_code = 20057, country_code="US"):
    """
    Displays a seven day weather forecast for the provided zip code.

    Params :

        country_code (str) a valid country code (see supported country codes list). Default is "US".

        zip_code (str) a valid US zip code, like "20057" or "06510".

    """
    geo = get_and_display_location_detail(zip_code)
    daytime_periods = request_and_clean_data(geo)[0]


    #for period in daytime_periods:
    #    #print(period.keys())
    #    dashed_line()
    #    print(period["name"], period["startTime"][0:7])
    #    print(period["shortForecast"], f"{period['temperature']} {degree_sign()}{period['temperatureUnit']}")
    #    #print(period["detailedForecast"])
    #    display(Image(url=period["icon"]))

    df = DataFrame(daytime_periods)

    df["date"] = df["startTime"].apply(chopped_date)

    # df["img"] = df["icon"].apply(to_image)

    # combined column for temp display
    # ... h/t: https://stackoverflow.com/questions/19377969/combine-two-columns-of-text-in-pandas-dataframe
    df["temp"] = df["temperature"].astype(str) + " " + degree_sign() + df["temperatureUnit"]

    # rename cols:
    df.rename(columns={
        "name":"day",
        "shortForecast": "forecast"
    }, inplace=True)

    # drop unused cols:
    df.drop(columns=[
        "temperature", "temperatureUnit", "temperatureTrend",
        "windSpeed", "windDirection",
        "startTime", "endTime",
        "number", "isDaytime", "detailedForecast"
    ], inplace=True)

    # re-order columns:
    df = df.reindex(columns=['day', 'date', 'temp', 'forecast', 'icon'])

    # return df
    dashed_line()
    print("SEVEN DAY FORECAST")
    print("LOCATION:", f"{geo.place_name}, {geo.state_code}".upper())
    dashed_line()

    return HTML(df.to_html(escape=False, formatters=dict(icon=to_image)))


def display_forecast(zip_code = 20057, country_code="US"):
    """
    Displays a seven day weather forecast for the provided zip code.

    Params :

        country_code (str) a valid country code (see supported country codes list). Default is "US".

        zip_code (str) a valid US zip code, like "20057" or "06510".

    """
    #print(zip_code)

    geo = get_and_display_location_detail(zip_code)
    data_pull_response = request_and_clean_data(geo)

    daytime_periods = data_pull_response[0]
    request_response_code = data_pull_response[1]

    for period in daytime_periods:
        #print(period.keys())
        dashed_line()
        print(period["name"], period["startTime"][0:7])
        print(period["shortForecast"], f"{period['temperature']} {degree_sign()}{period['temperatureUnit']}")
        #print(period["detailedForecast"])
        display(Image(url=period["icon"]))

    return request_response_code

if __name__ == "__main__":
    zip_entered = input("Please enter a zip code: ")
    display_forecast(zip_code=str(zip_entered))
    #forecast_demo(str(zip_entered))

