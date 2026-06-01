# hello.py

import click


@click.command()
@click.option(
    "--name", default="World", help="The person to greet."
)  # provides a default value if no name provided
# @click.argument('name') # done this way, it will error if a name is not provided, unlike above where we have a default if no name input
@click.option(
    "--lang",
    help="Specify a language English (en) or Spanish (es)",
    default="en",
    type=click.Choice(["es", "en"]),
)
@click.option("--say-it", type=int, default=1, help="Number of times to say greeting.")
def hello(name, lang, say_it):
    """Simple program that greets Name."""
    # if lang == 'es':
    #     greetings = 'Hola'
    # elif lang == 'en':
    #     greetings = 'Hello'
    # else:
    #     raise click.BadOptionUsage('lang', 'Unsupported language.')
    greetings = "Hello" if lang == "en" else "Hola"
    for _ in range(say_it):
        # click.echo(f"Hello, {name}!")
        click.secho(f"{greetings} {name}", fg = "blue", bold = True)


if __name__ == "__main__":
    hello()

"""
Examples for various options:
with @click.option -> python3 hello.py --name Chris
with @click.argument -> python3 hello.py Chris
"""
