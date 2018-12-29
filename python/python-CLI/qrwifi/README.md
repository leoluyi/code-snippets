# QR-Wifi: Python in the Command Line on Click

- https://kite.com/blog/python/python-command-line-click-tutorial
- [QR-code for Wi-Fi Network config (Android, iOS 11+)](https://github.com/zxing/zxing/wiki/Barcode-Contents#wifi-network-config-android)

Generating a 3D QR code of WIFI password

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
