import click


@click.group()
def cli() -> None:

@cli.command()
@click.option("--name", required=True, help="Ім'я, яке потрібно перевірити.")
def say(name: str) -> None:
    if name.lower().startswith("p"):
        click.echo("Ім’я не підходить")
    else:
        click.echo(name)


if __name__ == "__main__":
    cli()
