from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

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
            return 'Success'
        else:
            return "Invalid login credentials", 401


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)