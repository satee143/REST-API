import pytest
import json
import jsonpath
import requests

def test_put_student_details():

    uri='http://thetestingworldapi.com/api/studentsDetails/4258'
    file=open('c:/Users/Dusa/PycharmProjects/API/REST/data.json','r')
    jsonpart=json.loads(file.read())
    response=requests.put(uri,jsonpart)
    print(response.text)
    print()
    print(response.content)