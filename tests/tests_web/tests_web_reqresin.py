import jsonschema
import json
import pytest
from config import URL
from page.methods_page import MethodsPage
from utils.load_schema import load_schema


@pytest.mark.web
class TestsWeb:
    def test_get_list_users_web(self, browser):
        browser.get(URL)
        page = MethodsPage(browser)
        page.execute('List users')
        assert page.element_request() == '/api/users?page=2'
        assert page.response_code() == '200'
        content = page.response_content()
        jsonschema.validate(json.loads(content), load_schema('get_list_users.json'))
