import requests
header={"Result":"25850","Data":"satee"}
param={"Name":"satee143@gmail.com","mobile_number":9989884111}
response=requests.get('https://httpbin.org/get',params=param)
print(response.text)