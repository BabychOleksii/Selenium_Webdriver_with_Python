import pytest


@pytest.mark.usefixtures("data_load")
class TestExample2:

    def test_edit_profile(self, data_load):
        print(data_load)
        print(data_load[2])

