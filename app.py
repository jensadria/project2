from db import sql_fetch, sql_signup, sql_write
from flask import Flask, render_template, session, request, redirect
from os import environ
import bcrypt
import job_queries
app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY', 'secret key')


@app.route('/')
def index():
    if not session['logged_in']:
        return redirect('/login')
    if session['logged_in']:
        current_user_id = session['user'][0]
        applications = sql_fetch(job_queries.all_jobs, [current_user_id])
    return render_template('index.html', applications=applications)


@app.route('/job/<id>')
def job(id):
    if not session['logged_in']:
        return redirect('/login')
    if session['logged_in']:
        current_user_id = session['user'][0]
        job = sql_fetch(job_queries.job_by_id, [current_user_id, id])[0]

        return render_template('job.html', job=job)


@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign-up.html')
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        sql_signup(name, email, password)

        return redirect('/login')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = sql_fetch("SELECT * FROM users WHERE email = %s", [email])[0]
        password_hash = user[3]

        if bcrypt.checkpw(password.encode(), password_hash.encode()):
            session['id'] = user[0]
            session['user'] = user
            session['logged_in'] = True
            return redirect('/')
        else:
            return redirect('/login?signup=fail')


@app.route('/logout')
def logout():
    session.clear()
    session['logged_in'] = False
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
