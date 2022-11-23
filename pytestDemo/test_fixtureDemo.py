import pytest


@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixture_demo(self):
        print("I will execute steps in fixture_demo method")

    def test_fixture_demo1(self):
        print("I will execute steps in fixture_demo1 method")

    def test_fixture_demo2(self):
        print("I will execute steps in fixture_demo2 method")


