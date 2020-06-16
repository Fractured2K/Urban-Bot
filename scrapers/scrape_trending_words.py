import sys
import requests
from bs4 import BeautifulSoup


def scrape_trending_words():
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
        formatted_trending_words = []

        trending_words = soup.find(class_="alphabetical").children

        for num, word in enumerate(trending_words):
            formatted_word = dict()
            formatted_word["word"] = word.a.text
            formatted_word["num"] = num+1

            formatted_trending_words.append(formatted_word)

        return formatted_trending_words


sys.modules[__name__] = scrape_trending_words
