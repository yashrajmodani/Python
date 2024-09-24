import requests

#send a get request
response = requests.get('https://restcountries.com/v3.1/all')

#check status code
if response.status_code == 200:
    print("Response received")
else:
    print("Response not received", response.status_code)

countries = response.json()
# print(countries)
#loop through the list of countries and display relevant information
for country in countries:
    name = country.get('name',{}).get('common','N/A')
    capital = country.get('capital',['N/A'])[0]
    area = country.get('area','N/A')
    if name == 'India':
        print("Country: ",name)
        print("Capital: ",capital)
        print("Area: ",area,"sq km")
    # else:
    #     print()

