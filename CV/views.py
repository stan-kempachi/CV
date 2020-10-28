from flask import Flask
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='')

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
