import requests

req1 = requests.post('http://localhost:5000/users', json = {"name": "Jesus", "age":"42"})
print(req1.text)
