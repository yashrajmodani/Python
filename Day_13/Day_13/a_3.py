#DELETE

import requests


delete_url = "https://reqres.in/api/users/{id}"

response = requests.delete(delete_url.format(id=2))

if response.status_code == 204:
    print("Response received")
    print(response.text)
else:
    print("Response not received", response.status_code)