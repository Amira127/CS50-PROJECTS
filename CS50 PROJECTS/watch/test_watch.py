from watch import parse

def test_short_link():
    assert parse('<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"

def test_long_link():
    longLink='<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
    assert parse(longLink) == "https://youtu.be/xvFZjo5PgG0"


def test_invalid_link():
    assert parse('<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None



