import sqlite3
from app import app
from model.payment_model import Payment1
from flask import render_template
import requests


calling_payment=Payment1()
@app.route('/')
def home():
    response=requests.get("http://127.0.0.1:5000/payments")
    # print(student_data)
    Payment_data=response.json()['PaymentData']
    return render_template('index.html',payments=Payment_data,title="Payment Dashboard")



@app.route('/payments')
def get_payment():
    # return "this is get data method"
    return calling_payment.get_payment_data()

@app.route('/payments',methods=['POST'])
def post_payment():
    # return "this is post data method"
    return calling_payment.post_payment_data()

@app.route('/payments/<id>',methods=["PUT"])
def update_payment(id):
    return calling_payment.update_payment_data(id)


@app.route('/payments/<id>',methods=["DELETE"])
def delete_payment(id):
    # return "this is delete data method"
    return calling_payment.delete_payment_data(id)


