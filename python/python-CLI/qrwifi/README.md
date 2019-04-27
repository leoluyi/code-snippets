# QR-Wifi: Python in the Command Line on Click

CLI on [Click](https://click.palletsprojects.com/en/7.x/) that generates a 3D QR code of WIFI password

## Getting started

```bash
$ pipenv install --skip-lock
$ pipenv run python -um bin.qrwifi --help

# or

$ pipenv run python -um qrwifi -h
```

```
Usage: qrwifi.py [OPTIONS] COMMAND [ARGS]...

Options:
  --ssid TEXT            WiFi network name.
  --security [WEP|WPA|]
  --password TEXT        WiFi password.
  --help                 Show this message and exit.

Commands:
  png
  terminal
```

## Project structure

```
.
├── Pipfile
├── README.md
├── bin
│   ├── context.py
│   └── qrwifi.py
├── qrwifi
│   ├── __init__.py
│   ├── cli.py
│   └── functions.py
└── setup.py
```

## QR-code for Wifi

```
WIFI:T:WPA;S:mynetwork;P:mypass;;
```

## References

- https://kite.com/blog/python/python-command-line-click-tutorial
- [QR-code for Wi-Fi Network config (Android, iOS 11+)](https://github.com/zxing/zxing/wiki/Barcode-Contents#wifi-network-config-android)
