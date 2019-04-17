import requests


class DELETE:
    def delete_data(self):
        uri='https://reqres.in/api/users?page=2'
        result=requests.delete(uri)
        print(result)
        print(result.status_code)
        assert result.status_code==204




d=DELETE()
d.delete_data()