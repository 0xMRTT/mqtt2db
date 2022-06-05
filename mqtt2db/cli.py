"""Console script for mqtt2db."""
import sys
import click


def logo():
    click.echo(
        """
=========================================
 ____   ____  ____  __________ __________
/  _ \_/ _  \/ __ \ |___  ___| |___  ___|
| | \   / | | /  \ |    | |        | |
| |  \_/  | | \__/ |    | |        | |
|_|       |_|\_____ \   |_|        |_|

    ------- MQTT2DB by @0xMRTT -------
    https://github.com/0xMRTT/MQTT2DB

=========================================

"""
    )


@click.group()
def main():
    logo()

@main.command()
def run():
    logo()

@main.group()
def config():
    pass

from .mqtt2db import config_get, config_set
@config.command()
def get(key):
    config_get(key)

@config.command()
def set(key, value):
    config_set(key, value)



if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
