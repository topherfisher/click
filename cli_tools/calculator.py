# calculator.py

import click


@click.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def add(x, y):
    """Adds numbers."""
    click.echo(x + y)


@click.command()
@click.argument("x", type=int)
@click.argument("y", type=int)
def subtract(x, y):
    """Subtracts numbers."""
    click.echo(x - y)


####
# to use multiple numbers with having multiple variables:
####


@click.command()
@click.argument("xs", type=int, nargs=-1)
@click.option("-v", "--verbose", help="Show additional output.", is_flag=True)
def add_many(xs, verbose):
    """Adds multiple numbers."""
    if verbose:
        click.echo(f"{' + '.join(str(x) for x in xs)} = {sum(xs)}")
    else:
        click.echo(sum(xs))


@click.command()
@click.argument("xs", type=int, nargs=-1)
@click.option("-v", "--verbose", help="Show additional output.", is_flag=True)
def subtract_many(xs, verbose):
    """Subtracts multiple numbers."""
    results = xs[0]
    for x in xs[1:]:
        results -= xs

    if verbose:
        click.echo(f"{' - '.join(str(x) for x in xs)} = {sum(xs)}")
    else:
        click.echo(results)


if __name__ == "__main__":
    # add()
    # subtract()
    add_many()
    # subtract_many()
