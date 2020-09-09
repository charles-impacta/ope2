import os
basedir = os.path.abspath(os.path.dirname(__file__))

import sys
sys.path.append(basedir)

from flask import Flask, jsonify
from model import db, Usuario

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def index():
    return jsonify(
        mensagem='Olá mundo!'
    )
