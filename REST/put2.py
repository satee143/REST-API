import json
import requests
import jsonpath

load={'id': 4296, 'language': ['python', 'selenium'], 'yearsexp': '2', 'lastused': '2019', 'st_id': '4296'}
result=requests.get('http://thetestingworldapi.com/api/technicalskills/4182')
print(result.status_code)
rece=result.content
jse=json.loads(rece)
print(jse)
print(jsonpath.jsonpath(jse,'id'))