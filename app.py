from db import sql_fetch, sql_signup, sql_write
from flask import Flask, render_template, session, request, redirect
from os import environ
import bcrypt
app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY', 'secret key')


@app.route('/')
def index():
    if not session['logged_in']:
        return redirect('/login')
    if session['logged_in']:
        current_user_id = session['user'][0]
        applications = sql_fetch(
            '''SELECT applications.id, title, companies.name, deadline, applied, board,type_of_work, progress_status, progress_id FROM APPLICATIONS
                INNER JOIN progress ON progress_id = progress.id
                INNER JOIN companies ON company_id = companies.id
                INNER JOIN types_of_work ON type_of_work_id = types_of_work.id
                INNER JOIN job_board ON job_board_id = job_board.id
                WHERE user_id = %s''', [current_user_id])
    return render_template('index.html', applications=applications)


@app.route('/job')
def job():
    if session['logged_in'] == False:
        return render_template('login.html')
    if session['logged_in']:
        job = sql_fetch()
        return render_template('job.html')


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
