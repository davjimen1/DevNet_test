import json

with open('json_example.json', 'r') as file:
    data = json.load(file) # load the json format to variable in python format
user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)

user['location']['city'] = 'Barcelona' # change the diccionary
with open('json_example-edited.json', 'w') as file:
    json.dump(user, file, indent=4)  # load the new value into json format
