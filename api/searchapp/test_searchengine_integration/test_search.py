from searchengine import Engine


def test_simple_search():
    engine = Engine()
    result = engine.search("user:osarabia", "user")
    assert len(result) == 2
    assert isinstance(result[0], str)
    assert isinstance(result[1], list)