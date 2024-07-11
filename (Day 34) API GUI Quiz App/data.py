import random
import requests

category = random.choice([15, 18, 19])
if category == 19:
    category_name = "Category: \nMath"
elif category == 18:
    category_name = "Category: \nComputers"
else:
    category_name = "Category: \nVideo Games"
parameters = {
    "amount": 10,
    "category": category,
    # "category": 19,
    # "difficulty": "easy",
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

print(response)
question_data = response.json()["results"]
print(question_data)