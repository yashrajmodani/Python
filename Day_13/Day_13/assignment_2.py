import requests
get_url = "https://jsonplaceholder.typicode.com/posts"

post_data ={
    "city":"New York",
    "temperature":28,
    "Humidity":60,
    "condition":"Sunny"
}

response = requests.post(get_url,json=post_data)

if response.status_code == 201:
    print("Response received")
    print(response.json())