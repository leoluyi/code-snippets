# -*- coding: utf-8 -*-
# Librarys
from flask import Flask, render_template
from flask_pymongo import PyMongo
import os

# Variables
app = Flask(__name__)

# Settings
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.getenv('MONGO_SECRET_KEY')


# Views
@app.route('/', methods=('GET', 'POST'))
def index():
    return '<h1>Hello</h1>'


# Run
if __name__ == '__main__':
    app.run()
