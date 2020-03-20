import sys
sys.path.insert(0, '/var/www/dronapplication/db')
from flask import Flask,render_template
import dbConfig
app = Flask(__name__)

@app.route('/')
def index():
    db = dbConfig.Database()
    sql = "select * from test"
    row = db.executeAll(sql)
    return render_template('index.html',result=None,resultData=row,resultUPDATE=None)
