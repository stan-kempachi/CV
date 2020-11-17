import random
from datetime import datetime
from CV.vocabulary import SENTANCE_DESCRIPTION_GRANDPY, SENTANCE_PLACE_GRANDPY
from CV.parser_class import Parser
from flask import Flask, render_template, request, json, send_from_directory
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


@app.route('/get_user_request', methods=['GET'])
def get_user_request():
    """define get user request methode"""
    if request.method == "GET":
        request_user = request.args.get('question')
        parser = Parser(request_user)
        information_extracted = parser.extract_information_request(request_user)
        information_extracted = parser.remove_punctuation(information_extracted)
        information_extracted = parser.remove_word_please(information_extracted)
        information = information_extracted['information']
        dict_information = {'description': "Test"}
        dict_information.update({'sentance_description': random.choice(SENTANCE_DESCRIPTION_GRANDPY)})
        return json.dumps(dict_information)


if __name__ == '__main__':
    app.run(debug=True)
