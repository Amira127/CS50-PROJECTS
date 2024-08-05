from twttr import shorten


def test_lowercase():
    assert shorten("name") == "nm"
    assert shorten("world") == "wrld"


def test_uppercase():
    assert shorten("AMIRA") == "MR"
    assert shorten("HELLO") == "HLL"

def test_numbers():
    assert shorten ("123") == "123"
    assert shorten ("0") == "0"
    assert shorten ("-9") == "-9"

def test_punctuation():
    assert shorten ("!?,") == "!?,"

def test_various():
    assert shorten("Hello_World!") == "Hll_Wrld!"
    assert shorten("Cs50") == "Cs50"
    assert shorten("1/2/3") == "1/2/3"
