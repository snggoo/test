import sys
from os.path import pardir
sys.path.insert(0, pardir)
from db import dbConfig
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    db = dbConfig.Database()
    sql = "select * from mode"
    row = db.executeAll(sql)
    return render_template('index.html',resultData=row)