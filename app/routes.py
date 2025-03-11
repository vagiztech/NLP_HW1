from flask import render_template, request
from app import app
from housemd import find_best_reply

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        user_message = request.form['message']
        response = find_best_reply(user_message)
    return render_template('index.html', response=response)