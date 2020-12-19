#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""using the cool template for pyth3 scripts done by https://gist.github.com/nafeu, and adding some personnal tweaks. many thanks"""

import argparse
import os
import sys
import subprocess
import random, string
import utils
import json


__author__ = "lmeaou"
__credits__ = ["lmeaou"]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "lmeaou"
__email__ = "none"
__status__ = "Development"

parser = argparse.ArgumentParser(description='script handle for the hsfl server')

# Positional Arguments
parser.add_argument('command',
                    help="command to execute. list, add or delete")


                    


# Optional Arguments

parser.add_argument("-D", "--deleteAll",
                    help="no args",
                    action="store_true")
parser.add_argument("-d", "--delete",
                    help="id to remove",
                    metavar='id_to_remove')

args = parser.parse_args()

def add():
    uuid = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    f = open("./database/data-"+ uuid + ".json", "w")
    data = {}
    data['uuid'] = uuid
    json.dump(data, f)
    f.close()

def list_urls():
    i = 1
    for filename in os.listdir("./database/"):
        if filename.endswith(".json"):
            uuid  = filename [5:-5]
            print(str(i) + " - " + uuid)
            i = i + 1
        else:
            continue
        


def delete(id):
    i= 1
    for filename in os.listdir("./database/"):
        if i == id:
            f = open("./database/" + filename)
            data = json.load(f)
            uuid = data["uuid"]
            f.close()
            os.remove("./database/data-" + uuid + ".json")
            return
        i+=1


def main():

    if args.command == "add":
        add()
    elif args.command == "list":
        list_urls()
    elif args.command == "delete":
        if args.delete:
            delete(int(args.delete))
        elif args.deleteAll:
            for filename in os.listdir("./database/"):
                delete(1)
        else:
            delete(1)
        

    else:
        print("usage: hsfl <args>")
    
    

if __name__ == '__main__':
    main()