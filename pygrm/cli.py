"""
The Command Line Interface for pygrm
"""
import sys

import click


@click.command
def main():
    click.echo("This is the main program")
    return 0


if __name__ == "__main__":
    sys.exit(main())
