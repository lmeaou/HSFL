from flask import Flask, request, json, flash, redirect, url_for
from werkzeug.utils import secure_filename
import argparse
import os
import sys
import subprocess
import random, string
import json
import secrets


from utils import *
from hsfl_server import *

app = Flask(__name__)

DEBUG = True
UPLOAD_FOLDER = './uploaded'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


secret = secrets.token_urlsafe(32)

app.secret_key = secret

@app.route('/')
def index():
    print("nothing there")
    return "nothing there", 200

@app.route('/<id>', methods=['GET','POST'])
def upload(id):
    if allowed_file(id):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            else:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print("file was saved")
                return "thanks", 200
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>'''
    return "", 404