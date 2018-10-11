#!/usr/bin/env python3

"""LOLCat Factory Program."""

import os


def main():
    """Main function."""
    folder = output_folder()


def output_folder():
    """Create folder for output."""
    folder = 'cat_pictures'
    base_folder = os.path.dirname(__file__)
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print(f'Creating new directory {full_path}')
        os.mkdir(full_path)
    return full_path


if __name__ == "__main__":
    main()
