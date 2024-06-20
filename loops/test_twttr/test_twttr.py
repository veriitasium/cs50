# pip3 install pytest

from twttr import shorten

def test_casesensitiveness():
    assert shorten("TwittEr") == "Twttr"
    assert shorten("TwItter") == "Twttr"

def test_strips():
    assert shorten("   What's your name?  ") == "Wht's yr nm?"

def test_without_vowels():
    assert shorten("CS50") == "CS50"