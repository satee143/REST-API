import pytest
import requests
import jsonpath
import json

def test_PutStudentTechnicalDetails():
    uri='http://thetestingworldapi.com/api/studentsDetails'
    file=open('C:/Users/Dusa/PycharmProjects/API/REST/fullyapi.json','r')
    jsonrequest1=json.loads(file.read())
    result1=requests.post(uri,jsonrequest1)
    result2=result1.text
    retr=json.loads(result2)
    print(retr)
    data=jsonpath.jsonpath(retr,'id')
    print(data)
    rese=data[0]
    print(rese)


    uri='http://thetestingworldapi.com/api/technicalskills/'+str(rese)
    print(uri)
    file=open('C:/Users/Dusa/PycharmProjects/API/REST/fullytech.json','r')
    result3=file.read()
    required2=json.loads(result3)
    required2['id']=int(rese)
    required2["st_id"]=str(rese)
    print(required2)
    jsonrequests4=requests.post(uri,required2)
    print(jsonrequests4.status_code)
    print(jsonrequests4.text)
    print(jsonrequests4.content)
    # jse=json.loads(jsonrequests.content)
    # red=jsonpath.jsonpath(jse,'id')
    # print(red[0])
    uri='http://thetestingworldapi.com/api/addresses'
    file=open('C:/Users/Dusa/PycharmProjects/API/REST/address.json','r')
    son=file.read()
    jsonpathhx=json.loads(son)
    jsonpathhx['stId']=str(rese)
    responses=requests.post(uri,jsonpathhx)
    print(responses.status_code)

    ####GET API final details
    uri='http://thetestingworldapi.com/api/FinalStudentDetails/'+str(rese)
    requ=requests.get(uri)
    #print(requ)
    #print(requ.content)
    print(requ.text)
    #print(requ.status_code)
