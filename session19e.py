import json

data={"name": "Mehak",
      "phone":12878998,
"email":"@123"}

data_json = json.dumps(data)
print(data_json, type(data_json))
data_dictionary= json.loads(data_json)
print(data_dictionary,type(data_dictionary))