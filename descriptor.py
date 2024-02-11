from requests import get
from sys import argv


def get_endpoints(file):
    with open(file, "r", encoding="UTF8", newline="") as f:
        return list(map(lambda x: x.rstrip(), f.readlines()))


def api_call(endpoint):
    return get(endpoint).json()


endpoints = get_endpoints(argv[1])

print(endpoints[0])
print(api_call(endpoints[0]))
