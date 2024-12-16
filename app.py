from flask import Flask, render_template, redirect, request, session
from db import get_system_data, save_system_info
from auth import is_authenticated, AUTH_CREDENTIALS
from system_info import collect_system_info
import os

app = Flask(__name__)
app.secret_key = 'фывфывфыв'  # Оооочень секретный ключ


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == AUTH_CREDENTIALS['username'] and password == AUTH_CREDENTIALS['password']:
            session['logged_in'] = True
            return redirect('/dashboard')
        else:
            return render_template('login.html', error="Ты не Никита) ")

    return render_template('login.html')


@app.route('/dashboard')
def index():
    if not is_authenticated():
        return redirect('/')

    rows = get_system_data()
    return render_template('index.html', data=rows)


@app.route('/upload', methods=['POST'])
def upload():
    if not is_authenticated():
        return redirect('/')

    system_info = collect_system_info()
    save_system_info(system_info)
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
