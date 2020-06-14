import sys
import requests
from bs4 import BeautifulSoup
from utils.parsers import parse_definitions


def scrape_wotd():
    result = requests.get(f"https://www.urbandictionary.com")

    if result.status_code == 500:
        return {
            "error": "Sorry, but something went wrong. Try again later"
        }

    if result.status_code == 404:
        return {
            "error": f"Sorry, but we couldn't find: {word}"
        }

    if result.status_code == 200:
        soup = BeautifulSoup(result.content, 'lxml')

        # Parse definitions
        definitions = parse_definitions(soup)

        return definitions.pop(0)


sys.modules[__name__] = scrape_wotd
