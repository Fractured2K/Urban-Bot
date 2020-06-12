import sys
from discord import Embed


def error_message(error):
    return Embed(title=error, color=0xf55353)


def define_message(word):
    embed = Embed(title=word["word"],
                  description=word["word_definition"], color=0x0b4ee7)

    return embed
