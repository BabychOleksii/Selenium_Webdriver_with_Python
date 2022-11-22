import pytest


@pytest.mark.skip
def test_program():
    msg = "Hello!"
    assert msg == "Hi", "Test failed because string do not match"


@pytest.mark.xfail
def test_second_card():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

