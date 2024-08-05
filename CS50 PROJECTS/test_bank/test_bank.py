from bank import value


def test_hello():
    assert value("HELLO sir") == 0
    assert value("hello sir") == 0
    assert value("Hello sir") == 0
    assert value("HeLLo sir") == 0


def test_h():
    assert value("hi sir!") == 20
    assert value("  hhh, sir") == 20
    assert value("hann sir") == 20


def test_otherwise():
    assert value("What's up?") == 100
    assert value("Come on") == 100
    