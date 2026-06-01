import click
import json
import os
from datetime import datetime
import calendar

# path to the JSON file where events will be stored
DB_FILE = "/home/chris-fisher/click_training/calendar_events.json"


def load_events():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}


def save_events(events):
    with open(DB_FILE, "w") as f:
        json.dump(events, f, indent=4)


@click.group()
def cli():
    """A customizable CLI calendar with events."""
    pass


@cli.command()
@click.argument("date")
@click.argument("description")
def add(date, description):
    """"""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}


def save_events(events):
    with open(DB_FILE, "w") as f:
        json.dump(events, f, indent=4)


@click.group()
def cli():
    """A customizable CLI calendar with events."""
    pass


@cli.command()
@click.argument("date")
@click.argument("description")
def add(date, description):
    """Add an event (Date format: YYYY-MM-DD)."""
    try:
        # validate date format
        datetime.strptime(date, "%Y-%m-%d")
        events = load_events()
        if date not in events:
            events[date] = []
        events[date].append(description)
        save_events(events)
        click.echo(f"Successfully added event: '{description}' on {date}")
    except ValueError:
        click.echo("Error: Please use the YYYY-MM-DD date format.")


@cli.command()
@click.option("--month", default=datetime.now().month, help="Month as a number (1-12)")
@click.option("--year", default=datetime.now().year, help="Four digit year")
def view(month, year):
    """View the calendar and events for a specific month."""
    events = load_events()

    # display the text based calendar grid
    click.echo(f"\not{calendar.month(year, month)}")

    # filter and display events for the chosen month
    click.echo(f"--- Events for {year}-{month:02d} ---")
    found = False
    for date_str, descriptions in sorted(events.items()):
        event_date = datetime.strptime(date_str, "%Y-%m-%d")
        if event_date.year == year and event_date.month == month:
            found = True
            for desc in descriptions:
                click.echo(f" - [{date_str}] {desc}")

    if not found:
        click.echo("No events scheduled for this month.")


if __name__ == "__main__":
    cli()
