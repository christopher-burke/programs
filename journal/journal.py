
import os

"""Journal Module."""


def load(name):
    # todo: populate from file if it exists
    data = []
    filename = get_full_pathname(name)
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data


def save(name, journal_data):
    """Save the journal."""
    filename = get_full_pathname(name)
    print(f'Using : {filename}')
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(f'{entry}\n')


def get_full_pathname(name):
    """Return the full path of the named journal."""
    filename = os.path.join('.', 'journals', f'{name}.jrl')
    filename = os.path.abspath(filename)
    return filename


def add_entry(text, journal_data):
    # todo: add entry
    journal_data.append(text)
    return None
