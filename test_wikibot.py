from wikibot import scrape

def test_scrape():
    assert "Sucker Punch" in scrape("Sucker Punch film")