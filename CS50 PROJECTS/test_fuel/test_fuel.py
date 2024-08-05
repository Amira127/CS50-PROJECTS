import pytest
from fuel import convert, gauge

def test_valid():
    assert convert("1/2") == 50
    assert gauge(1) == "E"
    assert gauge(99) == "F"

def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:
        convert("5/0")

def test_ValueError():
    with pytest.raises(ValueError) as excinfo:
        convert("cat/dog")
        convert("5/2")

def test_gauge():
    assert gauge(0.5) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"