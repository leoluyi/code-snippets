import os
import sys

os.environ['LC_ALL'] = 'en_US.utf-8'
os.environ['LANG'] = 'en_US.utf-8'

is_local = os.path.split(os.getcwd())[-1] == 'bin'
if is_local:
    print(f'(Local execution {__file__})')
    from context import qrwifi

from qrwifi.cli import qrwifi

if __name__ == '__main__':
    if is_local:

        argv = ['--ssid', os.environ['ssid'],
                '--security', 'WPA',
                '--password', os.environ['pwd'],
                'terminal']

        sys.exit(qrwifi(argv))
    else:
        sys.exit(qrwifi())
