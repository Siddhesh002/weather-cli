from setuptools import setup

setup(
    name="weather_cli",
    version="0.1",
    packages=["weather_cli"],
    entry_points="""
        [console_scripts]
        cliw=weather_cli.get_weather:cliw
    """
)
