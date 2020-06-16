import sys
import requests
import math
import random
from bs4 import BeautifulSoup
from utils.parsers import parse_definitions


def scrape_random_word():
    random_page_num = random.randint(1, 1000)
    result = requests.get(
        f"https://www.urbandictionary.com/random.php?page={random_page_num}")

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
        random_result_num = random.randint(0, len(definitions) - 1)

        # Pop off and return pseudo random result
        return definitions.pop(random_result_num)


sys.modules[__name__] = scrape_random_word
