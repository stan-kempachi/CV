#! /usr/bin/env python
"""File containing functions utilised by the app"""


def get_type_search(nbr):
    if nbr.istitle() or len(nbr.split()) == 1:
        type_search = 'name'
        print(type_search)
        return type_search
    if len(nbr.split()) > 1:
        type_search = 'question'
        print(type_search)
        return type_search


def get_name(name):
    t = name.split()
    for w in t:
        name = w.strip('\'"?,.!_+=1234567890')
    return name


def search(skills, information):
    for key, value in skills.items():
        for v in value:
            if information in v:
                return key
