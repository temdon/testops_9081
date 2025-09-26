__author__ = 'Artem Kolesnichenko'
__date__ = '26.09.2025'

import allure
import pytest


@allure.label('component', 'S3 service')
@allure.feature('S3 protocol')
@allure.story('Other', 'Versioning')
@pytest.mark.versioning
@pytest.mark.no_upload_session
@allure.testcase(url='https://objectfirst.atlassian.net/browse/QQ-1443', name='QQ-1443')
@allure.title('Clear ObjectLockConfiguration rules')
def test_clear_object_lock_config_rules():
    """None

    **Command example**::

        # TODO

    Setup:
        - None

    Test Body:
        - None

    Teardown:
        - None
    """

    with allure.step('Title'):
        pass
