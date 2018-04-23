import requests

req1 = requests.post('http://localhost:5000/users/2/notebooks', json = {"brand": "dell"} )
print(req1.text)
