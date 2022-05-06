from db import sql_fetch, sql_signup, sql_write
from flask import Flask, render_template, session, request, redirect
from os import environ
import bcrypt
import job_queries
import cloudinary
import cloudinary.uploader
from util.helper import upload_file_to_s3
app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY', 'secret key')


@app.route('/')
def index():
    if not session['logged_in']:
        return render_template('index.html')
    if session['logged_in']:
        #current_user_id = session['user'][0]
        #applications = sql_fetch(job_queries.all_jobs, [current_user_id])
        return redirect('/jobs')


@app.route('/jobs')
def jobs():
    if not session['logged_in']:
        return redirect('/')
    if session['logged_in']:
        current_user_id = session['user'][0]
        if not request.args.get('progress'):
            applications = sql_fetch(job_queries.all_jobs, [current_user_id])
            count = len(applications)
            return render_template('jobs.html', applications=applications, count=count)
        if request.args.get('progress'):
            progress = request.args.get('progress')
            applications = sql_fetch(job_queries.jobs_by_progress, [
                                     current_user_id, progress])
            count = len(applications)

            return render_template('jobs.html', applications=applications, count=count)


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


@app.route('/edit-job', methods=['POST'])
def edit_job():
    progress_id = request.form.get('progress_id')
    job_id = request.form.get('id')
    title = request.form.get('title')
    company = request.form.get('company')
    deadline = request.form.get('deadline')
    applied = request.form.get('applied')
    job_type = request.form.get('job-type')
    job_board = request.form.get('job-board')
    url = request.form.get('url')

    sql_write(job_queries.edit_job, [
              progress_id, title, company, deadline, applied, job_type, job_board, url, job_id])
    return redirect(f'/job/{job_id}')


@app.route('/delete-job/<id>', methods=['POST'])
def job_(id):
    sql_write(job_queries.delete_files, [id])
    sql_write(job_queries.delete_job, [id])
    return redirect('/')


@app.route('/job/<id>')
def job(id):
    if not session['logged_in']:
        return redirect('/login')
    if session['logged_in']:
        current_user_id = session['user'][0]
        job = sql_fetch(job_queries.job_by_id, [current_user_id, id])[0]
        files = sql_fetch(job_queries.get_files_by_id, [id])
        return render_template('job.html', job=job, files=files)


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


cloudinary.config(
    cloud_name=environ.get('CLOUD_NAME'),
    api_key=environ.get('CLOUD_API_KEY'),
    api_secret=environ.get('CLOUD_API_SECRET')
)


@app.route("/upload", methods=["GET", "POST"])
def create():
    if request.method == 'GET':
        return render_template('upload.html')

    if request.method == 'POST':
        job_id = request.form.get('id')
        file = request.files['user_file']

        response = cloudinary.uploader.upload(file)
        print(response)

        if response:
            sql_write(job_queries.add_file, [
                      job_id, file.filename, response['url']])
        return redirect(f'/job/{job_id}')


if __name__ == '__main__':
    app.run(debug=True)
