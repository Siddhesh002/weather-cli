<center>

# CLI for Weather

</center>

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [How to use](#usage)

## Demo

<img src="demo/img.png" width="600" height="150" />

## About <a name = "about"></a>

The Weather Pilot CLI is a command line interface that provides weather information for a specific location. The [OpenWeather API](https://openweathermap.org/api)is used to create the CLI. The [Click](https://click.palletsprojects.com/en/7.x/) library is used to create the CLI.

## Getting Started <a name = "getting_started"></a>

Follow the below instructions to get this project running on your local machine for development and testing purposes.

cloning the repository

```bash
git clone https://github.com/mahimairaja/weather-pilot-cli.git
```

change directory

```bash
cd weather-cli
```

### Requirement

Before installing, you must first obtain an API key from[OpenWeather](https://openweathermap.org/api). You can install the CLI once you have your API key.

Then add your API key to the .env file

```bash
echo "API_KEY=your_api_key" >> weather_cli/.env
```

### Instalations

> A step-by-step series of examples that demonstrate how to set up a development environment.

Create a virtual environment using [venv](https://docs.python.org/3/library/venv.html) or [virtualenv](https://virtualenv.pypa.io/en/latest/).

```bash
python3 -m venv venv
```

Activate the virtual environment.

```bash
source venv/bin/activate
```

Install the requirements.

```bash
pip install -r requirements.txt
```

Install the CLI.

```bash
pip install -e .
```

## How to use <a name = "usage"></a>

get the current weather for a given location

```bash
cliw --city CITY_NAME
```

> NOTE : This Procedure is based on Linux environment.

Thank you visiting !
