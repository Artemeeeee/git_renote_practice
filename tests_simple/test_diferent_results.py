def test_ok():
    assert True

def test_fail():
    assert False

def test_error():
    raise ValueError("Ошибка")

def test_sum():
    assert 2+2 == 4

def test_wrong_sum():
    assert 2+2 == 5