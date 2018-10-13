import os
import requests
import shutil


def get_cat(folder: str, name: str):
    """Get cat image from internet.

    :param folder: String file folder path.
    :param name: String name of file
    """
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data(url)
    save_image(folder, name, data)


def get_data(url: str):
    """Get the data from the url.

    :param url: The link used to get the data.
    :return: The raw response from requests.
    """
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder: str, name: str, data):
    """Save image to disk.

    :param folder: The string path to the folder.
    :param name: The string name of the file.
    :param data: The data to be saved.
    """
    file_name = os.path.join(folder, name + '.jpg')

    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
