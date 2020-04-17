import csv
import json


books_dict = {}
users_dict = {}
output_dict = {"Users": []}

with open("../data_input/input_csv_file_hw3.csv") as input_csv:
    reader = csv.DictReader(input_csv)
    for count, row in enumerate(reader, 1):
        books_dict[count] = {
            "title": row["Title"],
            "author": row["Author"],
            "height": row["Height"]}

with open("../data_input/input_json_file_hw3.json") as input_json:
    users = json.loads(input_json.read())
    for count, user in enumerate(users, 1):
        users_dict[count] = {
            "name": user["name"],
            "gender": user['gender'],
            "address": user['address']
        }

for number, user in users_dict.items():
    temp_user = user.copy()
    temp_user["books"] = []
    if books_dict:
        temp_user["books"].append(books_dict[number])
        books_dict.pop(number)
    output_dict["Users"].append(temp_user)

with open("../data_output/output_json_file_hw3.json", "w") as output_json:
    s = json.dumps(output_dict, indent=4)
    output_json.write(s)
