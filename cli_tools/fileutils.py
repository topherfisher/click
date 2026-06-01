# fileutils.py

import click
import typing
import requests


@click.command()
@click.argument("file_output", type=click.File("a"))  # a = append
def note(file_output: typing.IO):
    """Write notes input to given file."""
    click.echo("Enter lines of text below and CTRL+C to exit.")
    try:
        while True:
            value = click.prompt("", prompt_suffix=">")
            file_output.write(f"{value}\n")
    except click.Abort:
        click.echo(f"\nOutput written to file {file_output.name}")


@click.command()
@click.argument("inputs", type=click.File("r"), nargs=-1)  # r = read only
@click.argument("output", type=click.File("w"))  # w = write
def concat(inputs: typing.Collection[typing.IO], output: typing.IO):
    """Concatenates the contents of one or more files into an output file."""
    for f in inputs:
        for line in f:
            output.write(line)
        click.echo(f"{f.name} written to {output.name}")


@click.command()
@click.argument("inputs", nargs=-1)
def download(inputs):
    """Downloads web resources from (url, filename) input pairs.
    Example:
        download http://xyz.com/p1.txt,page1.txt http://xyz.com/p2.txt,page2.txt

        This fetches web resources by url and saves them locally to filename.

    python3 fileutils.py https://www.gutenberg.org/files/98/98-0.txt,tale-of-two-cities.txt https://www.gutenberg.org/files/1400/1400-0.txt,great-expectations.txt
    """
    # with click.progressbar(inputs) as bar:
    with click.progressbar(
        length=len(inputs),
        show_eta=False,
        item_show_func=lambda fname: f"Downloading {fname}",
    ) as bar:
        # for item in bar:
        for i, item in enumerate(inputs):
            url, file_name = item.split(",")
            response = requests.get(url)
            with open(file_name, "w") as fo:
                fo.write(response.text)
            bar.update(1)

    click.echo("Download complete!")


if __name__ == "__main__":
    # note()
    # concat()
    download()
