import json

file = open('data/db-export.json', 'r')
lines = file.readlines()
photos = []

for line in lines:
    photo = json.loads(line)
    photos.append(photo)

print(photos)
