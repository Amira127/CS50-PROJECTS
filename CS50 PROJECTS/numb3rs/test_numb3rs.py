from numb3rs import validate

def test_string():
    assert validate("cat") == False
    assert validate("my ip is 12.5.3.9") == False

def test_white_space():
    assert validate("12 . 3 . 4 .110") == False
    assert validate("85.6.9.10") == True

def test_not_between_0_and_255():
    assert validate ("1110.9.10.7") == False
    assert validate ("256.3.9.7") == False
    assert validate ("2.256.256.256") == False

def test_format():
    assert validate("12.3.4.255.10") == False
    assert validate ("0.0.0") == False

def test_particular_situation():
    assert validate ("255.255.255.255") == True
    assert validate ("0.0.0.0") == True




