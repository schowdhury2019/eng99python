import requests, json
from pprint import pprint

postcode_header = {
    "Content-Type": "application/json"
}
json_data = {
    "postcodes": [
        "PR3 0SG",
        "M45 6GN",
        "EX165BL"
    ]
}

multi_req = requests.post(
    "https://api.postcodes.io/postcodes",
    headers=postcode_header,
    #data=json.dumps(json_data)
    json=json_data # does the same as the line above
)

postcodes = multi_req.json()

# print(type(postcodes))

for codes in postcodes["result"]:
    print(f"{codes['query']} - Latitude: {codes['result']['latitude']}, Longitude: {codes['result']['longitude']}")

# postcode_req = requests.get(
#     "https://api.postcodes.io/postcodes/se120nb"
# )
#
# print(postcode_req, type(postcode_req))
#
# if postcode_req.status_code == 200:
#     # pprint(postcode_req.headers, sort_dicts=False)
#     # pprint(postcode_req.json(), sort_dicts=False) # returns a dict
#     # print(postcode_req.content)
#     postcode = postcode_req.json()
#
#
# print(postcode)
# print(postcode["result"]["eastings"])
# print(postcode["result"]["northings"])