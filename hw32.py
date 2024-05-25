import requests
import json
import csv

data = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(data.text)
with open("hw.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
    writer.writeheader()
    for d in todos:
        writer.writerow(d)
