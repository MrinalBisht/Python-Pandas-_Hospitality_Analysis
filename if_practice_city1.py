India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York","Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]
city = input("Enter a city name: ")
if city in India:
    print(f'{city} belongs to india')
elif city in USA:
    print(f'{city} belongs to USA')
elif city in UK:
    print(f'{city} belongs to UK')

city_1 = input("Enter a city 1 name: ")
city_2 = input("Enter a city 2 name: ")
if city_1 and city_2 in India:
    print("Both cities are in India")
elif city_1 and city_2 in USA:
    print("Both cities are in USA")
elif city_1 and city_2 in UK:
    print("Both cities are in UK")
else:
    print("They don't belong to the same country")