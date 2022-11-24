import pytest


@pytest.mark.skip
def test_hello(setup):
    print("Hello World!")


def test_morning():
    print("Good Morning!")


def test_cross_browser(cross_browser):
    print(cross_browser)
    print(cross_browser[2])

