import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint,
                        json={'query': 'hello_world'},
                        params={"abc": 123},)


# print(f"{response.headers=}")
# print(f"{response.text=}")
print(f"{response.json()=}")
