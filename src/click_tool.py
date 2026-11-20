"""CLI-утиліта з командою say, створена за допомогою Click."""

import click


@click.group()
def cli() -> None:
    """Прості команди з використанням бібліотеки Click."""


@cli.command()
@click.option("--name", required=True, help="Ім'я, яке потрібно перевірити.")
def say(name: str) -> None:
    """Вивести ім'я, якщо воно не починається на p або P."""
    if name.lower().startswith("p"):
        click.echo("Ім’я не підходить")
    else:
        click.echo(name)


if __name__ == "__main__":
    cli()
