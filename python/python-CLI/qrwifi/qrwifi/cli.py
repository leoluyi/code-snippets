import click
from qrwifi.functions import wifi_qr


@click.group()
@click.option("--ssid", help="WiFi network name.")
@click.option("--security", type=click.Choice(["WEP", "WPA", ""]))
@click.option("--password", help="WiFi password.")
@click.pass_context
def main(ctx, ssid: str, security: str = "", password: str = ""):

    qr = wifi_qr(ssid=ssid, security=security, password=password)

    ctx.ensure_object(dict)
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


def qrwifi(*args, **kwargs):
    main(*args, **kwargs)


if __name__ == "__main__":
    qrwifi()
