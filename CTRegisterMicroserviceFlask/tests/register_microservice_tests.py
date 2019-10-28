import os

import pytest
import requests_mock

import CTRegisterMicroserviceFlask


@pytest.fixture
def validate_env():
    if not os.getenv('CT_URL'):
        raise Exception('CT_URL needs to be set')
    if not os.getenv('CT_TOKEN'):
        raise Exception('CT_TOKEN needs to be set')


@requests_mock.mock(kw='mocker')
def test_microservice_register(mocker):
    post_calls = mocker.post(os.getenv('CT_URL') + '/api/v1/microservice', json={})

    CTRegisterMicroserviceFlask.ct_register('test app', os.getenv('CT_URL'), 'http://local-url.com', True)

    assert post_calls.call_count == 1
    assert post_calls.called
    assert post_calls.last_request.text == '{"name": "test app", "url": "http://local-url.com", "active": true}'
