from flask import render_template, request, redirect, url_for, flash
from app import app
from housemd import find_best_reply

app.secret_key = 'blablabla'

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        user_message = request.form['message']
        response = find_best_reply(user_message)
    return render_template('index.html', response=response)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        # Сохраняем обратную связь в файл или базу данных; здесь пример записи в файл
        with open("feedback.txt", "a", encoding="utf-8") as f:
            f.write(f"Имя: {name}\nEmail: {email}\nСообщение: {message}\n{'-'*40}\n")
        flash("Спасибо за обратную связь!")
        return redirect(url_for('feedback'))
    return render_template("feedback.html")