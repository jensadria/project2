from db import sql_fetch, sql_signup, sql_write
from flask import Flask, render_template, session, request, redirect
from os import environ
import bcrypt
import job_queries
from util.helper import upload_file_to_s3
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


@app.route('/add-job', methods=['POST'])
def add_job():
    current_user_id = session['user'][0]
    title = request.form.get('title'),
    company = request.form.get('company'),
    deadline = request.form.get('deadline'),
    applied = request.form.get('applied'),
    job_type = request.form.get('job-type'),
    job_board = request.form.get('job-board'),
    url = request.form.get('url')

    sql_write(job_queries.add_job, [
              '1', current_user_id, title, company, deadline, applied, job_type, job_board, url])
    return redirect('/')


@app.route('/job')
def job_():
    return render_template('job.html')


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
    if request.method == 'GET' and session['logged_in']:
        return redirect('/')
    # if request.method == 'GET':
    if request.method == 'GET' and request.args.get('login'):
        signup = request.args.get('login')
        return render_template('login.html', login=login)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = sql_fetch("SELECT * FROM users WHERE email = %s", [email])[0]
        password_hash = user[3]

        # if not user:
        #    return redirect('/login?signup=fail')

        if bcrypt.checkpw(password.encode(), password_hash.encode()):
            session['id'] = user[0]
            session['user'] = user
            session['logged_in'] = True
            return redirect('/')
        # return redirect('/login')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    session['logged_in'] = False
    return redirect('/')


@app.route("/upload", methods=["GET", "POST"])
def create():
    if request.method == 'GET':
        return render_template('upload.html')

    if request.method == 'POST':
        # check whether an input field with name 'user_file' exist
        # if 'user_file' not in request.files:
        #    flash('No user_file key in request.files')
        #    return redirect(url_for('new'))

        # after confirm 'user_file' exist, get the file from input
        file = request.files['user_file']
        # check whether a file is selected
        # if file.filename == '':
        #    flash('No selected file')
        #    return redirect(url_for('new'))

        # check whether the file extension is allowed (eg. png,jpeg,jpg,gif)
        # if file and allowed_file(file.filename):
        file_name, file_url = upload_file_to_s3(file)
        print(file_name)
        print(file_url)
        # if upload success,will return file name of uploaded file
        if file_url:
            # write your code here
            # to save the file name in database

            #flash("Success upload")
            return redirect('/')

            # upload failed, redirect to upload page

        # if file extension not allowed
        # else:
        #    flash("File type not accepted,please try again.")
        #    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
