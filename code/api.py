from serpapi import GoogleSearch
import json

search = GoogleSearch({
    "q": "Angels",
    "location" : "Albuquerque, New Mexico",
    "api_key" : ""
})

result = search.get_dict()

details = result

with open('convert.json', 'w') as convert_file:
    convert_file.write(json.dumps(details))

