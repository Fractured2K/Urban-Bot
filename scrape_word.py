import sys
import requests
from bs4 import BeautifulSoup


def scrape_word(word, result_to_return=0):
    result = requests.get(
        f"https://www.urbandictionary.com/define.php?term={word}")

    # Handle 500 error
    if result.status_code == 500:
        return {
            "error": "Sorry, but something went wrong. Try again later"
        }

    # Handle 404 error
    if result.status_code == 404:
        return {
            "error": f"Sorry, but we couldn't find: {word}"
        }

    # Handle 200 (Successful page scrape)
    if result.status_code == 200:
        # Parse page
        soup = BeautifulSoup(result.content, 'lxml')

        # Scraped definitions
        scraped_definitions = soup.find_all("div", class_="def-panel")
        # Hold Formatted and scraped definitions
        definitions = []

        for result_num in range(len(scraped_definitions)):
            # Current definition result
            definition = scraped_definitions[result_num]

            # Skip word of the day
            if result_num == 1:
                continue

            # Defined word -> "Stupendous"
            word = definition.find(class_="word").text
            # Word definition -> "Of colossal excellence or greatness. The most esteemed level of hierarchical stature."
            word_definition = definition.find(class_="meaning").text
            # List of word examples -> ["", "Elon Musk and his companies are quite stupendous", ""]
            word_examples = (definition.find(class_="example").text).split('"')
            # Removes empty strings from list -> ["Elon Musk and his companies are quite stupendous"]
            word_examples = [word for word in word_examples if len(word) != 0]

            # Format scraped word and word data in dictionary
            formatted_definition = dict()
            formatted_definition["word"] = word
            formatted_definition["word_definition"] = word_definition
            formatted_definition.setdefault(
                "word_examples", []).append(word_examples)

            definitions.append(formatted_definition)

        if result_to_return <= len(definitions):
            return definitions[result_to_return-1]
        else:
            return definitions[0]


sys.modules[__name__] = scrape_word
