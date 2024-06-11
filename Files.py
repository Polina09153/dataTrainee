import json

import yaml
import pandas as pd

conn = [
    {
        "username": "name1",
        "password": 1234558,
        "host": "myHost"
    },
    {
        "username": "name2",
        "password":" 754572584"
    }
]

with open(r'connection.yaml', 'w') as file:
    documents = yaml.dump(conn, file)

with open(r'connection.yaml') as file:
    lst = yaml.load(file, yaml.FullLoader)
    print(lst)

dictionary = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA"
    }
}


json_obj = json.dumps(dictionary, indent=4)
print(type(json_obj))

with open('sample.json', 'w') as file:
    file.write(json_obj)

conn_csv = [
    {
        "username": "name1",
        "password": 1234558
    },
    {
        "username": "name2",
        "password":" 754572584"
    }
]

df = pd.DataFrame(conn_csv)
df.to_csv("pandas.csv", index = False)

df2 = pd.read_csv("pandas.csv")
print(df2)