# Mastering Click: Writing Advanced Python Command-Line Apps -- dbader.org

https://dbader.org/blog/mastering-click-advanced-python-command-line-apps

## Get Started

```bash
$ pipenv install

# Store the API key in a configuration file using another sub-command
$ pipenv run python weather.py config

# Show you the current weather
$ pipenv run python weather.py current Taipei
```

## Advanced Python CLIs with Click --- Summary

- How to read parameter values from environment variables.
- How you can separate functionality into separate commands.
- How to ask the user for input on the command-line.
- What parameter types are in Click and how you can use them for input validation.
- How Click contexts can help you share data between commands.
