import requests

req = requests.post('http://localhost:5000/users/2/phones', json = {"number": "9f5b7329", "brand": "iphone", "carrier": "entel" } )
# req = requests.patch('http://localhost:5000/users/2', json={"name": 'andrea', 'age' : '18'})

