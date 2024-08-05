from um import count

def test_um_middle_word():
    assert count("instrumentation") == 0
    assert count("humanitarianism") == 0

def test_um_last_word():
    assert count("cryptosporidium") == 0
    assert count ("enterobacterium") == 0

def test_Um():
    assert count("Um, thanks for the album.") == 1
    assert count ("Um, thanks, um...") == 2

def test_none_um():
    assert count("Hi,cs50!") == 0
    assert count("1254!!?") == 0

def test_um_punctuation():
    assert count("um?") == 1
