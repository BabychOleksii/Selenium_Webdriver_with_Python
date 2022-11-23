import pytest


@pytest.fixture()
def setup():
    print("I will be executed first")
    yield
    print("I will executed last")


def test_fixture_demo(setup):
    print("I will execute steps in fixture_demo method")

