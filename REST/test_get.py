import pytest
import requests
import json
import jsonpath

class Test:
    @pytest.mark.Sanity
    def test_dict_to_json(self):
        d='{"Name":"satheesh","Mobile":9989884111}'
        result=json.loads(d)
        print(result)

    @pytest.mark.Smoke
    def test_get_resource(self):
        uri = 'https://reqres.in/api/users?page=2'
        response=requests.get(uri)
        print("Direct Response:",response)
        print('Status Code of Get method:',response.status_code)
        print('Header of Request:',response.headers)
        print('Content of Response:',response.content)
        print('Header with specific key as Date:',response.headers.get('date'))
        self.response1=response.content

    @pytest.mark.Sanity
    def test_response_to_json(self):
        uri = 'https://reqres.in/api/users?page=2'
        response = requests.get(uri).content
        result = json.loads(response)
        print(result)
        retrive=jsonpath.jsonpath(response,'data')
        print(retrive)

