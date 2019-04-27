import click
from qrwifi.functions import wifi_qr

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(name='qrwifi', context_settings=CONTEXT_SETTINGS)
@click.option("--ssid", help="WiFi network name.")
@click.option("--security", type=click.Choice(["WEP", "WPA", ""]))
@click.option("--password", help="WiFi password.")
@click.pass_context
def cli_entry_point(ctx, ssid: str, security: str = "", password: str = ""):
    '''Main qrwifi command.

    Arguments:
        ctx {[type]} -- [description]
        ssid {str} -- [description]

    Keyword Arguments:
        security {str} -- [description] (default: {""})
        password {str} -- [description] (default: {""})
    '''

    # ensure that ctx.obj exists and is a dict
    # (in case `cli()` is called by means other than the `qrwifi()` function below)
    # http://click.palletsprojects.com/en/7.x/commands/#nested-handling-and-contexts
    ctx.ensure_object(dict)

    qr = wifi_qr(ssid=ssid, security=security, password=password)

    ctx.obj["qr"] = qr
    ctx.obj["ssid"] = ssid
    ctx.obj["security"] = security
    ctx.obj["password"] = password


@cli_entry_point.command()
@click.pass_context
def terminal(ctx):
    print(ctx.obj["qr"].terminal())


@cli_entry_point.command()
@click.option("--filename", help="full path to the png file")
@click.pass_context
def png(ctx, filename, scale: int = 10):
    ctx.obj["qr"].png(filename, scale)


def cli(args=None):
    # https://click.palletsprojects.com/en/7.x/api/#click.BaseCommand.main
    cli_entry_point(args=args, prog_name='qrwifi', obj=dict())
    '''
    :args -- the arguments that should be used for parsing. If not provided, sys.argv[1:] is used.
    :prog_name -- the program name that should be used. By default the program name is constructed by taking the file name from sys.argv[0].
    :**extra -- "obj" is forwarded to the context constructor.
    '''
