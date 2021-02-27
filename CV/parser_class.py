#! /usr/bin/env python

"""File containing the class who parsing the user request"""

import json
import string

from CV.vocabulary import WORD_PLEASE
# import enchant


class Parser:
    """
    Class defining the method of parser
    """
    def __init__(self, sentance: str):
        """constructor"""
        self.sentance = sentance

    def extract_information_request(self, sentance: str):
        """
        Extract good information from search
        :param sentance:
        :return: dict_request
        """
        with open('CV/stop_words.json', 'r') as json_data:
            stop_words = json.load(json_data)
        list_words = sentance.split(' ')
        list_words_for_search = list_words
        for word in list(list_words):
            if word.lower() in stop_words:
                list_words_for_search = list_words[list_words.remove(word):]
            if "d'" in word:
                list_words_for_search = list_words[list_words.index(word):]
                break
        information = " ".join(list_words_for_search)
        information = information.replace("d'", '')
        information = information.replace(" de ", '')
        return information

    # def remove_unexpected_word(self, information: str):
    #     d = enchant.Dict("en_FR")
    #     information = information.split()
    #     info = []
    #     for word in information:
    #         d.check(word)
    #         if d is True:
    #             info.append(word)
    #         else:
    #             pass
    #     return str(info)

    def remove_punctuation(self, information: str):
        """punctuation to space"""
        translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        information = information.translate(translator)
        information = information.rstrip().lstrip()
        return information

    def remove_word_please(self, information: str):
        """remove element in the list"""
        information = information.split(' ')
        dict_request = {}
        for elt in information:
            if elt in WORD_PLEASE:
                information.remove(elt)
        information_to_search = " ".join(information)
        dict_request['information'] = information_to_search
        return dict_request
