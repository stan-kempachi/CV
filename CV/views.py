import random
from CV.vocabulary import TYPE_QUESTION, WORD_ABOUT_PROFIL, WORD_ABOUT_FORMATION, WORD_ABOUT_EXP, WORD_ABOUT_SKILLS, \
    WORD_ABOUT_PROJECT
from CV.parser_class import Parser
from CV.infos import profil, experiences, projets, formation, skills
from CV.utils import get_type_search, get_name
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
        if type_search == 'name':
            name = get_name(request_user)
            dict_information = {'type_search': type_search, 'name': name, 'nice': random.choice(TYPE_QUESTION)}
            return json.dumps(dict_information)
        if type_search == 'question':
            parser = Parser(request_user)
            information_extracted = parser.extract_information_request(request_user)
            information_extracted = parser.remove_punctuation(information_extracted)
            information_extracted = parser.remove_word_please(information_extracted)
            information = information_extracted['information'].lower()
            print(information)
            for key, value in profil.items():
                matching = [s for s in value if information in s]
                if matching or information in WORD_ABOUT_PROFIL:
                    dict_information = {'information': information,
                                        'resp': random.choice(list(profil.values()))}
                    return json.dumps(dict_information)
            for key, value in experiences.items():
                matching = [s for s in value if information in s]
                if matching or information in WORD_ABOUT_EXP:
                    dict_information = {'information': information,
                                        'resp': random.choice(list(experiences.values()))}
                    return json.dumps(dict_information)

            for key, value in skills.items():
                matching = [s for s in value if information in s]
                if matching or information in WORD_ABOUT_SKILLS:
                    dict_information = {'information': information,
                                        'resp': random.choice(list(skills.values()))}
                    return json.dumps(dict_information)
            for key, value in projets.items():
                matching = [s for s in value if information in s]
                if matching or information in WORD_ABOUT_PROJECT:
                    dict_information = {'information': information,
                                        'resp': random.choice(list(projets.values()))}
                    return json.dumps(dict_information)
            for key, value in formation.items():
                matching = [s for s in value if information in s]
                if matching or information in WORD_ABOUT_FORMATION:
                    dict_information = {'information': information,
                                        'resp': random.choice(list(formation.values()))}
                    return json.dumps(dict_information)


if __name__ == '__main__':
    app.run(debug=True)
