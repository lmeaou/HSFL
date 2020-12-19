import os
import sys
import subprocess
import random, string

def allowed_file(id):
    for filename in os.listdir("./database/"):
        if filename.endswith(".json"):
            uuid  = filename [5:-5]
            if id == uuid:
                return True
    return False