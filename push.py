from ast import Param
from datetime import date
from inspect import Parameter
from sqlite3 import paramstyle
from flask import Flask,request,render_template,redirect
import requests
app=Flask(__name__)
url='https://httptest1977.herokuapp.com/'
par={
        'name':'ben',
        'age':'45'
    }
payload = {"name1": "value1", "key2": "value2"}
@app.route('/')
def lala():
    return "helloben"

@app.route("/push_get",methods=["GET"])
def push():  

    re=requests.get(url,params=par)
    
    return 'OK'
@app.route("/push_post",methods=['POST'])
def push_post():
    re1=requests.post(url, data = payload)
    print(type(re1))
    print(re1)
    return 'ok'
if __name__=='__main__':
    app.run(debug=True)