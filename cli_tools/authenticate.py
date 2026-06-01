# authenticate.py

import click


@click.command()
@click.option("--username", prompt=True)
@click.option("--password", prompt=True, hide_input=True, confirmation_prompt=True)
def auth(username, password):
    """Provides user authentication."""
    username2 = click.prompt("username2")
    password2 = click.prompt("password2", hide_input=True, confirmation_prompt=True)

    if click.confirm("Are you an admin?"):
        admin_id = click.prompt("Admin ID", type=int, prompt_suffix=">")
        click.echo(f"Logging in admin {username} (ID = {admin_id})")
    else:
        click.echo(f"Logging in {username}")
    click.echo(f"Logging in {username2}")


if __name__ == "__main__":
    auth()
