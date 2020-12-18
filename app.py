from flask import Flask
import argparse
import os
import sys
import subprocess
import random, string
import utils
import json


app = Flask(__name__)

DEBUG = True

@app.route('/')
def index():
    print("nothing there")

@app.route('/<id>')
def upload(id):
    for filename in os.listdir("./database/"):
        if filename.endswith(".json"):
            uuid  = filename [5:-5]
            if id == uuid:
                print("valid url")
                return "Hello world", 200
    return "", 404