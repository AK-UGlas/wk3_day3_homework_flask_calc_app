
from flask import render_template, request, redirect
from app import app
from modules.calculator import *

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        req = request.form
        url_add = f"{req['operator']}/{req['first']}/{req['second']}"
        return redirect(request.url + url_add)

    return render_template('index.html', title='Barely Usable Calculator')

@app.route('/<operator>/<first>/<second>')
def result(operator, first, second):
    # cast inputs from strings to ints
    first = int(first)
    second = int(second)

    # execute correct mathematical function
    if operator == '+':
        answer = add(first, second)
    elif operator == '-':
        answer = subtract(first, second)
    elif operator == '/':
        answer = divide(first, second)
    elif operator == '*':
        answer = multiply(first, second)

    return render_template('result.html', answer=answer)