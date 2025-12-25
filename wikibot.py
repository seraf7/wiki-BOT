import click
from mylib.bot import scrape

@click.command()
@click.option("--term", help="Termino que se quiere buscar")
@click.option("--orac", help="Cantidad de oraciones en el resultado")
def cli(term, orac):
    resultado = scrape(term, orac)
    click.echo(click.style(f"{resultado}:", fg="cyan"))

if __name__ == "__main__":
    cli()