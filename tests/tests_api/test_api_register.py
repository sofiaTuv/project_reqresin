import pytest
import requests
import jsonschema

from config import URL
from utils.load_schema import load_schema


@pytest.mark.api
class TestRegisterUser:
    @pytest.mark.parametrize('email, password, status_code',
                             [('eve.holt@reqres.in', 'pistol', 200),
                              ('eve.holt@reqres.in', None, 400)])
    @pytest.mark.register
    def test_register_user_fail(self, email, password, status_code):
        response = requests.post(f'{URL}api/register', json={
            'email': email,
            'password': password
        })

        assert response.status_code == status_code
        data = response.json()
        jsonschema.validate(data, load_schema('register.json'))
