import csv
import json


books_dict = {}
users_dict = {}
output_dict = {"Users": []}

with open("input_csv_file.csv") as input_csv:
    reader = csv.DictReader(input_csv)
    for count, row in enumerate(reader, 1):
        books_dict[count] = {
            "title": row["Title"],
            "author": row["Author"],
            "height": row["Height"]}

with open("input_json_file.json") as input_json:
    users = json.loads(input_json.read())
    for count, user in enumerate(users, 1):
        users_dict[count] = {
            "name": user["name"],
            "gender": user['gender'],
            "address": user['address']
        }

for user in users_dict.values():
    temp_user = user.copy()
    temp_user["books"] = []
    for book in books_dict.values():
        temp_user["books"].append(book)
    output_dict["Users"].append(temp_user)

with open("output_json_file.json", "w") as output_json:
    s = json.dumps(output_dict, indent=4)
    output_json.write(s)
