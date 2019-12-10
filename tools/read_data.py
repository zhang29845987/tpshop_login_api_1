import json

import os

from data import paths


def login_data():
    processed_data = []
    with open(paths, "r", encoding="utf8") as f:
        ee = json.load(f)
        for data in ee:
            username=data.get("username")
            password=data.get("password")
            code=data.get("code")
            expect=data.get("expect")
            processed_data.append((username,password,code,expect))
    print(processed_data)
    return processed_data


