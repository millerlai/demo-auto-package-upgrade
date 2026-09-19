from calc import sub


def test_sub_positive_numbers():
    assert sub(5, 2) == 3


def test_sub_negative_numbers():
    assert sub(-5, -2) == -3


def test_sub_zero_and_positive_number():
    assert sub(0, 2) == -2
