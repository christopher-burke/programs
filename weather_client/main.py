#!/usr/bin/env python3

"""Weather Client App.

## Note ##
Please use the API for wunderground.com in production.
Using requests and BeautifulSoup is used as a demoinstration.
"""

import requests
from bs4 import BeautifulSoup
from collections import namedtuple


WeatherReport = namedtuple('WeatherReport',
                           'cond, temp, scale, loc')


def main():
    """
    Program Main method.

    :return: None
    """
    zipcode = input('Zipcode (11001)? ')
    html = get_html(zipcode)
    report = get_weather_from_html(html)

    print(
        f'The temp in {report.loc} '
        f'is {report.temp} {report.scale} '
        f'and {report.cond}.')


def get_html(zipcode):
    """
    Get the html to be parsed.

    :param zipcode:
    :return: html from web.
    """
    url = f'https://www.wunderground.com/weather-forecast/{zipcode}'
    response = requests.get(url)

    return response.text


def get_weather_from_html(html: str) -> WeatherReport:
    """
    Get the weather from the html.

    :param html:
    :return:
    """
    soup = BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(
        class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(
        class_='wu-unit-temperature').find(class_='wu-label').get_text()

    report = WeatherReport(
        cond=cleanup_text(condition),
        temp=cleanup_text(temp),
        scale=cleanup_text(scale),
        loc=find_city_and_state_from_location(loc)
    )

    return report


def find_city_and_state_from_location(loc: str) -> str:
    """
    Get the location.

    :param loc: Location string from web.
    :return: Location string.
    """
    split_ = loc.split("\n")
    return split_[0].strip()


def cleanup_text(text: str) -> str:
    """
    Clean up text.

    :param text: Text to be cleaned up.
    :return: Cleaned up text.
    """
    if not text:
        return text
    text = text.strip()
    return text


if __name__ == "__main__":
    main()
