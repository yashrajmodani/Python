from locale import currency
import requests

try:
    #send a get request
    response = requests.get('https://restcountries.com/v3.1/all')
    response1 = requests.get('https://restcountries.com/v3.1/currency/INR')

    #check status code
    if response.status_code == 200 and response1.status_code == 200:
        print("Response received")
    else:
        print("Response not received", response.status_code)

    countries = response.json()
    currencies = response1.json()
    # print(countries)
    # print(currencies)
    #loop through the list of countries and display relevant information

    reg = input("enter a region: ")
    cur = input("enter a currency: ")
    for country in countries:
        name = country.get('name',{}).get('common','N/A')
        capital = country.get('capital',['N/A'])[0]
        area = country.get('area','N/A')
        region = country.get('region','N/A')
        # currency = country.get('currencies',{}).get('INR',{}).get('name','N/A')
        currencies = country.get('currencies',{})
        for currency in currencies:
            if currency == 'INR':
                currency = currencies[currency]['name']
        if region == reg and currency == cur:
            print("Country: ",name)
            print("Capital: ",capital)
            print("Area: ",area,"sq km")
            print("Region: ",region)
            print("Currency: ",currency)
        # else:
        #     print()

except Exception as e:
    print(e)

finally:
    print("Execution completed")