from app.weather_app import display_forecast

def test_weather_app():
    assert display_forecast() == 200