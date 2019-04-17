import requests
import json
import jsonpath

class Post:

    uri='https://reqres.in/api/users'
    def convert_file_into_json(self):
        file=open('C:/Users/Dusa/PycharmProjects/API/REST/read.json','r')
        read=file.read()

        self.load=json.loads(read)
        #print(load)


    def posting_json_into_api(self):
        result=requests.post(self.uri,self.load)
        print(result.status_code)
        print(result.content)
        self.content=result.text
        print(self.content)
        retr=json.loads(self.content)

        result=jsonpath.jsonpath(retr,'id')

        print(result)
        print(jsonpath.jsonpath(retr,'Name'))

p=Post()
p.convert_file_into_json()
p.posting_json_into_api()