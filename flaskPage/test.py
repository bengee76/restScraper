import json

lista = [
    {"name": "gamon",
     "type": "kot"},
    {"name": "gacek",
     "type": "pies"}
]
json.dumps(lista)
for i in lista:
    print(i["name"])