import requests

# Using Title

endpoint_title = "http://127.0.0.1:8000/api/title/"
params = {"title": "spiderman"}
response_data = requests.get(endpoint_title, params=params) 
print("Response 1:", response_data.json())
print()
print()

# Using Id

endpoint_id = "http://127.0.0.1:8000/api/id/"
params = {"id": "tt0478087"}
response_data = requests.get(endpoint_id, params=params) 
print("Response 2:", response_data.json())
print()
print()

# Using year

endpoint_year = "http://127.0.0.1:8000/api/year/"
params = {"year": "2021"}
response_data = requests.get(endpoint_year, params=params) 
print("Response 3:", response_data.json())
print()
print()

# Using rating

endpoint_rating = "http://127.0.0.1:8000/api/rating/"
params = {"rating": "8"}
response_data = requests.get(endpoint_rating, params=params) 
print("Response 4:", response_data.json())
print()
print()
# Using genres

endpoint_genres = "http://127.0.0.1:8000/api/genres/"
params = {"genre": "action"}
response_data = requests.get(endpoint_genres, params=params) 
print("Response 5:", response_data.json())

