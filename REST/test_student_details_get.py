import pytest
import json
import jsonpath
import requests

def test_get_student_details():
    uri='http://thetestingworldapi.com/api/studentsDetails/4259'
    request=requests.get(uri)
    print('Reason is;',request.text)
    jsonres=json.loads(request.content)
    id=jsonpath.jsonpath(jsonres,'data.id')
    print(id)
    assert id[0]==4258


def test_get_student_details_using_json():
    uri = 'http://thetestingworldapi.com/api/studentsDetails/4259'
    request = requests.get(uri)
    jsonres=request.json()
    id=id=jsonpath.jsonpath(jsonres,'data.id')
    assert id[0] == 4259