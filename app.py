from flask import Flask, render_template, redirect, url_for, request, session, make_response, flash

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'SOME KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/who-we-are')
def redirect_endpoint():
    return redirect(url_for('about'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Add logic to check username and password

        if username == 'admin' and password == 'pass':
            flash('Successful Login!')
            return render_template('admin.html', message='')
        else:
            flash('Login Failed! Check Credentials.')
            return render_template('login.html', message='')


@app.route('/file-upload', methods=['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part in the request', 400
        file = request.files['file']
        if file.filename == '':
            return 'No file selected for uploading', 400
        if file.content_type == 'text/plain':
            return file.read().decode()
    return render_template('file_upload.html')

@app.route('/set_data')
def set_data():
    session['name'] = 'Kelvin'
    session['other'] = 'Hello Kelvin, Flask Dev'
    return render_template('index.html', message='Session data set.')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index.html', message=f'Name: {name}, Other: {other}')
    else:
        return render_template('index.html', message='No session found.')
    

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message='Session cleared.')

@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('index.html', message='Cookie Set.'))
    response.set_cookie('cookie_name', 'cookie_value')
    return response

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies['cookie_name']
    return render_template('index.html', message=f'Cookie Value: {cookie_value}')

@app.route('/remove_cookie')
def remove_cookie():
    response = make_response(render_template('index.html', message='Cookie Removed.'))
    response.set_cookie('cookie_name', expires=0)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)