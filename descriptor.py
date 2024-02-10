from sys import argv


def get_endpoints(file):
    with open(file, "r", encoding="UTF8", newline="") as f:
        return f.readlines()


print(get_endpoints(argv[1]))
