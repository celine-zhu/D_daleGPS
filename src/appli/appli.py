from flask import Flask, Blueprint, render_template, abort, request, redirect, url_for
from flask import g
import sqlite3
import numpy as np




app = Flask(__name__, static_folder='static', template_folder='templates')
DATABASE = "../../bdd/project.db"

def getdb():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.route('/')
def Index():
    return render_template('index.html')

