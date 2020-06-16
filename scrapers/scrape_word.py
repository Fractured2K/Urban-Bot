import sys
import requests
from bs4 import BeautifulSoup
from utils.parsers import parse_definitions


def scrape_word(word, result_to_return=0):
    result = requests.get(
        f"https://www.urbandictionary.com/define.php?term={word}")

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

        # Parse definitions and remove wotd from parsed definitions
        definitions = parse_definitions(soup)
        definitions.pop(1)

        if result_to_return <= len(definitions) and result_to_return != 0:
            return definitions[result_to_return-1]
        else:
            return definitions[0]


sys.modules[__name__] = scrape_word
