import pytest

from pytestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("data_load")
class TestExample2(BaseClass):

    def test_edit_profile(self, data_load):
        log = self.getLogger()
        log.info(data_load[0])
        log.info(data_load[2])
