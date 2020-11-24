#! /usr/bin/env python
"""File containing functions utilised by the app"""
from CV.vocabulary import WORD_ABOUT_PROFIL


def get_type_search(information):
    if information == '1':
        type_search = 'son profil'
        return type_search
    if information == '2':
        type_search = 'son expérience'
        return type_search
    if information == '3':
        type_search = 'sa formation'
        return type_search
    if information == '4':
        type_search = 'ses skills'
        return type_search


# def get_if_error(type_search):
#     """
#     Check (and return if it is) error for a search
#     :param type_search:
#     :return: dict_error
#     """
#     dict_error = {'error_place': False, 'error_description': False}
#     if type_search == 'place':
#         dict_error['error_description'] = True
#     elif type_search == 'description':
#         dict_error['error_place'] = True
#     elif type_search == 'error':
#         dict_error['error_place'] = True
#         dict_error['error_description'] = True
#     return dict_error
