from weather import current_weather
import click
import os
import re


class ApiKey(click.ParamType):
    name = 'api-key'

    def convert(self, value, param, ctx):
        found = re.match(r'[0-9a-f]{32}', value)

        if not found:
            self.fail(
                f'{value} is not a 32-character hexadecimal string',
                param,
                ctx,
            )

        return value


@click.group()
@click.option(
    '--api-key', '-a',
    type=ApiKey(),
    help='your API key for the OpenWeatherMap API',
)
@click.option(
    '--config-file', '-c',
    type=click.Path(),
    default='./.weather.cfg',
)
@click.pass_context
def main(ctx, api_key, config_file):
    """
    A little weather tool that shows you the current weather in a LOCATION of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:
    1. London,UK
    2. Canmore
    You need a valid API key from OpenWeatherMap for the tool to work. You can
    sign up for a free account at https://openweathermap.org/appid.
    """
    filename = os.path.expanduser(config_file)

    if not api_key and os.path.exists(filename):
        with open(filename) as cfg:
            api_key = cfg.read()

    ctx.obj = {
        'api_key': api_key,
        'config_file': filename,
    }


@main.command()
@click.pass_context
def config(ctx):
    """
    Store configuration values in a file, e.g. the API key for OpenWeatherMap.
    """
    config_file = ctx.obj['config_file']

    api_key = click.prompt(
        "Please enter your API key",
        default=ctx.obj.get('api_key', '')
    )

    with open(config_file, 'w') as cfg:
        cfg.write(api_key)


@main.command()
@click.argument('location')
@click.pass_context
def current(ctx, location):
    """
    Show the current weather for a location using OpenWeatherMap data.
    """
    api_key = ctx.obj['api_key']

    weather = current_weather(location, api_key)
    print(f"The weather in {location} right now: <{weather[0]}> | Temp: {weather[1]} ({weather[2]}~{weather[3]}).")


if __name__ == "__main__":
    main()
