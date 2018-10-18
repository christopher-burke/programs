#!/usr/bin/env python3

"""File Searcher App."""

import os
import glob
from collections import namedtuple


SearchResult = namedtuple('SearchResult',
                          'file, line, text')


def main():
    """File Searcher App main function entry."""
    folder = get_folder_from_user()
    if not folder:
        print(f'Can\'t find {folder}.')
        return
    text = get_search_text_from_user()
    if not text:
        print(f'No text, no results.')
        return
    matches = search_folders(folder, text)

    match_count = 0
    for m in matches:
        match_count += 1
        print(f'{m.file}, line {m.line}>> {m.text}')

    print(f"Found {match_count} matches")


def get_folder_from_user():
    """Ge the folder from the user."""
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    """Get the search text from the user."""
    text = input('Search for [single phrases only]: ')
    return text.lower()


def search_folders(folder, text):
    """Search folders."""
    # macOS
    items = glob.glob(os.path.join(folder, '*'))
    # Windows
    # items = os.listdir(folder)

    print(f'Searching {folder} for {text}')
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(item):
            yield from search_folders(full_item, text)
        else:
            yield from search_file(full_item, text)


def search_file(filename, search_text):
    """Search files."""
    with open(filename, 'r', encoding='utf-8') as fin:
        line_number = 0
        for line in fin:
            line_number += 1
            if line.lower().find(search_text) >= 0:
                match = SearchResult(
                    line=line_number,
                    file=filename,
                    text=line)
                yield match


if __name__ == "__main__":
    main()
