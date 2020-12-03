#! /usr/bin/env python
"""File containing functions utilised by the app"""
from CV.vocabulary import WORD_ABOUT_PROFIL


def get_type_search(nbr):
    if nbr == '1':
        print('1')
        type_search = 'son profil'
        return type_search
    if nbr == '2':
        print('2')
        type_search = 'son expérience'
        return type_search
    if nbr == '3':
        print('3')
        type_search = 'sa formation'
        return type_search
    if nbr == '4':
        print('4')
        type_search = 'ses skills'
        return type_search
    if len(nbr.split()) > 1:
        print('quest')
        type_search = 'question'
        return type_search
    if nbr.istitle():
        type_search = 'name'
        print('name')
        return type_search


def get_name(name):
    if len(name.split()) == 1:
        return name

