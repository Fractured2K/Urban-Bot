def parse_definitions(soup):
    """
    Parses definitions from soup, 
    returning a list of dictionaries that contain 
    a word, word_definition and example of the word.

    :param soup:
    :return definitions:
    """
    # Definition blocks
    definition_blocks = soup.find_all("div", class_="def-panel")
    # Store
    definitions = []

    for result in range(len(definition_blocks)):
        # Current definition block
        definition = definition_blocks[result]

        # Defined word -> "Stupendous"
        word = definition.find(class_="word").text

        # Word definition -> "Of colossal excellence or greatness. The most esteemed level of hierarchical stature."
        word_definition = definition.find(class_="meaning").text

        # List of examples -> ["", "Elon Musk and his companies are quite stupendous", ""]
        word_examples = (definition.find(class_="example").text).split('"')
        # Removes empty strings from list -> ["Elon Musk and his companies are quite stupendous"]
        cleaned_word_examples = [
            word for word in word_examples if len(word) != 0]

        # Format scraped definition
        formatted_definition = dict()
        formatted_definition["word"] = word
        formatted_definition["word_definition"] = word_definition
        formatted_definition.setdefault(
            "word_examples", []).append(cleaned_word_examples)

        definitions.append(formatted_definition)

    return definitions
