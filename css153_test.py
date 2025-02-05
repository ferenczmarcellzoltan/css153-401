import pytest
from bs4 import BeautifulSoup

@pytest.fixture
def soup():
    # Open the index.html file for parsing
    with open("index.html", "r", encoding="utf-8") as file:
        content = file.read()
    return BeautifulSoup(content, "html.parser")

def test_body_background_color(soup):
    body_style = soup.find("style").string
    assert "background-color: aqua;" in body_style

def test_container_background_color(soup):
    container_style = soup.find("style").string
    assert "background-color: white;" in container_style

def test_bars_background_color(soup):
    bar_style = soup.find("style").string
    assert "background-color: darkmagenta;" in bar_style

def test_bars_border_color(soup):
    bar_style = soup.find("style").string
    assert "border-bottom: 5px solid gold;" in bar_style

def test_first_bar_width(soup):
    bar_style = soup.find("style").string
    assert ".bar:first-child {\\n            width: 50%;" in bar_style

def test_bars_height(soup):
    bar_style = soup.find("style").string
    assert "height: 30px;" in bar_style