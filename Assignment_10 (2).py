import requests

# Task 1: Chuck Norris
joke_response = requests.get("https://api.chucknorris.io/jokes/random").json()
print(f"Joke: {joke_response['value']}\n")

# Task 2: Weather
city = input("Enter your city for weather: ")
api_key = "e4c9a0ba5ee38e1433e7ddd5c60b6dea"
geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"

geo_data = requests.get(geo_url).json()

if geo_data:
    lat, lon = geo_data[0]['lat'], geo_data[0]['lon']
    # Adding units=metric simplifies the Kelvin to Celsius conversion!
    w_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    w_data = requests.get(w_url).json()
    
    desc = w_data['weather'][0]['description']
    temp = w_data['main']['temp']
    print(f"In {city.title()}: {desc}, {temp}°C\n")
else:
    print("City not found.\n")

# Task 4: Airport Info
icao = input("Enter Airport ICAO (e.g., LFLL): ")
airport_resp = requests.get(f"http://127.0.0.1:5000/airport/{icao}")

if airport_resp.status_code == 200:
    data = airport_resp.json()
    print(f"Airport: {data['name']} in {data['city']}, {data['country']}")
else:
    print(f"Error: {airport_resp.json().get('error', 'Unknown error')}")
    
    # Task 3: Prime Number
number_to_check = input("Enter a number to check if it's prime: ")
prime_url = f"http://127.0.0.1:5000/prime_number/{number_to_check}"
prime_data = requests.get(prime_url).json()

if prime_data['isPrime']:
    print(f"Result: {prime_data['Number']} is a prime number.")
else:
    print(f"Result: {prime_data['Number']} is NOT a prime number.")