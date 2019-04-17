import pytest
import json
import jsonpath
import requests

def test_delete_student_details():

    uri='http://thetestingworldapi.com/api/studentsDetails/4258'
    request=requests.delete(uri)
    print(request.content)
    print(request)
    print(request.text)