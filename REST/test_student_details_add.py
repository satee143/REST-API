import pytest
import json
import jsonpath
import requests

def test_AddStudentDetails():
    file=open('C:/Users/Dusa/PycharmProjects/API/REST/data.json','r')
    json_format=json.loads(file.read())
    request=requests.post('http://thetestingworldapi.com/api/studentsDetails',json_format)
    assert request.status_code==201
    json_request=json.loads(request.text)
    print(json_request)
    rjsonpath=jsonpath.jsonpath(json_request,'id')
    print(rjsonpath[0])