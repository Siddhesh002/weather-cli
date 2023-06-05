import click
import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path
from geopy.geocoders import Nominatim
from datetime import datetime

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

if __name__ == "__main__":
    api_key = os.getenv('API_KEY')


@click.command()
@click.option("--city", prompt="City name", help="Enter city name")
def cliw(city):
    """Display the weather of a city."""
    
    data = getWeather(city)
   
    loc_data = get_loc_data(data['coord'])
    
    weather = data['weather'][0]['description']
    temp = data['main']['temp'] - 273.15
    click.echo("Searching....\n")
    click.echo(f"{city},{loc_data['state']},{loc_data['country']}")
    
    current_date = datetime.now()
    current_day = current_date.strftime("%A")
    current_time_formatted = current_date.strftime("%H:%M")
    click.echo(f'{current_day}, {current_time_formatted}')
    
    click.echo(f"\n-Temperature: {temp : .2f}•C")
    click.echo(f"-Atmospheric Pressure: {data['main']['pressure']} mbar")
    click.echo(f"-Humidity: {data['main']['humidity']} %")
    click.echo(f"-Description : {weather}")
    
    click.echo(f'\nHave a Nice Day:)')

@click.group()
def cli():
    pass


def getWeather(city):
    api_key = os.getenv('API_KEY')
    link = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"
    response = requests.get(link)
    data = json.loads(response.text)
    return data

def get_loc_data(coord):
    Latitude = coord['lat']
    Longitude = coord['lon']
    
    geolocator = Nominatim(user_agent="weather_cli")
    location = geolocator.reverse(f"{Latitude}, {Longitude}")
    
    return location.raw['address']

if __name__ == "__main__":
    cli.add_command(cliw)
