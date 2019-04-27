# Mastering Click: Writing Advanced Python Command-Line Apps -- dbader.org

https://dbader.org/blog/mastering-click-advanced-python-command-line-apps

## Get Started

```bash
$ pipenv install

# Store the API key in a configuration file using another sub-command
$ pipenv run python cli.py config

# Show you the current weather
$ pipenv run python cli.py current Taipei
```

```
$ pipenv run python cli.py --help

Usage: cli.py [OPTIONS] COMMAND [ARGS]...

  A little weather tool that shows you the current weather in a LOCATION of
  your choice. Provide the city name and optionally a two-digit country
  code. Here are two examples: 1. London,UK 2. Canmore You need a valid API
  key from OpenWeatherMap for the tool to work. You can sign up for a free
  account at https://openweathermap.org/appid.

Options:
  -a, --api-key API-KEY   your API key for the OpenWeatherMap API
  -c, --config-file PATH
  --help                  Show this message and exit.

Commands:
  config   Store configuration values in a file, e.g.
  current  Show the current weather for a location using OpenWeatherMap...
```

## Advanced Python CLIs with Click --- Summary

- How to read parameter values from environment variables.
- How you can separate functionality into separate commands.
- How to ask the user for input on the command-line.
- What parameter types are in Click and how you can use them for input validation.
- How Click contexts can help you share data between commands.
