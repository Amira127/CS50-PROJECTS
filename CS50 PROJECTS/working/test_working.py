from working import convert
import pytest

def test_invalid_time():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("cat")

def test_omits_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_invalid_structure():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("10Am to 5Pm")
    with pytest.raises(ValueError):
        convert("10 am to 2 pm")

def test_valid_AM_to_PM():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_valid_PM_to_AM():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

