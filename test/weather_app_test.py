from app.weather_app import display_forecast
from app.weather_app import get_and_display_location_detail
from app.weather_app import forecast_demo
from pandas import Series 
from IPython.core.display import HTML

def test_display_forecast():
    assert display_forecast() == 200

def test_forecast_demo():
    assert isinstance(forecast_demo(), HTML) == True
    #assert str(type(forecast_demo())) == "<class 'IPython.core.display.HTML'>"

def test_get_location_detail():
    assert isinstance(get_and_display_location_detail(), Series) == True