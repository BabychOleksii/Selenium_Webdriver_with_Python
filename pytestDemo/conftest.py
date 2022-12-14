import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will executed last")


@pytest.fixture()
def data_load():
    print("User profile data is being created.")
    return ["Alex", "Babych", "Welcome on a board."]


@pytest.fixture(params=[("chrome", "Alex", "Canada"), "firefox", "edge"])
def cross_browser(request):
    return request.param

