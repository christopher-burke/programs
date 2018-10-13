#!/usr/bin/env python3

"""LOLCat Factory Program."""

import os
import cat_service
import subprocess
import platform


def main():
    """Run LOLCat factory.

    :return: None
    """
    folder = output_folder()
    download_cats(folder)
    display_cats(folder)


def output_folder():
    """Create folder for output.

    :return: Full path to download folder.
    """
    folder = 'cat_pictures'
    base_folder = os.path.dirname(__file__)
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory {full_path}')
        os.mkdir(full_path)
    return full_path


def download_cats(folder, count=8):
    """Download cat pictures."""
    cat_count = count + 1
    for i in range(1, cat_count):
        name = f'lolcat_{i}'
        cat_service.get_cat(folder, name)


def display_cats(folder: str):
    """Display the folder to the user.

    Support for macOS, Windows and Linux(Ubuntu).
    :return: None
    """
    os_open = {'Darwin': 'open',
               'Windows': 'explorer',
               'Linux': 'xdg-open'}
    try:
        command = f'{os_open[platform.system()]}'
        subprocess.call([command, folder])
    except KeyError:
        print(f'Your OS is not supported for opening `{folder}`.')


if __name__ == "__main__":
    main()
