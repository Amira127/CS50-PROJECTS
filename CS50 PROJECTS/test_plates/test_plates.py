from plates import is_valid

def test_beginning_alphabetical():
    assert is_valid("A111") == False
    assert is_valid("D511") == False
    assert is_valid("HI") == True

def test_length():
    assert is_valid("A") == False
    assert is_valid("MA") == True
    assert is_valid("AAAAAAAAA") == False
    assert is_valid("HELLOO") == True

def test_number_placement():
    assert is_valid("HI1SIR") == False
    assert is_valid("AAA11") == True

def test_zero_placement():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_contains_illegal_character():
    assert is_valid("HI!") == False
    assert is_valid("HI?") == False
