import requests
import json
import csv

#get request
""" response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.json())
print(response.text)
print(response.status_code) """


#post request
""" url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "userId": 1,
    "title": "test title 1",
    "body": "test body"

}

response = requests.post(url, payload)
print(response.json())
print(f"Status code: ",response.status_code) """

#params 
""" url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId": 10
}

url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "id": 10
}

response = requests.get(url, params)
print(response.text) 
print(response.status_code) """

#realtime data fetch

url = "https://api.open-meteo.com/v1/forecast"

params =  {
	"latitude": 23.7104,
	"longitude": 90.4074,
	"current_weather": True,
}

response = requests.get(url, params=params)

if response.status_code == 200 :
    current_weather = response.json()['current_weather']

# weather dhaka save in jason
""" with open('weather_dhaka_json.json', 'w') as json_file:
    json.dump(current_weather, json_file, indent=4)
    print("weather dhaka save") """

#weather dhaka save in csv

with open('weather_dhaka_csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=current_weather.keys())
    writer.writeheader()
    writer.writerow(current_weather)


