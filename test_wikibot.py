from mylib.bot import scrape
from wikibot import cli
from click.testing import CliRunner

def test_scrape():
    assert "Sucker Punch" in scrape("Sucker Punch film")

def test_wikibot():
    runner = CliRunner()
    resultado = runner.invoke(
        cli, ["--term", "Sucker Punch film", "--orac", 3])
    assert resultado.exit_code == 0
    assert "Sucker Punch" in resultado.output