import requests, json
from pprint import pprint

class PostcodeAPI:
    def __init__(self, postcodes):
        self.url = "https://api.postcodes.io/postcodes"
        self.postcodes = postcodes
        self.header = {"Content-Type": "application/json"}
        self.result = self.post_request()

    def parse_postcodes(self) -> dict:          # postcodes str/list -> dict
        if isinstance(self.postcodes, list):
            return {"postcodes": self.postcodes}
        return {"postcodes": [self.postcodes]}

    def get_request(self):                      # return body of GET request
        if isinstance(self.postcodes, str):
            req = requests.get(
                f"{self.url}/{self.postcodes}"
            )
            if req.status_code == 200:
                return req.json()
        else:
            result = []
            for pc in self.postcodes:
                req = requests.get(
                    f"{self.url}/{pc}"
                )
                if req.status_code == 200:
                    result.append(req.json())

            return result

    def post_request(self) -> list:
        req = requests.post(
            self.url,
            headers=self.header,
            json=self.parse_postcodes()
        )
        if req.status_code == 200:
            return req.json()["result"]

    def get_info(self, postcode, detail): # Retrieves a particular detail of a postcode
        for pc in self.result:
            if pc["query"] == postcode:
                return f"{postcode} - {detail}: {pc['result'][detail]}"


postcodes = [
        "PR3 0SG",
        "M45 6GN",
        "EX165BL"
    ]

r = PostcodeAPI(postcodes)

print(r.get_info("PR3 0SG", "eastings"))

# for pc in r.postcodes:
#     print(r.get_info(pc, "longitude"))

pprint(r.get_request())



