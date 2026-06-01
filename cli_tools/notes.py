from pathlib import Path
from datetime import datetime

import click

NOTES_DB = Path.home() / ".notes" / "notes.txt"

DISPLAY_FMT = "{:<3} {:16} {:16} {:40}"


def print_header():
    click.echo(DISPLAY_FMT.format("ID", "Created", "Updated", "Contents"))
    click.echo(DISPLAY_FMT.format("-" * 3, "-" * 16, "-" * 16, "-" * 40))


def print_note(idx, note):
    created, updated, contents = note.split("\t")
    dt_frm = "%b-%d %I:%M %p"
    created = datetime.fromisoformat(created).strftime(dt_frm)
    updated = datetime.fromisoformat(updated).strftime(dt_frm)
    click.echo(DISPLAY_FMT.format(idx, created, updated, contents))


def load_notes():
    notes = []
    with open(NOTES_DB) as fo:
        for line in fo:
            notes.append(line.strip())
    return notes


def save_notes(notes):
    with open(NOTES_DB, "w") as fo:
        for note in notes:
            fo.write(f"{note}\n")


@click.group()
@click.pass_context
def main(ctx):
    """Program for managing notes."""
    if not NOTES_DB.parent.exists():
        NOTES_DB.parent.mkdir()
        NOTES_DB.touch()

    ctx.ensure_object(dict)

    ctx.obj["notes"] = load_notes()


@main.command()
@click.pass_context
def show(ctx):
    """Shows notes in notes database."""

    notes = ctx.obj["notes"]
    print_header()
    for i, note in enumerate(notes, start=1):
        print_note(i, note)


@main.command()
@click.pass_context
def add(ctx):
    """Adds note to notes database."""

    notes = ctx.obj["notes"]

    created = datetime.now().isoformat()
    contents = click.prompt("Note context")
    notes.append(f"{created}\t{created}\t{contents}")

    save_notes(notes)


@main.command()
@click.pass_context
def update(ctx):
    """Updates note in notes databse."""

    notes = ctx.obj["notes"]

    print_header()

    for i, note in enumerate(notes, start=1):
        print_note(i, note)

    idx = click.prompt("Index of note to update or -1 to exit", type=int)
    if idx == -1:
        return
    updated_content = click.prompt("Updated content")

    idx -= 1

    updated = datetime.now().isoformat()
    created = notes[idx].split("\t")[0]
    notes[idx] = f"{created}\t{updated}\t{updated_content}"

    save_notes(notes)


@main.command()
@click.pass_context
def delete(ctx):
    """Deletes note in notes database."""

    notes = ctx.obj["notes"]

    print_header()

    for i, note in enumerate(notes, start=1):
        print_note(i, note)

    idx = click.prompt("Index of note to delete or -1 to exit", type=int)
    if idx == -1:
        return

    idx -= 1

    notes.remove(notes[idx])

    save_notes(notes)


if __name__ == "__main__":
    main()
