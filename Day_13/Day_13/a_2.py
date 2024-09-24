import requests
#api endpoint to create a new user
post_url = "https://reqres.in/api/users"
#data to be snt int the post request
post_data = {
    "name":"John Deo",
    "job":"SD"
}

response = requests.post(post_url,json=post_data)
if response.status_code == 201:
    print("Response received")
    print(response.json())

