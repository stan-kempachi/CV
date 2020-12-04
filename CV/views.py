import random
from datetime import datetime
from CV.vocabulary import SENTANCE_PROFIL, SOFTSKILLS, TYPE_SENTENCE, TYPE_QUESTION_NAME, TYPE_QUESTION, WORD_ABOUT_PROFIL
from CV.parser_class import Parser
from CV.infos import profil
from CV.utils import get_type_search, get_name
from CV.forms import FormType, FormName
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
        type_search = get_type_search(request_user)
        if type_search == 'son profil' or type_search == 'son expérience' or type_search == 'sa formation' or \
                type_search == 'ses skills':
            dict_information = {'type_search': type_search, 'sentance_type': random.choice(TYPE_SENTENCE),
                                'ask_for_name': random.choice(TYPE_QUESTION_NAME)}
            return json.dumps(dict_information)
        if type_search == 'name':
            name = get_name(request_user)
            dict_information = {'type_search': type_search, 'name': name, 'nice': random.choice(TYPE_QUESTION)}
            return json.dumps(dict_information)
        if type_search == 'question':
            parser = Parser(request_user)
            information_extracted = parser.extract_information_request(request_user)
            information_extracted = parser.remove_punctuation(information_extracted)
            information_extracted = parser.remove_word_please(information_extracted)
            information = information_extracted['information']
            dict_information = {'information': information,
                                'sentance_type': random.choice(TYPE_SENTENCE),
                                'resp': profil['bio']}
            return json.dumps(dict_information)
        else:
            print('erreur views')


if __name__ == '__main__':
    app.run(debug=True)
