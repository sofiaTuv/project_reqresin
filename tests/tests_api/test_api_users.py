import pytest
import requests
import jsonschema

from config import URL
from utils.load_schema import load_schema


@pytest.mark.api
class TestUsersApi:
    @pytest.mark.parametrize('page', [(2)])
    @pytest.mark.get_list
    def test_get_list_users_returns_users(self, page):
        response = requests.get(f'{URL}api/users?page={page}')
        per_page = 6

        assert response.status_code == 200
        data = response.json()
        jsonschema.validate(data, load_schema('get_list_users.json'))
        assert data['page'] == page
        assert len(data['data']) == per_page

    @pytest.mark.parametrize('user_id, status_code, schema', [(2, 200, 'get_user.json'),
                                                             (333, 404, 'get_user_fail.json')])
    @pytest.mark.get
    def test_get_user(self, user_id, status_code, schema):
        response = requests.get(f'{URL}api/users/{user_id}')

        assert response.status_code == status_code
        jsonschema.validate(response.json(), load_schema(schema))

    @pytest.mark.parametrize('name, job', [('morpheus', 'leader')])
    @pytest.mark.create
    def test_create_user(self, name, job):
        response = requests.post(f'{URL}api/users', json={
            'name': name,
            'job': job
        })

        assert response.status_code == 201
        data = response.json()
        assert data['name'] == name
        assert data['job'] == job
        jsonschema.validate(data, load_schema('create_user.json'))

    @pytest.mark.parametrize('name, job', [('morpheus', 'zion resident')])
    @pytest.mark.update
    def test_update_user(self, name, job):
        response = requests.put(f'{URL}api/users/2', json={
            'name': name,
            'job': job
        })

        assert response.status_code == 200
        data = response.json()
        assert data['name'] == name
        assert data['job'] == job
        jsonschema.validate(data, load_schema('update_user.json'))

    @pytest.mark.delete
    def test_delete_user(self):
        user_id = 2
        response = requests.delete(f'{URL}api/users/{user_id}')

        assert response.status_code == 204
