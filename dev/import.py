import json

file = open('data/db-export.json', 'r')
lines = file.readlines()

for line in lines:
    photo = json.loads(line)
    print(photo)
