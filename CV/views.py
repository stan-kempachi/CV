import random
from datetime import datetime
from CV.vocabulary import SENTANCE_PROFIL, SOFTSKILLS, TYPE_SENTENCE, TYPE_QUESTION_NAME, TYPE_QUESTION
from CV.parser_class import Parser
from CV.infos import profil
from CV.utils import get_type_search
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
        if type_search:
            dict_information = {'type_search': type_search, 'sentance_type': random.choice(TYPE_SENTENCE),
                                'ask_for_name': random.choice(TYPE_QUESTION_NAME)}
            return json.dumps(dict_information), type_search
        else:
            name = request_user
            dict_information = {'name': name, 'nice': random.choice(TYPE_QUESTION)}
            return json.dumps(dict_information)


        # parser = Parser(request_user)
        # information_extracted = parser.extract_information_request(request_user)
        # information_extracted = parser.remove_punctuation(information_extracted)
        # information_extracted = parser.remove_word_please(information_extracted)
        # type_search = information_extracted['type_search']
        # information = information_extracted['information']
        # if type_search == 'error':
        #     dict_information = {'type_search': 'error'}
        # if type_search == 'profil':
        #     dict_information = {'information': information, 'type_search': type_search, 'profil': profil,
        #                         'softskills': random.choice(SOFTSKILLS)}
        #     dict_information.update({'sentance_description': random.choice(SENTANCE_DESCRIPTION_GRANDPY),
        #                              'sentance_profil': random.choice(SENTANCE_PROFIL)})
        #     return json.dumps(dict_information)


if __name__ == '__main__':
    app.run(debug=True)
