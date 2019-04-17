import json
import requests
import jsonpath

class GET:
    def dict_to_json(self):
        # Converting Dictonary into JSON Format
        d = '{"Name":"Satheesh Kumar","City":"Hyderabad","MobileNo":9989884111}'


        result = json.loads(d)
        print(result)

### GET OPERATION ON API
    def get_method(self):
        uri='https://reqres.in/api/users?page=2'
        response=requests.get(uri)
        #print(response)
        status_code=response.status_code
        #print(status_code)
        header=response.headers
        self.content=response.content
        cookies=response.cookies
        #print(header)
        #print(cookies)
        #print(content)
        #print(header.get('server'))
        #print(header.get('date'))


### Converting Response into JSON FORMAT
    def respone_to_json(self):
        self.result=json.loads(self.content)
        #print(self.result)


    def get_jsonpath(self):
        rep=jsonpath.jsonpath(self.result,'total')
        print(rep[0])
        print(jsonpath.jsonpath(self.result,'data'))
        for i in range(3):

            print(jsonpath.jsonpath(self.result,'data['+str(i)+'].first_name'))

            #print(jsonpath.jsonpath(self.result,'data['+str(i)+'].avatar'))






s=GET()
#s.dict_to_json()
s.get_method()
s.respone_to_json()
s.get_jsonpath()