import json
import os
from os import path

def get_key_from_db(uuid, key):
    data_path = "database/data-" + uuid + ".json"
    if path.exists(data_path):
        f = open(data_path, "r")
        data = json.load(f)
        return data[key]
    return "nodata"