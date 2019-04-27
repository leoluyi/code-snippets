import click
from qrwifi.functions import wifi_qr

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(name='qrwifi', context_settings=CONTEXT_SETTINGS)
@click.option("--ssid", help="WiFi network name.")
@click.option("--security", type=click.Choice(["WEP", "WPA", ""]))
@click.option("--password", help="WiFi password.")
@click.pass_context
def main(ctx, ssid: str, security: str = "", password: str = ""):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `qrwifi()` function below)
    # http://click.palletsprojects.com/en/7.x/commands/#nested-handling-and-contexts
    ctx.ensure_object(dict)

    qr = wifi_qr(ssid=ssid, security=security, password=password)

    ctx.obj["qr"] = qr
    ctx.obj["ssid"] = ssid
    ctx.obj["security"] = security
    ctx.obj["password"] = password


@main.command()
@click.pass_context
def terminal(ctx):
    print(ctx.obj["qr"].terminal())


@main.command()
@click.option("--filename", help="full path to the png file")
@click.pass_context
def png(ctx, filename, scale: int = 10):
    ctx.obj["qr"].png(filename, scale)


def cli(*args, **kwargs):
    main(obj=dict(), *args, **kwargs)


if __name__ == "__main__":
    cli()
