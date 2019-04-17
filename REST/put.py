import json
import requests
import jsonpath

class PUT:
    uri='https://reqres.in/api/users/2'
    def Read_File_and_json(self):
        file=open('C:/Users/Dusa/PycharmProjects/API/REST/read.json','r')
        read=file.read()
        self.load=json.loads(read)

    def Put_Resource(self):
        result=requests.put(self.uri,self.load)
        print(result.status_code)
        print(result.content)
        self.json_load=result.text

    def Retriving_Updated(self):
        reload=json.loads(self.json_load)
        ret=jsonpath.jsonpath(reload,'updatedAt')
        print(ret)

p=PUT()
p.Read_File_and_json()
p.Put_Resource()
p.Retriving_Updated()