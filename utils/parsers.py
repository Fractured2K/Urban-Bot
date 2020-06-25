def parse_definitions(soup):
    """
    Parses and formats definitions from soup, 
    returning a list of dictionaries.

    :param soup:
    :return definitions:
    """

    # Definition panels
    definition_panels = soup.find_all("div", class_="def-panel")
    # Store
    definitions = []

    for result in range(len(definition_panels)):
        # Current definition block
        definition = definition_panels[result]

        # Defined word -> "Stupendous"
        word = definition.find(class_="word").text

        # Word URL
        word_url = word.split(' ')
        word_url = '+'.join(word_url)
        word_url = f"https://www.urbandictionary.com/define.php?term{word_url}"

        # Word definition -> "Of colossal excellence or greatness. The most esteemed level of hierarchical stature."
        word_definition = definition.find(class_="meaning").text

        # List of examples -> ["", "Elon Musk and his companies are quite stupendous", ""]
        word_examples = (definition.find(class_="example").text).split('"')
        # Removes empty strings from list -> ["Elon Musk and his companies are quite stupendous"]
        cleaned_word_examples = [
            word for word in word_examples if len(word) != 0]

        # Contributor -> "by Evolved guppy June 22, 2020"
        word_contributor = definition.find(class_="contributor").text

        # Definition Likes/Dislikes
        word_ratings = definition.find_all(class_="count")
        word_ratings = [word_ratings[0].text, word_ratings[1].text]

        formatted_definition = dict()
        formatted_definition["word"] = word
        formatted_definition["url"] = word_url
        formatted_definition["word_definition"] = word_definition
        formatted_definition["contributor"] = word_contributor
        formatted_definition["word_examples"] = cleaned_word_examples
        formatted_definition["ratings"] = word_ratings

        definitions.append(formatted_definition)

    return definitions
