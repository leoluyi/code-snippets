import os
import sys
import dotenv
from pathlib import Path

is_local = os.path.split(os.getcwd())[-1] == 'bin'
if is_local:
    print(f'(Local execution {__file__})')
    from context import qrwifi

    '''Fix click encoding error in venv by setting environment variables manually:
    RuntimeError: Click will abort further execution because Python 3 was
    configured to use ASCII as encoding for the environment.
    '''
    env_path = (Path(__file__).parent / '../.env').resolve()
    dotenv.load_dotenv(dotenv_path=env_path, verbose=True)

from qrwifi.cli import cli

if __name__ == '__main__':
    if is_local:

        argv = ['--ssid', os.environ['ssid'],
                '--security', 'WPA',
                '--password', os.environ['pwd'],
                'terminal']

        sys.argv.extend(argv)
        print('sys.argv:')
        print(sys.argv)
        sys.exit(cli())
    else:
        sys.exit(cli())
