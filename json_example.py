import json

user_ids_and_addresses = {
    1: "A",
    2: "B",
}

json_str = json.dumps(user_ids_and_addresses)

with open("addresses.json", "w+") as file:
    file.write(json_str)
    file.close()

f = open("addresses.json")
json_str = f.read()
val = json.loads(json_str)

for k,v in enumerate(val):
    print(str(k) +" -> "+ str(v))