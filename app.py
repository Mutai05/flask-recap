from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about-us.html')

@app.route('/who-we-are')
def redirect_endpoint():
    return redirect(url_for('about'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)