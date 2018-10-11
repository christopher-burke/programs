#!/usr/bin/env python3

"""LOLCat Factory Program."""

import os
import cat_service


def main():
    """Main function."""
    folder = output_folder()
    download_cats(folder)


def output_folder():
    """Create folder for output.

    :return: Full path to download folder."""
    folder = 'cat_pictures'
    base_folder = os.path.dirname(__file__)
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory {full_path}')
        os.mkdir(full_path)
    return full_path


def download_cats(folder, count=8):
    cat_count = count + 1
    for i in range(1, cat_count):
        name = f'lolcat_{i}'
        cat_service.get_cat(folder, name)


if __name__ == "__main__":
    main()
