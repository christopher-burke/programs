#!/usr/bin/env python3

"""Journal Module."""


import os


def load(name):
    """
    Create and load a new journal.

    :param name: The base name of the journal to load.
    :return: A new journal data structure populated with the file data.
    """
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    """
    Save the journal to file.

    :param name: The base name of the journal to load.
    :param journal_data: Journal data to be saved.
    :return: None
    """
    filename = get_full_pathname(name)
    print(f'Using : {filename}')
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(f'{entry}\n')


def get_full_pathname(name):
    """
    Return the full path of the named journal.

    :param name: The base name of the journal.
    :return: filename path
    """
    filename = os.path.join('.', 'journals', f'{name}.jrl')
    filename = os.path.abspath(filename)
    return filename


def add_entry(text, journal_data):
    """
    Add entry to journal.

    :param test: Entry to be added.
    :param journal_data: Journal data to be saved.
    :return: None
    """
    # todo: add entry
    journal_data.append(text)
