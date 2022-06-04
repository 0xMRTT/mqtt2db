"""Console script for mqtt2db."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for mqtt2db."""
    click.echo("Replace this message by putting your code into " "mqtt2db.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
